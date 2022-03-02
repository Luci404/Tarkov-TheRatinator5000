import cv2 as cv
import numpy as np

screenshot_rgb = cv.imread("screenshot.png")
screenshot_gray = cv.cvtColor(screenshot_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread("icons/14c2ef8c-d6b3-459c-b59f-39722a064981.png", 0)
width, height = template.shape[::-1]

resolution = cv.matchTemplate(screenshot_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.8
location = np.where(resolution >= threshold)
for point in zip(*location[::-1]):
    cv.rectangle(screenshot_rgb, point, (point[0] + width, point[1] + height), (0, 0, 255), 2)

cv.imwrite("result.png", screenshot_rgb)