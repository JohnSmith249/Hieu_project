import cv2 as cv
import caer
import numpy as np
import pandas as pd

master_fol = "C:\\Users\\DELL\\Desktop\\temper\\Hieu C7\\"
test_img_fol = "C:\\Users\\DELL\\Desktop\\Hieu C7\\test_image_fol\\"
test_vid_fol = "C:\\Users\\DELL\\Desktop\\Hieu C7\\test_video_fol\\"


# *******************************************************************************************

def rescaleFrame(frame, scale):
    # img, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)


# Translation
def translate(img,x,y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down


# Rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

# *******************************************************************************************

# test_img_1 = cv.imread(test_img_fol + 'subject_1.jpg')
# subject_01 = rescaleFrame(test_img_1, 0.35)
# cv.imshow('test', subject_01)
# cv.waitKey(0)

test_img_1 = cv.imread(test_img_fol + 'subject_1.jpg')
subject_01 = rescaleFrame(test_img_1, 0.10)
cv.imshow('Subject 01', subject_01)

# *******************************************************************************************
# capture = cv.VideoCapture(test_vid_fol + "test_video_2.mp4")
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame,0.5)
#
#     # cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)
#
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()

# *******************************************************************************************

# blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# *******************************************************************************************

# paint all the img
# blank[:] = 0,0,255
# blank[200:300, 300:400] = 235, 252, 3
# cv.imshow('Green', blank)

# ***********************************************************************************************

# draw rectangle
# cv.rectangle(blank, (0,0), (250,250), (0, 255, 0), thickness = 2)
# cv.imshow('Rectangle', blank)

# ************************************************************************************************

# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255,255,0), thickness=-1)
# cv.imshow('Circle', blank)

# ************************************************************************************************



# Gray_scale_img Function
# gray = cv.cvtColor(subject_01, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur_scale_img Function
# blur = cv.GaussianBlur(subject_01,(7,7), cv.BORDER_WRAP)
# cv.imshow('Blur', blur)

# Edge Cascade
# canny = cv.Canny(subject_01, 125, 175)
# cv.imshow('Canny_Edges', canny)

# Dilating the image
# dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow('Dialated', dilated)

#Eroding
# eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize
# resized = cv.resize(test_img_1, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# Cropping
# cropped = test_img_1[50:200, 200:400]
# cv.imshow('Cropped', cropped)

# ****************************************************************************************

# translated = translate(subject_01, -100, 100)
# cv.imshow('Translated', translated)

# rotated = rotate(subject_01, 45)
# cv.imshow('Rotated', rotated)

# Resizing
# resized = cv.resize(test_img_1, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# Flipping
# flip = cv.flip(subject_01, -1)
# cv.imshow('Flip', flip)
#
# flip2 = cv.flip(subject_01, 2)
# cv.imshow('Flip_2', flip2)

# Cropping

cropped = subject_01[100:200, 100:200]
cv.imshow('Cropped', cropped)

print(test_img_1.shape)

cv.waitKey(0)
























