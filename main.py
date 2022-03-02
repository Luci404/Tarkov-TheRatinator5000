import cv2
import numpy as np
import pyautogui as pg
from scipy.spatial import distance

screenshot = pg.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

sortedItems = []
for i in pg.locateAllOnScreen("icon01.png", confidence=0.7):
	alreadyContains = False
	for sortedItem in sortedItems:
		a = (float(i.top), float(i.left), 0.0)
		b = (float(sortedItem.top), float(sortedItem.left), 0.0)
		dst = distance.euclidean(a, b)
		if (dst <= 25.0):
			alreadyContains = True
			print("Duplicate found, Dist:" + str(dst)) 

	if not alreadyContains:
		sortedItems.append(i)
	
for i in sortedItems:
	print("Item: " + str(i.top))
	cv2.rectangle(screenshot, (i.left, i.top), (i.left + i.width, i.top + i.height), (0, 255, 255))

cv2.imshow("Screenshot", screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows()