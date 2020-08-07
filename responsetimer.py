import time
import getch as g
import numpy as np
import cv2 as cv
import random as rd

count=0
row=800
col=1024
mask = 255*np.ones((row,col,3),np.uint8)

mask = cv.circle(mask,(int(col/2),int(row/2)), 5, (0,0,0), -1)
mask = cv.circle(mask,(int(col/2),int(row/2)), 10, (0,0,0), 3)

while True:
	print("Press Space to start : ")
	start_value = g.getch()
	if start_value == ' ':
		break

while True:
	while (count<10):
		random_row = rd.randint(10,int(0.90*row))
		random_col = rd.randint(10,int(0.90*col))
		random_wait = rd.randint(50,500)
		random_sleep = rd.randint(1000,4000)
		time.sleep(int(random_sleep/1000))
		mask = cv.circle(mask,(random_col,random_row), 5, (0,0,0), -1)
		cv.imshow("Image",mask)
		cv.waitKey(random_wait)	
		mask = cv.circle(mask,(random_col,random_row), 5, (255,255,255), -1)
		cv.imshow("Image",mask)
		cv.waitKey(5)

		start = time.time()
		while True:
			val = g.getch()
			if val == ' ':
				break
		finish = time.time()
		print(finish-start)
	
		count = count + 1	

	print("The Program is complete!")
	k = cv.waitKey(0) & 0xff 
	if k==27:
		break

cv.destroyAllWindows()
