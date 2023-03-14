import cv2
import numpy as np

def nothing(a):
    pass

cap = cv2.VideoCapture(1)
cv2.namedWindow('stream')
cv2.createTrackbar('green', 'stream', 90, 255, nothing)

coordinates=np.zeros((0,2), dtype=int)
while True:
    ret, frame=cap.read()

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    v=cv2.getTrackbarPos('green', 'stream')
    lower_green=(45, v, v)
    upper_green=(75, 255, 255)
    mask=cv2.inRange(hsv, lower_green, upper_green)

    circles=cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=50, param2=30, minRadius=50, maxRadius=0)

    if circles is not None:
        circles=np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            new_coordinates=np.array([[x,y]])
            coordinates=np.append(coordinates, new_coordinates, axis=0)
            #print(x, y)

    cv2.imshow('stream', frame)

    c=cv2.waitKey(1)
    if c&0xFF == ord('q'):
        break

cv2.destroyAllWindows
print(coordinates)
