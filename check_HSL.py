import cv2
import numpy as np

img = cv2.imread("ball.PNG")
# greenLower = (80, 73, 75)
# greenUpper = (102, 132, 255)

if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow( "result" )
cv2.namedWindow( "settings" )

cv2.createTrackbar('h1', 'settings', 0, 360, nothing)
cv2.createTrackbar('l1', 'settings', 0, 100, nothing)
cv2.createTrackbar('s1', 'settings', 0, 100, nothing)
cv2.createTrackbar('h2', 'settings', 0, 360, nothing)
cv2.createTrackbar('l2', 'settings', 0, 100, nothing)
cv2.createTrackbar('s2', 'settings', 0, 100, nothing)
cv2.createTrackbar('bloor', 'settings', 0, 10, nothing)

while True:
    hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS_FULL )

    bloor = cv2.getTrackbarPos('bloor', 'settings')
    h1 = cv2.getTrackbarPos('h1', 'settings')
    l1 = cv2.getTrackbarPos('l1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    l2 = cv2.getTrackbarPos('l2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')

    if bloor % 2 == 0:
        bloor = bloor + 1

    h_min = np.array((h1, l1, s1), np.uint8)
    h_max = np.array((h2, l2, s2), np.uint8)


    hsv = cv2.GaussianBlur(hls, (bloor, bloor), 2)
    thresh = cv2.inRange(hls, h_min,h_max )

    dst = cv2.bitwise_and(img, img, mask=thresh)
    cv2.imshow('result', dst)

    ch = cv2.waitKey(5)
    if ch == 27:
        break