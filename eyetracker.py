import cv2 as cv
from math import sqrt

cap= cv.VideoCapture("eyeDetection3.mp4")
# cap = cv.VideoCapture(0)
x_eye_prev=0 ; y_eye_prev=0	
while (cap.isOpened()):
	ret,frame=cap.read()
	rows,cols,_=frame.shape
	gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY) 
	gray_frame=cv.GaussianBlur(gray_frame,(5,5),0)
	_,thresh_frame=cv.threshold(gray_frame,10,255,cv.THRESH_BINARY_INV)
	contours,hierarchy=cv.findContours(thresh_frame, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contours=sorted(contours, key=lambda x: cv.contourArea(x), reverse=True)	

	for cnt in contours:
		(x,y,w,h)=cv.boundingRect(cnt)

		x_eye=x+int(w/2) ; y_eye=y+int(h/2)
		x_centre=int(cols/2) ; y_centre=int(rows/2)

		cv.line(frame,(x_eye,0),(x_eye,rows),(0,255,0),3)
		cv.line(frame,(0,y_eye),(cols,y_eye),(0,255,0),3)
		if x_eye==x_eye_prev and y_eye==y_eye_prev:
			distance = sqrt((x_eye - x_centre)**2 + (y_eye - y_centre)**2)
			print(distance)
		x_eye_prev=x_eye ; y_eye_prev=y_eye	
		break

	cv.imshow("Thresh",thresh_frame)
	cv.imshow("Eye",frame)	

	if cv.waitKey(30) == 27:
		break

cap.release()
cv.destroyAllWindows()			