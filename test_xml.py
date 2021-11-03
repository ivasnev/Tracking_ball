import cv2
import numpy as np
import imutils
from PIL import Image, ImageDraw

# Opening the image from files
imaging = cv2.imread("rl3.jpg")

imaging = np.asarray(imaging)

# Altering properties of image with cv2
imaging_gray = cv2.cvtColor(imaging, cv2.COLOR_RGB2GRAY)
imaging_rgb = cv2.cvtColor(imaging, cv2.COLOR_BGR2RGB)

# Importing Haar cascade classifier xml data
xml_data = cv2.CascadeClassifier('haarcascade\cascade.xml')
# Detecting object in the image with Haar cascade classifier
detecting = xml_data.detectMultiScale(imaging)
# Amount of object detected
amountDetecting = len(detecting)
# Using if condition to highlight the object detected
if amountDetecting != 0:
    for(a, b, width, height) in detecting:
        cv2.rectangle(imaging,(a, b), # Highlighting detected object with rectangle
                     (a + height, b + width),
                     (0, 275, 0), 9)
        break
# Displaying image in the output
if imaging.shape[1] > 600:
    imaging = imutils.resize(imaging, width=600)
cv2.imshow('result',imaging)
cv2.waitKey(0)