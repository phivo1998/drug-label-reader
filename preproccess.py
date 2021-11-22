import glob
import cv2
import numpy as np
import time
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def read_img(img_list, img):
    n = cv2.imread(img, 0)
    img_list.append(n)
    return img_list



path = glob.glob("*.jpg")
#path = glob.glob("pfi_20210224_AV-UK-033-20_0_0_B3Zbe6apcMK.jpg")
list_ = []

cv_image = [read_img(list_, img) for img in path]

for i in range(5):#len(list_)):
    image = list_[i]


    thresh1 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
    thresh2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

    cv2.imshow('Adaptive Mean', thresh1)
    cv2.imshow('Adaptive Gaussian', thresh2)

    
    text = pytesseract.image_to_string(thresh2)

    print(text)

    print("##############################################")
    cv2.waitKey(0)