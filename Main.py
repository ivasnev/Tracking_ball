from cv2 import cv2
import pyautogui
import time

import cv2
import numpy as np
import imutils
from PIL import ImageDraw
import keyboard
import vgamepad as vg


def find_ball(n, xml_data, screenshot):
    imaging = np.asarray(screenshot)
    x, y = screenshot.size  # ширина (x) и высота (y) изображения
    imagings = []
    for j in range(n):
        for i in range(n):
            if i != n and j != n:
                imagings.append(np.asarray(
                    screenshot.crop(box=(x / n * i, y / n * j, x / n * (i + 1) - 1, y / n * (j + 1) - 1))))
    for i in range(n * n):
        detecting = xml_data.detectMultiScale(imagings[i])
        amountDetecting = len(detecting)
        if amountDetecting != 0:
            for (a, b, width, height) in detecting:
                img_check = np.asarray(screenshot.crop(box=(a - 40, b - 40, a + height + 40, b + width + 40)))
                detecting2 = xml_data.detectMultiScale(img_check)
                amountDetecting2 = len(detecting2)
                if amountDetecting2 != 0:
                    cv2.rectangle(imaging, (a, b),
                                  (a + height, b + width),
                                  (255, 0, 0), 9)
                    x_ball = int((i / y) * (1920 / n) + (a + int(height / 2)))
                    y_abll = int((i / x) * (1080 / n) + (b + int(width / 2)))
                    return False, imaging, x_ball, y_abll
    return True, imaging, 0, 0


def lets_go_keyboard(x, y, status):
    # status[] w-0 a-1 s-2 d-3
    if status[0]: print('w')
    if status[2]: print('s')
    if status[1]: print('a')
    if status[3]: print('d')
    if (768 <= x and x <= 1152) and (0 <= y and y <= 1080):
        if status[2]: keyboard.release('s'); status[2] = False
        if status[1]: keyboard.release('a'); status[1] = False
        if status[3]: keyboard.release('d'); status[3] = False
        keyboard.press('w')
        status[0] = True
    elif (0 <= x and x <= 767) and (0 <= y and y <= 1080):
        if status[2]: keyboard.release('s'); status[2] = False
        if status[3]: keyboard.release('d'); status[3] = False
        keyboard.press('w+a')
        status[0] = True
        status[1] = True
    elif (1153 <= x and x <= 1920) and (0 <= y and y <= 1080):
        if status[2]: keyboard.release('s'); status[2] = False
        if status[1]: keyboard.release('a'); status[1] = False
        keyboard.press('w+d')
        status[0] = True
        status[3] = True
    else:
        if status[0]: keyboard.release('w'); status[0] = False
        if status[1]: keyboard.release('a'); status[1] = False
        keyboard.press('s+d')
        status[2] = True
        status[3] = True
    return status


def lets_go_gamepad(x, y, gamepad):
    gamepad.reset()
    if (x == 0) and (y == 0):
        gamepad.left_trigger_float(value_float=0.2)
        gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)
    elif (768 <= x and x <= 1152) and (0 <= y and y <= 1080):
        tmp_trigger = (720 - y) / 720
        if tmp_trigger == 0:
            tmp_trigger = 0.5
        elif tmp_trigger <= 0.2:
            tmp_trigger = 0.2
        gamepad.right_trigger_float(value_float=tmp_trigger)
    elif (0 < x and x <= 767) and (0 <= y and y <= 1080):
        tmp_joystick = (-1) * ((960 - x) / 960)
        tmp_trigger = (720 - y) / 720
        if tmp_trigger == 0:
            tmp_trigger = 0.5
        elif tmp_trigger <= 0.2:
            tmp_trigger = 0.2
        gamepad.right_trigger_float(value_float=tmp_trigger)
        gamepad.left_joystick_float(x_value_float=tmp_joystick, y_value_float=0.0)

    elif (1153 <= x and x <= 1920) and (0 <= y and y <= 1080):
        tmp_joystick = 1 - ((-1) * (x - 1920) / 960)
        tmp_trigger = (720 - y) / 720
        if tmp_trigger == 0:
            tmp_trigger = 0.5
        elif tmp_trigger <= 0.2:
            tmp_trigger = 0.2
        gamepad.right_trigger_float(value_float=tmp_trigger)
        gamepad.left_joystick_float(x_value_float=tmp_joystick, y_value_float=0.0)
    time.sleep(0.01)
    gamepad.update()


def main():
    gamepad = vg.VX360Gamepad()  # vg.VDS4Gamepad()
    keyboard.wait('space')
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(5.0)
    xml_data = cv2.CascadeClassifier('haarcascade\cascade.xml')
    while True:
        if keyboard.is_pressed('~'):
            break
        screenshot = pyautogui.screenshot()
        pencil = ImageDraw.Draw(screenshot)
        pencil.rectangle((1620, 780, 1920, 1080), fill='black')
        x_ball, y_ball = 960, 540

        for i in range(1, 5):
            Flag_b_not_seek, imaging, x_ball, y_ball = find_ball(i, xml_data, screenshot)
            if not (Flag_b_not_seek):
                break
        cv2.circle(imaging, (x_ball, y_ball), 10, (0, 0, 255), 3)

        if imaging.shape[1] > 600:
            imaging = imutils.resize(imaging, width=600)
        cv2.imshow('result', imaging)
        cv2.waitKey(1)
        # status = lets_go_keyboard(x_ball,y_ball,status)
        lets_go_gamepad(x_ball, y_ball, gamepad)


main()