import cv2
import numpy as np
import pyautogui as pg
from scipy.spatial import distance
import typing

CONFIG_DUPLICATE_DISTANCE_CUTOFF: float = 25.0

class ItemInfo:
	_iconPath: str
	_confidence: float

	def __init__(self, itemPath, confidence = 0.8) -> None:
		self._itemPath = itemPath
		self._confidence = confidence

	def GetIconPath(self) -> str:
		return self._itemPath

	def GetConfidence(self) -> float:
		return self._confidence

class ScanResult:
	_count: int

	def __init__(self, count):
		self._count = count
		
	def GetCount(self) -> int:
		return self._count
	

def Scan(itemInfo: ItemInfo) -> ScanResult:
	screenshot = pg.screenshot()
	screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

	sortedItems = []
	for i in pg.locateAllOnScreen(itemInfo.GetIconPath(), confidence=itemInfo.GetConfidence()):
		alreadyContains = False
		for sortedItem in sortedItems:
			dist = distance.euclidean((float(i.top), float(i.left)), (float(sortedItem.top), float(sortedItem.left)))
			if (dist <= CONFIG_DUPLICATE_DISTANCE_CUTOFF):
				alreadyContains = True

		if not alreadyContains:
			sortedItems.append(i)
	
	for i in sortedItems:
		print("Item: " + str(i.top))
		cv2.rectangle(screenshot, (i.left, i.top), (i.left + i.width, i.top + i.height), (0, 255, 0))

	cv2.imshow("Screenshot", screenshot)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	return ScanResult(len(sortedItems))

testItem: ItemInfo = ItemInfo("icon01.png")
scanInfo: ScanResult = Scan(testItem)