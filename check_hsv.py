import cv2
import numpy as np
import imutils

def find_circles(input,output):
    circles = cv2.HoughCircles(input, cv2.HOUGH_GRADIENT, 1.5, 120, param1=30, param2=15, minRadius=0, maxRadius=30)
    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(output, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(output, center, radius, (255, 0, 255), 3)
    except:
        pass


# greenLower = (80, 73, 75)
# greenUpper = (102, 132, 255)

# greenLower = (90, 71, 56)
# greenUpper = (106, 212, 233) #b=11

# greenLower = (75, 50, 52)
# greenUpper = (99, 83, 255) #b=0

if __name__ == '__main__':
    def nothing(*arg):
        pass

img = cv2.imread("rl3.jpg")

cv2.namedWindow( "result" )
cv2.namedWindow( "settings" )

cv2.createTrackbar('im', 'settings', 0, 4, nothing)
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
cv2.createTrackbar('bloor', 'settings', 0, 10, nothing)

unit_to_img = {
    0: 'ball.PNG',
    1: "rl.jpg",
    2: "rl2.jpg",
    3: "rl3.jpg",
    4: "rl_light.jpg"
}

while True:
    im = cv2.getTrackbarPos('im', 'settings')
    img = cv2.imread(unit_to_img[im])
    if img.shape[1] > 600:
        img = imutils.resize(img, width=600)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

    bloor = cv2.getTrackbarPos('bloor', 'settings')
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    if bloor % 2 == 0:
        bloor = bloor + 1

    h_min = np.array((h1, s1, v1), np.uint8)
    h_max = np.array((h2, s2, v2), np.uint8)

    # h_min = np.array((75, 50, 52), np.uint8)
    # h_max = np.array((99, 83, 255), np.uint8)

    hsv = cv2.GaussianBlur(hsv, (bloor, bloor), 2)
    thresh = cv2.inRange(hsv, h_min,h_max )
    dst = cv2.bitwise_and(img, img, mask=thresh)
    find_circles(thresh, dst)
    cv2.imshow('result', dst)

    ch = cv2.waitKey(5)
    if ch == 27:
        break