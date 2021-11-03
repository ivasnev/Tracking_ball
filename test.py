import cv2
from cv2 import cv2
import pyautogui
import numpy as np
import time

import cv2
import numpy as np
import imutils


def loading_displaying_saving():
    # img = cv2.imread('gendelf.PNG', cv2.IMREAD_GRAYSCALE)
    # cv2.imshow('gendelf.PNG', img)
    # cv2.waitKey(0)
    # cv2.imwrite('gendelf.PNG', img)

    screenshot = pyautogui.screenshot()  # создание скрина с сохранением
    # screenshot.save("screenshot.png") #сохранение скрина
    cv2.imshow("screenshot.png", np.asarray(screenshot))  # преобразование mat в numpy array
    cv2.waitKey(0)


def colored_mask(img, threshold=-1):
    # Размытие для удаления мелких шумов.
    denoised = cv2.medianBlur(img, 3)

    # Сохранение в ЧБ для получения маски.
    gray = cv2.cvtColor(denoised, cv2.COLOR_BGR2GRAY)

    # Получение цветной части изображения.
    adaptiveThreshold = threshold if threshold >= 0 else cv2.mean(img)[0]
    color = cv2.cvtColor(denoised, cv2.COLOR_BGR2HLS)
    mask = cv2.inRange(color, (80, 30, 80), (260, 90, 110))

    # Создание маски цветной части изображения.
    dst = cv2.bitwise_and(gray, gray, mask=mask)
    return dst


def equals(first, second, epsilon):
    diff = cv2.subtract(first, second)
    nonZero = cv2.countNonZero(diff)
    area = first.size * epsilon
    return nonZero <= area

def find_circles(input,output):
    circles = cv2.HoughCircles(input, cv2.HOUGH_GRADIENT, 1.5, 120, param1=30, param2=15, minRadius=0, maxRadius=30)

    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # circle center
        cv2.circle(output, center, 1, (0, 100, 100), 3)
        # circle outline
        radius = i[2]
        cv2.circle(output, center, radius, (255, 0, 255), 3)


# Load an image
img = cv2.imread('rl.jpg')
# Resize an image
if img.shape[1] > 600:
    img = imutils.resize(img, width=600)

# greenLower = (80, 73, 75)
# greenUpper = (102, 132, 255)

greenLower = (90, 71, 56)
greenUpper = (106, 212, 233) #b=11

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsv = cv2.GaussianBlur(hsv, (3, 3), 2)
thresh = cv2.inRange(hsv, greenLower, greenUpper)

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

background = img.copy()
# mask = cv2.inRange(img, greenLower, greenUpper)
mask = colored_mask(img)

canny = cv2.Canny(thresh, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)

find_circles(canny,canny)
find_circles(closed,closed)
find_circles(thresh,thresh)
find_circles(grey,img)
find_circles(mask,mask)

cv2.imshow('canny', canny)
cv2.imshow('closed', closed)
cv2.imshow('thresh', thresh)
cv2.imshow("Original", img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
