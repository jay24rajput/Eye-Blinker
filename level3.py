from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import subprocess
from playsound import playsound

class LookAway:
	def lookAway(self,detector,predictor,cap):
		TIME_TO_LOOK_AWAY=5

		# detector = dlib.get_frontal_face_detector()
		# predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

		print('I am in level 3')

		# cap=cv2.VideoCapture(0)
		ret, frame = cap.read()
		startTime=0
		endTime=0
		while ret:
			ret,frame = cap.read()
			frame = imutils.resize(frame, width=450)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			cv2.imshow('lookAway',frame)

			# detect faces in the grayscale frame
			rects = detector(gray, 0)
			if len(rects)==0 and startTime==0:
				startTime=time.time()

			if len(rects)==1:
				startTime=time.time()

			elpased_time = time.time()-startTime

			if round(elpased_time) >=TIME_TO_LOOK_AWAY:
				#print("congoooooooooooooooooooo")
				playsound('beep.mp3')
				break

			print(round(elpased_time))




			key = cv2.waitKey(1) & 0xFF
		  
			# if the `q` key was pressed, break from the loop
			if key == ord("q"):
				break

		cap.release()
		cv2.destroyAllWindows()
