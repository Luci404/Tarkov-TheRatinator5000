import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

img_cv = cv2.imread("screenshot.png")
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
img_text = pytesseract.image_to_string(img_rgb, config="--psm 7 --oem 0")

with open("pytesseract-result.txt", "w") as f:
    f.write(img_text)