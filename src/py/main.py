import cv2
import numpy as np 
path = r'C:\Users\ASUS\Downloads\image.png'
frame = cv2.imread(path,1)

while True:
    # Belt
    belt = frame[55:630,185:260]
    gray_belt =cv2.cvtColor(belt,cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_belt,148,255,cv2.THRESH_BINARY)
    # detect the nuts
    contours, _ = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)
        # Calculate area
        area = cv2.contourArea(cnt)            
        cv2.putText(belt, str(area), (x, y), 1, 1, (0, 255, 0))
        cv2.rectangle(belt,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Frame",frame)
    cv2.imshow("Belt",belt)
    cv2.imshow("threshold",threshold)
    key = cv2.waitKey(0)
    if key == 27:
        break


frame.release()
cv2.destroyAllWindows()

