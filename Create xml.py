from cv2 import cv2
import pyautogui
import time
import cv2


def make_photo():
    time.sleep(15)
    i = 71
    while True:
        screenshot = pyautogui.screenshot()  # создание скрина с сохранением
        screenshot.save("Bad//" + str(i) + ".bmp")  # сохранение скрина
        time.sleep(2)
        i += 1
    cv2.waitKey(0)

make_photo()