import cv2
from cv2 import cv2
import pyautogui
import numpy as np
import time

import cv2
import numpy as np
import imutils

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