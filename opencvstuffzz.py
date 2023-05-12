import cv2 as cv
from cv2 import rectangle
import numpy as np
import json

screenshot_rgb = cv.imread("screenshot.png")
screenshot_gray = cv.cvtColor(screenshot_rgb, cv.COLOR_BGR2GRAY)

templates = []
"""
with open("data.json", 'r') as file:
    data = file.read()
obj = json.loads(data)

scanItemInfos = []
for item in obj:
	templates.append(cv.imread("icons/" + item["uid"] + ".png", 0))
"""

templates = [
    cv.imread("icons/14c2ef8c-d6b3-459c-b59f-39722a064981.png", 0), # Metal parts
    cv.imread("icons/5b9f9704-4d6d-4c4b-b627-2dc4e8cbff52.png", 0) # PCB
]

cnt = 0
for t in templates:
    cnt = cnt + 1
    template_width, template_height = t.shape[::-1]
    print(cnt)
    resolution = cv.matchTemplate(screenshot_gray, t, cv.TM_CCOEFF_NORMED)
    threshold = 0.46
    locations = np.where(resolution >= threshold)
    locations = list(zip(*locations[::-1]))
    
    # [x, y, w, h]
    rectangles = []
    for location in locations:
        rectangles.append([int(location[0]), int(location[1]), template_width, template_height])

    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.5) 

    for point in rectangles:
        cv.rectangle(screenshot_rgb, (point[0], point[1]), (point[0] + point[2], point[1] + point[3]), (0, 0, 255), 2)

#cv.imwrite("result.png", screenshot_rgb)
cv.imshow("Result", screenshot_rgb)
cv.waitKey()
# https://www.youtube.com/watch?v=ffRYijPR8pk&list=PL1m2M8LQlzfKtkKq2lK5xko4X-8EZzFPI&index=2