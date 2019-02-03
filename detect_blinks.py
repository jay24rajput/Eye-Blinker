# USAGE
# python detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat --video blink_detection_demo.mp4
# python detect_blinks.py --shape-predictor shape_predictor_68_face_landmarks.dat

# import the necessary packages
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
import level3
import bright
import generate_report

def eye_aspect_ratio(eye):


	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	A = dist.euclidean(eye[1], eye[5])
	B = dist.euclidean(eye[2], eye[4])

	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = dist.euclidean(eye[0], eye[3])

	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)

	# return the eye aspect ratio
	return ear
 
# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-p", "--shape-predictor", required=True,
# 	help="path to facial landmark predictor")
# ap.add_argument("-v", "--video", type=str, default="",
# 	help="path to input video file")
# args = vars(ap.parse_args())
 
# define two constants, one for the eye aspect ratio to indicate
# blink and then a second constant for the number of consecutive
# frames the eye must be below the threshold

def main():

	elapsed_time_values = set()
	wow_flag=0
	wow_flag2=0
	wow_flag3=0
	wow_flag4=0
	problems = [0,0,0,0]
	blinks=[0,0,0,0]
	blinksArray=[]

	EYE_AR_THRESH = 0.3
	EYE_AR_CONSEC_FRAMES = 3

	# initialize the frame counters and the total number of blinks
	COUNTER = 0
	TOTAL = 0

	# initialize dlib's face detector (HOG-based) and then create
	# the facial landmark predictor
	print("[INFO] loading facial landmark predictor...")
	detector = dlib.get_frontal_face_detector()
	# print(type(args["shape_predictor"]))
	# exit()
	# predictor = dlib.shape_predictor(args["shape_predictor"])
	predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
	# print(type(predictor))
	# exit()
	# predictor="shape_predictor_68_face_landmarks.dat"

	# grab the indexes of the facial landmarks for the left and
	# right eye, respectively
	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
	start_time = time.time()
	# start the video stream thread
	print("[INFO] starting video stream thread...")
	vs = cv2.VideoCapture(0)
	fileStream = True
	# vs = VideoStream(src=0).start()
	# vs = VideoStream(usePiCamera=True).start()
	# fileStream = False
	# time.sleep(1.0)
	ret, frame = vs.read()

	# loop over frames from the video stream
	while ret:
		# if this is a file video stream, then we need to check if
		# there any more frames left in the buffer to process

		# grab the frame from the threaded video file stream, resize
		# it, and convert it to grayscale
		# channels)
		ret,frame = vs.read()
		frame = imutils.resize(frame, width=450)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
		# cv2.imshow('frame',frame)

		# detect faces in the grayscale frame
		rects = detector(gray, 0)
	    
		# loop over the face detections
		for rect in rects:
			# determine the facial landmarks for the face region, then
			# convert the facial landmark (x, y)-coordinates to a NumPy
			# array
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
			# extract the left and right eye coordinates, then use the
			# coordinates to compute the eye aspect ratio for both eyes
			leftEye = shape[lStart:lEnd]
			rightEye = shape[rStart:rEnd]
			leftEAR = eye_aspect_ratio(leftEye)
			rightEAR = eye_aspect_ratio(rightEye)

			# average the eye aspect ratio together for both eyes
			ear = (leftEAR + rightEAR) / 2.0

			# compute the convex hull for the left and right eye, then
			# visualize each of the eyes
			leftEyeHull = cv2.convexHull(leftEye)
			rightEyeHull = cv2.convexHull(rightEye)
			cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
			cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

			# check to see if the eye aspect ratio is below the blink
			# threshold, and if so, increment the blink frame counter
			#while(USER DOES NOT PRESS STOP)
			elapsed_time = time.time()-start_time
			elapsed_time = round(elapsed_time)
			
			elapsed_time=elapsed_time%60
			
			elapsed_time_values.add(elapsed_time)
			print(elapsed_time)
			
			

			if 15 in elapsed_time_values and wow_flag==0:
				blinks[0]=TOTAL
				print("the array is",blinks)
				print("Total is",blinks[0])
				if(TOTAL<5):
					problems[0]=1
					print("yo")

				wow_flag=1
				wow_flag4=0
				
							
					
	        
			elif 30 in elapsed_time_values and wow_flag2==0:
				blinks[1]=TOTAL-blinks[0]
				print("the array is",blinks)
				print("total is",TOTAL-blinks[0])
				if(TOTAL-blinks[0]<5):
					problems[1]=1
					print("YO1")
				wow_flag2=1
					
				
				

			elif 45 in elapsed_time_values and wow_flag3==0:
				blinks[2]=TOTAL-(blinks[0]+blinks[1])
				print("the array is",blinks)
				print("total is",TOTAL-(blinks[0]+blinks[1]))
				if(TOTAL-(blinks[0]+blinks[1])<5):
					problems[2]=1
					print("Yo3")
				wow_flag3=1
				
					
				

			elif 0 in elapsed_time_values and wow_flag4==0:
				blinks[3]=TOTAL-(blinks[0]+blinks[1]+blinks[2])
				print("the array is",blinks)
				print("total is",TOTAL-(blinks[0]+blinks[1]+blinks[2]))
				if(TOTAL-(blinks[0]+blinks[1]+blinks[2])<5):
					problems[3]=1
				TOTAL=0
				
				elapsed_time=0
				flag1=0
				flag2=0
				wow_flag4=1
				count=0
				print(problems)
				
				for i in range(0,len(problems)):
					if problems[i]==1:
						count+=1
				if count == 4:
					print("level 3 warning")
					#level 3 code
					subprocess.Popen(['notify-send',"Please look away from the screen for 15 seconds"])
					thirdLevel=level3.LookAway()
					thirdLevel.lookAway(detector,predictor,vs)
					vs=cv2.VideoCapture(0)
					flag1=1
				if flag1==0:
					for i in range(0,len(problems)-2):
						if problems[i]==1 and problems[i+1]==1 and problems[i+2] == 1:
							print("Level 2 warning")
							#level 2 code
							subprocess.Popen(['notify-send',"Level 2 Warning"])
							dimBrightness=bright.Brightness()
							dimBrightness.change_brightness(25)
							flag2=1
				if flag1==0 and flag2==0:			
					for i in range(0,len(problems)-1):
						if problems[i]==1 and problems[i+1]==1:
							print("Level 1 warning")		
							#level 1 code
							subprocess.Popen(['notify-send',"Level 1 Warning"])

				blinksArray+=blinks
				wow_flag=0
				wow_flag2=0
				wow_flag3=0
				blinks = [0,0,0,0]
				problems = [0,0,0,0]

				


				
			if 0 in elapsed_time_values:
				elapsed_time_values.remove(0)
			if 15 in elapsed_time_values:
				elapsed_time_values.remove(15)
			if 30 in elapsed_time_values:
				elapsed_time_values.remove(30)
			if 45 in elapsed_time_values:
				elapsed_time_values.remove(45)

			
				
			
			if ear < EYE_AR_THRESH:
				COUNTER += 1

			# otherwise, the eye aspect ratio is not below the blinkf
			# threshold
			else:
				# if the eyes were closed for a sufficient number of
				# then increment the total number of blinks
				if COUNTER >= EYE_AR_CONSEC_FRAMES:
					TOTAL += 1

				# reset the eye frame counter
				COUNTER = 0

			# draw the total number of blinks on the frame along with
			# the computed eye aspect ratio for the frame
			cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			cv2.putText(frame, "EAR: {:.2f}".format(ear), (300, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
	 
		# show the frame
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
	 
		# if the `q` key was pressed, break from the loop
		if key == ord("q"):
			report=generate_report.Report()
			report.save_report_data(blinksArray)
			break

	# do a bit of cleanup
	vs.release()
	cv2.destroyAllWindows()  

if __name__ == '__main__':
	main()
