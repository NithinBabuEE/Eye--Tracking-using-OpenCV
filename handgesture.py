import cv2
import numpy as np
import math
cap = cv2.VideoCapture(0)
	 
while(1):
			  
	ret, frame = cap.read()
	frame=cv2.flip(frame,1)
	rows,cols,_ = frame.shape
	kernel = np.ones((3,3),np.uint8)
	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	 
# define range of skin color in HSV
	lower_skin = np.array([0,20,70], dtype=np.uint8)
	upper_skin = np.array([20,255,255], dtype=np.uint8)
	
 #extract skin colur imagw  
	mask = cv2.inRange(hsv, lower_skin, upper_skin)
	

	
#extrapolate the hand to fill dark spots within
	mask = cv2.dilate(mask,kernel,iterations = 4)
	
#blur the image
	mask = cv2.GaussianBlur(mask,(5,5),100) 
	
	
	
#find contours
	contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#find contour of max area(hand)
	cnt = max(contours, key = lambda x: cv2.contourArea(x))
	
	x,y,w,h = cv2.boundingRect(cnt)
	frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)	
	if  x >= int(0.8*cols) and y <= int(0.9*rows) and y>= int(0.1*rows):
		print("RIGHT")
	if  x <= int(0.2*cols) and y <= int(0.9*rows) and y>= int(0.1*rows):   
		print("LEFT") 
	if  y <= int(0.2*rows) and x <= int(0.1*cols) and x>= int(0.9*cols):
		print("UP")
	if  y >= int(0.8*rows) and x <= int(0.1*cols) and x>= int(0.9*cols):
		print("Down")
	cv2.imshow('Image',frame) 
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()    
cv2.destroyAllWindows()

