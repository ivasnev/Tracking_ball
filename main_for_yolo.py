import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageDraw
import keyboard
import vgamepad as vg
from ultralytics import YOLO

# Загрузка обученной модели YOLO
def load_yolo_model():
    model = YOLO('path_to_your_yolov8_model.pt')  # Путь к вашей обученной модели YOLOv8
    return model

# Функция обнаружения мяча с использованием модели YOLOv8
def find_ball_yolo(model, screenshot):
    # Преобразование изображения в формат, ожидаемый моделью YOLOv8
    img = np.array(screenshot)
    results = model(img)

    # Извлечение координат ограничивающей рамки для первого обнаруженного объекта
    if results[0].boxes.shape[0] > 0:
        box = results[0].boxes[0].xyxy[0].cpu().numpy()  # Предполагается, что интересует только первая рамка
        x1, y1, x2, y2 = box.astype(int)
        x_ball = (x1 + x2) // 2
        y_ball = (y1 + y2) // 2
        return False, img, x_ball, y_ball
    else:
        return True, img, 0, 0

# Функция управления геймпадом на основе положения мяча
def control_gamepad(x_ball, y_ball, gamepad):
    gamepad.reset()
    if (x_ball == 0) and (y_ball == 0):
        gamepad.left_trigger_float(value_float=0.2)
        gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0.0)
    elif (768 <= x_ball <= 1152) and (0 <= y_ball <= 1080):
        tmp_trigger = (720 - y_ball) / 720
        tmp_trigger = max(tmp_trigger, 0.2)
        gamepad.right_trigger_float(value_float=tmp_trigger)
    elif (0 < x_ball <= 767) and (0 <= y_ball <= 1080):
        tmp_joystick = (-1) * ((960 - x_ball) / 960)
        tmp_trigger = (720 - y_ball) / 720
        tmp_trigger = max(tmp_trigger, 0.2)
        gamepad.right_trigger_float(value_float=tmp_trigger)
        gamepad.left_joystick_float(x_value_float=tmp_joystick, y_value_float=0.0)
    elif (1153 <= x_ball <= 1920) and (0 <= y_ball <= 1080):
        tmp_joystick = 1 - ((-1) * (x_ball - 1920) / 960)
        tmp_trigger = (720 - y_ball) / 720
        tmp_trigger = max(tmp_trigger, 0.2)
        gamepad.right_trigger_float(value_float=tmp_trigger)
        gamepad.left_joystick_float(x_value_float=tmp_joystick, y_value_float=0.0)
    time.sleep(0.01)
    gamepad.update()

def main():
    model = load_yolo_model()  # Загрузка модели YOLOv8
    gamepad = vg.VX360Gamepad()  # Инициализация геймпада

    keyboard.wait('space')  # Ожидание нажатия клавиши Space для начала
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # Пример нажатия кнопки на геймпаде
    gamepad.update()
    time.sleep(5.0)  # Ожидание 5 секунд перед стартом

    while True:
        if keyboard.is_pressed('0'):  # Выход из цикла по нажатию клавиши '0'
            break

        screenshot = pyautogui.screenshot()  # Захват скриншота
        pencil = ImageDraw.Draw(screenshot)
        pencil.rectangle((1620, 780, 1920, 1080), fill='black')

        Flag_b_not_seek, img, x_ball, y_ball = find_ball_yolo(model, screenshot)
        if not Flag_b_not_seek:
            cv2.circle(img, (x_ball, y_ball), 10, (0, 0, 255), 3)

        if img.shape[1] > 600:
            img = imutils.resize(img, width=600)
        cv2.imshow('result', img)
        cv2.waitKey(1)

        control_gamepad(x_ball, y_ball, gamepad)  # Управление геймпадом на основе координат мяча

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
