import cv2 as cv
import numpy as np
import os
import array as ar

def main():

    cap = cv.VideoCapture(0)

    ret, frame = cap.read()


    img = cv.imread("b2.jpg", 0)
    img2 = cv.imread("B1.jpg", 0)

    default = cv.imread("default_size.png", 0)

    H,W = default.shape[:2]

    #print("H: ", H, "W: ", W)

    imRe1 = cv.resize(img, default.shape[:2])
    imRe2 = cv.resize(img2, default.shape[:2])


    #ret, threshold = cv.threshold(imRe1, 220, 255, 0)
    #_, contours, hierachy = cv.findContours(threshold, 3, cv.CHAIN_APPROX_SIMPLE)

    threshold = cv.inRange(imRe1, 0, 254)



    ret2, threshold2 = cv.threshold(imRe2, 220, 255, 0)
    _2, contours2, hierachy2 = cv.findContours(threshold2, 3, cv.CHAIN_APPROX_SIMPLE)

    #ret3, threshold3 = cv.threshold(imgray, 220, 255, 0)
    #_3, contours3, hierachy3 = cv.findContours(threshold3, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #final3 = cv.drawContours(imgray, contours3, 0, (0, 255, 0), 2)

    #print(contours)
    #cnt = contours[4]

    #final = cv.drawContours(imRe1, contours, 0, (0, 255, 0), 2)
    final2 = cv.drawContours(imRe2, contours2, 0, (0, 255, 0), 2)


    hist1 = cv.calcHist([threshold], [0], None, [256], [0,256])
    hist2 = cv.calcHist([threshold2], [0], None, [256], [0,256])

    count = 1

    i = 0

    verts = [i] * 30

    pic = str('frame')
    jp = str('.jpg')
    index = 1

    print(verts[2])
    while count < 30:
        _, webcam = cap.read()  # _ is a return value we do not care about and therefore did not name properly

        kernel = np.ones((5, 5), np.float32) / 25  # mean blur kernel
        smoothed = cv.filter2D(webcam, -1, kernel)  # apply kernel to the webcam-feed

        # convert RGB to HSV to be able to use intensity and saturation
        hsv = cv.cvtColor(smoothed, cv.COLOR_BGR2HSV)

        # defining the colour range in HSV (H's range is 0-180(360/2), while S and V is scaled to 0-255)
        lower_colour = np.array([79, 100, 64])  # Lowest HSV-colour value detected
        upper_colour = np.array([96, 255, 175])  # Highest HSV-colour value detected

        # Threshold the HSV coloured and smoothed webcam feed to only let colours between our upper and lower range through
        mask = cv.inRange(hsv, lower_colour, upper_colour)

        verts[i in range(28)] = cv.imwrite("frame%d.jpg" % count, mask)

        verts[1] = 0

        count += 1
        i += 1
        imgframes = cv.imread(pic + str(i) + jp, 0)

        imRe3 = cv.resize(imgframes, default.shape[:2])

        ret3, threshold3 = cv.threshold(imRe3, 220, 255, 0)
        _3, contours3, hierachy3 = cv.findContours(threshold3, 3, cv.CHAIN_APPROX_SIMPLE)


        cv.imshow("Webcam", webcam)  # Show webcam-feed
        cv.imshow("Mask", mask)  # Show the mask

        hist3 = cv.calcHist(mask, [0], None, [256], [0, 256])
        #final3 = cv.drawContours(imRe3, contours3, 0, (0, 255, 0), 2)

        com = cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)
        print('retrival', com)

        if cv.waitKey(20) & 0xFF == ord('q'):  # Press 'q' to close the windows
            break
    #cap.waitKey(0)
    #cap.destroyAllWindows()




    cv.imshow("thresh", threshold)
    #cv.imshow("thresh2", threshold2)
    #cv.imshow("mask", mask)
    #cv.imshow('frames', threshold3)

    #cv.imshow("threshold3", threshold3)

    i = 0

    if com == 100:

        count = 31

    elif count == 30:

        for c in range(30):
            # print('111hej med dig duu derrrrrrr', verts.index(str(i)))

            i += 1

            #print(i)

            if os.path.exists(pic + str(i) + jp):
                os.remove(pic + str(i) + jp)
                # list.remove(verts.index(pic+str(i)+jp))
                cv.waitKey(2)
                main()


    cv.waitKey(0)

    #while cap.isOpened():
    #    if com > 0.90:
    #        print("Hist3 is Hist1")
    #        break
    #    else:
    #        print("No Match")
    #        cv.waitKey(0)
    #        break
    #hist3 = cv.calcHist([img3], [0], None, [256], [0,256])

    """
    params = cv.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.filterByColor = True
    
    detector = cv.SimpleBlobDetector_create(params)
    spot_keypoints = detector.detect(img)
    i = cv.drawKeypoints(img, spot_keypoints, outImage=np.array([]), color=(0,0,255), flags=0)
    """
    #cv.imshow("2", final2)
    #cv.imshow("threshold", threshold)
    #cv.imshow("Contour", final)
    #cv.imshow("thresh", threshold)
    cv.waitKey(0)

if  __name__ == '__main__':
    main()