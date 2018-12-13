import cv2

img1 = cv2.imread('1.png',0)
img2 = cv2.imread('2.png',0)
img3 = cv2.imread('3.png',0)
img4 = cv2.imread('4.png',0)
img5 = cv2.imread('5.png',0)
img12 = cv2.imread('12.png', 0)
img13 = cv2.imread('13.png', 0)
img14 = cv2.imread('14.png', 0)
img15 = cv2.imread('15.png', 0)
img2Right = cv2.imread('2_Right.png', 0)
img2Left = cv2.imread('2_Left.png', 0)
img3Right = cv2.imread('3_Right.png', 0)
img3Left = cv2.imread('3_Left.png', 0)
img4Right = cv2.imread('4_Right.png', 0)
img4Left = cv2.imread('4_Left.png', 0)
img5Right = cv2.imread('5_Right.png', 0)
img5Left = cv2.imread('5_Left.png', 0)



# mean blurring
def mask(image):
    image=cv2.resize(image,(200,200))
    #440, 440
    return image

