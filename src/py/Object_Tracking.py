from collections import deque
from imutils.video import VideoStream
import numpy as np
import os
import argparse
import cv2
import imutils
import time

test_img_fol = "..\\test_image_fol\\"
test_vid_fol = "..\\test_video_fol\\"

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", type=str, default=test_vid_fol + "test_video_2.mp4", help="Path to videos")
# ap.add_argument("-v", "--video", help="Path to videos")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

yellowLower = (20, 100, 100)
yellowUpper = (30, 255, 255)

redLower = (170, 70, 50)
redUpper = (180, 255, 255)

# ************************************************************************************************
Lower_color = yellowLower
Upper_color = yellowUpper

Lower_color_1 = redLower
Upper_color_1 = redUpper
# ************************************************************************************************

pts = deque(maxlen=args["buffer"])

# *****************************************************************

if not args.get("video", False):
	vs = VideoStream(src=0).start()
	# vs = cv2.VideoCapture(args['video'])
	print(args.get("video", True))
else:
	vs = cv2.VideoCapture(args["video"])
	print('there')

# ******************************************************************

# print(args["video"])
# print(args["buffer"])
# vs = cv2.VideoCapture(args["video"])
# print(args["video"])

time.sleep(2.0)

while True:
	frame = vs.read()
	frame = frame[1] if args.get("video", False) else frame
	if frame is None:
		break
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	mask = cv2.inRange(hsv, Lower_color, Upper_color)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

	mask_1 = cv2.inRange(hsv, Lower_color_1, Upper_color_1)
	mask_1 = cv2.erode(mask_1, None, iterations=2)
	mask_1 = cv2.dilate(mask_1, None, iterations=2)

	# (x, y) center of the ball

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None

	cnts_1 = cv2.findContours(mask_1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts_1 = imutils.grab_contours(cnts_1)
	center1 = None

	if len(cnts) > 0:
		c = max(cnts, key=cv2.contourArea)
		# print(cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		print(str(round(x))+ ', '+ str(round(y)))
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		if radius > 10:
			cv2.circle(frame, (int(x), int(y)), int(radius),
					   (0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
	pts.appendleft(center)

	if len(cnts_1) > 0:
		c1 = max(cnts_1, key=cv2.contourArea)
		# print(cv2.contourArea)
		((x1, y1), radius1) = cv2.minEnclosingCircle(c1)
		print(str(round(x1))+ ', '+ str(round(y1)))
		M1 = cv2.moments(c1)
		center1 = (int(M1["m10"] / M1["m00"]), int(M1["m01"] / M1["m00"]))
		if radius1 > 10:
			cv2.circle(frame, (int(x1), int(y1)), int(radius1),
					   (0, 255, 255), 2)
			cv2.circle(frame, center1, 5, (0, 0, 255), -1)
	pts.appendleft(center1)

	# for i in range(1, len(pts)):
	# 	if pts[i - 1] is None or pts[i] is None:
	# 		continue
	# 	thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
	# 	cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
	cv2.imshow("Frame", frame)
	if cv2.waitKey(20) & 0xFF == ord('d'):
		break
if not args.get("video", False):
	vs.stop()
else:
	vs.release()
cv2.destroyAllWindows()