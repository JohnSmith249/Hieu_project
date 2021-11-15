import cv2
import pandas
import numpy as np
import os

master_fol = "C:\\Users\\DELL\\Desktop\\temper\\Hieu C7\\"
test_img_fol = "C:\\Users\\DELL\\Desktop\\temper\\Hieu C7\\test_image_fol\\"
test_vid_fol = "C:\\Users\\DELL\\Desktop\\temper\\Hieu C7\\test_video_fol\\"

# ********************************************************************************************************

vid_object = cv2.VideoCapture(0)

while True:
    _, frame = vid_object.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])

    lower_white = np.array([177,7,7])
    upper_white = np.array([104, 104, 237])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # mask2 = cv2.inRange(hsv, lower_white, upper_white)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    # print(contours)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    # cv2.imshow("Mask2", mask2)


    if cv2.waitKey(20) & 0xff == ord('d'):
        break
vid_object.release()
cv2.destroyAllWindows()

