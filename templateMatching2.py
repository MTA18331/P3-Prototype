import cv2
import numpy as np
import image_threshold as imgThre
import time

def webcam(frame):
    #cap = cv2.VideoCapture(0)
    startTime = True

    template = imgThre.mask
    w, h = template.shape[::-1]

    while (True):
        #ret, frame = cap.read()
        #frame = cv2.flip(frame, +1)

        kernel = np.ones((10, 10), np.float32) / 100
        smoothed = cv2.filter2D(frame, -1, kernel)

        hsv = cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV)

        lower_red = np.array([80, 140, 35])  # [90, 100, 150]) grøn handske
        upper_red = np.array([97, 255, 175])

        mask = cv2.inRange(hsv, lower_red, upper_red)

        roi = mask[70:270, 50:250]
        res = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
        res = float(res)
        #print("res ", res)

        if res >= 0.65:
            if startTime == True:
                start=time.time()
                startTime = False

            timer = time.time() -start
            print(int(timer))
            if timer >= 5:
                print('Yay, res is: ', res)
                cv2.rectangle(frame, (300,70), (600,100), (50,50,50), -1)
                cv2.putText(frame, "YOu be good", (310, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
        else:
            startTime = True


        cv2.rectangle(frame, (50, 70), (250, 270), (0, 255, 0), 3)

        #cv2.imshow('thump', template)
        #cv2.imshow('Frame', frame)
        #cv2.imshow('mask', roi)

        #key = cv2.waitKey(1)

        #if key == 27:
         #   break

    #cap.release()
    #cv2.destroyAllWindows()