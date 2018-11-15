import cv2
import numpy as np


img1 = cv2.imread('1.png',0)
img2 = cv2.imread('2.png',0)
img3 = cv2.imread('3.png',0)
img4 = cv2.imread('4.png',0)
img5 = cv2.imread('5.png',0)

# mean blurring
def mask(image):
    image=cv2.resize(image,(440,440))

    return image


'''cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



#cv2.imshow('Color Detect', img)
#cv2.imshow('Detection', mask)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
