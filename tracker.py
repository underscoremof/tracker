import cv2

cap = cv2. VideoCapture(1)

while True:
    ret, frame =cap.read()
    cv2.imshow('image', frame)
    c =cv2.waitKey(1)
    if c &0xFF == ord('q'):
        cv2.destroyAllWindows()
        break