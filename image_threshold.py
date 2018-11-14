import cv2
import numpy as np


img = cv2.imread('thump3s.jpg',0)

# mean blurring
kernel = np.ones((10, 10), np.float32) / 100
smoothed = cv2.filter2D(img, -1, kernel)

#hsv = cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV)

#lower_red = np.array([80, 140, 35])    #[90, 100, 150]) grøn handske
#pper_red = np.array([97, 255, 175])

mask = cv2.inRange(smoothed, 0, 254)

'''cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



#cv2.imshow('Color Detect', img)
#cv2.imshow('Detection', mask)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
