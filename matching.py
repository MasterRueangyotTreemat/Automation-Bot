#pip install opencv-python
#pip install numpy
#pip install pyautogui
#pip install pyperclip
import cv2
import numpy as np
import pyautogui as pg
import time
import pyperclip


def Screenshot():
	time.sleep(3)
	im = np.array(pg.screenshot('screen.jpg'))
	return im


def BOT(temp='template1.jpg'):

	img = Screenshot()

	img_temp = cv2.imread(temp)
	template = cv2.cvtColor(img_temp, cv2.COLOR_BGR2GRAY)


	screen = cv2.imread('screen.jpg',cv2.IMREAD_GRAYSCALE)

	result = cv2.matchTemplate(template,screen, cv2.TM_CCOEFF_NORMED)

	#print(result)

	loc = np.where(result>=0.8)

	allpoint = []

	for pt in zip(*loc):
		#print(pt)
		allpoint.append(pt)

	print(allpoint)
	x = allpoint[0][1] + 10
	y = allpoint[0][0] + 10
	pg.moveTo(x,y)
	pg.click()



#BOT('template4.jpg')
#time.sleep(3)
#BOT('template5.jpg')



#cv2.imshow('img',result)
#cv2.waitKey(0)
#cv2.destroyAllWindows()