import cv2 as cv
import numpy as np

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

cap = cv.VideoCapture(0)

while(True):

	ret,frame = cap.read()
	gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray_frame,1.3,5)
	for (x,y,w,h) in faces:
		cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

		roi_gray = gray_frame[y:y+h,x:x+w]
		roi_color = frame[y:y+h,x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes :
			cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),3)


	cv.imshow('Image',frame)
	
	k = cv.waitKey(30) & 0xff 

	if k==27:
		break

cap.release()

cv.destroyAllWindows()
