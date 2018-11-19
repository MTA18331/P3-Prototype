import cv2

img1 = cv2.imread('1.png',0)
img2 = cv2.imread('2.png',0)
img3 = cv2.imread('3.png',0)
img4 = cv2.imread('4.png',0)
img5 = cv2.imread('5.png',0)

# mean blurring
def mask(image):
    image=cv2.resize(image,(440,440))

    return image




