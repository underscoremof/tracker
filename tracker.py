import cv2
import numpy as np

cap = cv2. VideoCapture(1)

# Filter out green color channel
def green():
    global mask
    lower_green = (40, 50, 50)
    upper_green = (80, 255, 255)
    mask = cv2.inRange(hsv, lower_green, upper_green)

# Filter out red color channel
def red():
    global mask
    lower_red = (0, 50, 50)
    upper_red = (10, 255, 255)
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = (170, 50, 50)
    upper_red = (180, 255, 255)
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.bitwise_or(mask1, mask2)

def blue():
    global mask
    lower_blue=(100, 50, 50)
    upper_blue=(130, 255, 255)
    mask=cv2.inRange(hsv, lower_blue, upper_blue)

while True:
    ret, frame =cap.read()

    hsv = cv2. cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue()

    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, dp=1, minDist=20, 
                               param1=50, param2=30, minRadius=0, maxRadius=0)
    
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        print('test', circles)
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)

    cv2.imshow('image', hsv)
    #cv2. imshow('orig', frame)
    c =cv2.waitKey(1)
    if c &0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

print(hsv)