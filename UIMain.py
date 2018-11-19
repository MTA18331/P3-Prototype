import pygame
import cv2
import numpy as np
import time
import threading
import image_threshold as imgThre
from queue import Queue

camera = cv2.VideoCapture(0)    # 0 for webcam
display_width = 1080
display_height = 720
white = (255, 255, 255)
black = (0, 0, 0)

q = Queue()

mainScreen = pygame.image.load('UI_Images/mainscreen.png')
mainHelp = pygame.image.load('UI_Images/mainHelp.png')
cameraScreen = pygame.image.load("UI_Images/camscreen.png")
camHelp = pygame.image.load("UI_Images/camHelp.png")
camEx1 = pygame.image.load("UI_Images/camEx1.png")
camEx2 = pygame.image.load("UI_Images/camEx2.png")
camEx3 = pygame.image.load("UI_Images/camEx3.png")
camEx4 = pygame.image.load("UI_Images/camEx4.png")
camEx5 = pygame.image.load("UI_Images/camEx5.png")
camSearch = pygame.image.load("UI_Images/camSearch.png")
mainQuit = pygame.image.load("UI_Images/mainQuit.png")
camMenu = pygame.image.load("UI_Images/camMenu.png")
one = pygame.image.load("UI_Images/Number1.png")
two = pygame.image.load("UI_Images/Number2.png")
three = pygame.image.load("UI_Images/Number3.png")
four = pygame.image.load("UI_Images/Number4.png")
five = pygame.image.load("UI_Images/Number5.png")
p0 = pygame.image.load("UI_Images/00.png")
p1 = pygame.image.load("UI_Images/10.png")
p2 = pygame.image.load("UI_Images/20.png")
p3 = pygame.image.load("UI_Images/30.png")
p4 = pygame.image.load("UI_Images/40.png")
p5 = pygame.image.load("UI_Images/50.png")
p6 = pygame.image.load("UI_Images/60.png")
p7 = pygame.image.load("UI_Images/70.png")
p8 = pygame.image.load("UI_Images/80.png")
p9 = pygame.image.load("UI_Images/90.png")
p10 = pygame.image.load("UI_Images/100.png")
flueben = pygame.image.load("UI_Images/flueben.png")

mainScreen = pygame.transform.scale(mainScreen, (display_width, display_height))
mainHelp = pygame.transform.scale(mainHelp, (display_width, display_height))
cameraScreen = pygame.transform.scale(cameraScreen, (display_width, display_height))
camHelp = pygame.transform.scale(camHelp, (display_width, display_height))
camEx1 = pygame.transform.scale(camEx1, (display_width, display_height))
camEx2 = pygame.transform.scale(camEx2, (display_width, display_height))
camEx3 = pygame.transform.scale(camEx3, (display_width, display_height))
camEx4 = pygame.transform.scale(camEx4, (display_width, display_height))
camEx5 = pygame.transform.scale(camEx5, (display_width, display_height))
camSearch = pygame.transform.scale(camSearch, (display_width, display_height))
mainQuit = pygame.transform.scale(mainQuit, (display_width, display_height))
camMenu = pygame.transform.scale(camMenu, (150, display_height))
p0 = pygame.transform.scale(p0, (200, 200))
p1 = pygame.transform.scale(p1, (200, 200))
p2 = pygame.transform.scale(p2, (200, 200))
p3 = pygame.transform.scale(p3, (200, 200))
p4 = pygame.transform.scale(p4, (200, 200))
p5 = pygame.transform.scale(p5, (200, 200))
p6 = pygame.transform.scale(p6, (200, 200))
p7 = pygame.transform.scale(p7, (200, 200))
p8 = pygame.transform.scale(p8, (200, 200))
p9 = pygame.transform.scale(p9, (200, 200))
p10 = pygame.transform.scale(p10, (200, 200))
one = pygame.transform.scale(one, (90, 110))
two = pygame.transform.scale(two, (90, 110))
three = pygame.transform.scale(three, (90, 110))
four = pygame.transform.scale(four, (90, 110))
five = pygame.transform.scale(five, (90, 110))

pygame.init()

gameDisplay = pygame.display.set_mode((display_width, display_height))#, pygame.FULLSCREEN)
pygame.display.set_caption('Danske Tegn Bank')

clock = pygame.time.Clock()
pygame.display.update()
clock.tick(60)  # frames per second
start = time.time()
startTime = True
input_box = pygame.Rect(display_width/2-285, display_height/2+130, 520, 42)
input_box_popup = pygame.Rect(display_width/2-295, display_height/2-25, 445, 42)
#roi_box = pygame.Rect(86, 91, 500, 500)
roi_box = pygame.Rect(193, 91, 550, 550)
font = pygame.font.Font(None, 32)


def imageProcessing(nr, start):

        #print(frame)
        #frame = cv2.flip(frame, +1)
        ret, frame = camera.read()
        frame = cv2.flip(frame, +1)
        if nr == 1:
            mask =  imgThre.mask(imgThre.img1)
        elif nr == 2:
            mask =  imgThre.mask(imgThre.img2)
        elif nr == 3:
            mask = imgThre.mask(imgThre.img3)
        elif nr==4:
            mask =  imgThre.mask(imgThre.img4)
        elif nr == 5:
            mask = imgThre.mask(imgThre.img5)

        template = mask
        w, h = template.shape[::-1]



        #ret, frame = camera.read()
        #frame = cv2.flip(frame, +1)

        kernel = np.ones((10, 10), np.float32) / 100
        smoothed = cv2.filter2D(frame, -1, kernel)

        hsv = cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV)

        lower_red = np.array([80, 140, 35])  # [90, 100, 150]) grøn handske
        upper_red = np.array([97, 255, 175])

        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        roi = mask2[60:500, 60:500]
        res = cv2.matchTemplate(roi, mask, cv2.TM_CCOEFF_NORMED)
        minval, maxval, minlog, maxlog= cv2.minMaxLoc(res)
        res = maxval

        #print(minval, minlog, maxlog)
        cv2.imshow("roi",roi)
        cv2.imshow("mask", mask)
        print(res)
        q.put(res)
        #print("res ", res)
          # draws the box
        #send res to main thread

            #if timer >= 5:
             #   print('Yay, res is: ', res)
              #  cv2.rectangle(frame, (300,70), (600,100), (50,50,50), -1)
               # cv2.putText(frame, "YOu be good", (310, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))


def runprogressbar(input):

    if input == 0:
        gameDisplay.blit(p0, (35, 400))
    elif input <= 0.3:
        gameDisplay.blit(p1, (35, 400))
    elif input <= 0.6:
        gameDisplay.blit(p2, (35, 400))
    elif input <= 1:
        gameDisplay.blit(p3, (35, 400))
    elif input <= 1.3:
        gameDisplay.blit(p4, (35, 400))
    elif input <= 1.6:
        gameDisplay.blit(p5, (35, 400))
    elif input <= 2:
        gameDisplay.blit(p6, (35, 400))
    elif input <= 2.3:
        gameDisplay.blit(p7, (35, 400))
    elif input <= 2.6:
        gameDisplay.blit(p8, (35, 400))
    elif input <= 3:
        gameDisplay.blit(p9, (35, 400))
    elif input <= 3.3:
        gameDisplay.blit(p10, (35, 400))
    elif input >= 3.4:
        gameDisplay.blit(p10, (35, 400))
        gameDisplay.blit(flueben,(56,443))


def game_loop():
    game_exit = False
    mScreen = True
    runCam = False
    cScreen = False
    popUp = False
    popUpSearch = False
    mainHelpPopUp = False
    mainClose = False
    nr = 0
    active = True
    text = ''
    global startTime
    startTime = True

    gameDisplay.blit(mainScreen, (0, 0))



    while not game_exit:

        if runCam:

            ret, frame = camera.read()
            gameDisplay.fill([243, 243, 243])
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = np.rot90(frame)
            t = threading.Thread(target=imageProcessing(nr, start), name='thread2', args=(nr,frame))
            frame = pygame.surfarray.make_surface(frame)
            frame = pygame.transform.scale(frame, (920, 720))
            gameDisplay.blit(camMenu, (920, 0))
            gameDisplay.blit(frame, (0, 0))
            pygame.draw.rect(gameDisplay, [0,255,0], roi_box, 2) # ROI green rect
            t.start()
            if nr == 1:
                gameDisplay.blit(one, (810, 25))  # draws the input on the camerascreen
            if nr == 2:
                gameDisplay.blit(two, (810, 25))  # draws the input on the camerascreen
            if nr == 3:
                gameDisplay.blit(three, (810, 25))  # draws the input on the camerascreen
            if nr == 4:
                gameDisplay.blit(four, (810, 25))  # draws the input on the camerascreen
            if nr == 5:
                gameDisplay.blit(five, (810, 25))  # draws the input on the camerascreen
            res= q.get()
            #if res >= 0 and res <= 0.10:
            if res >= 0.65 and res < 0.99:

                runprogressbar(time.time() - start)
            else:
                start=time.time()
            pygame.display.update()
            try:
                t.start()
            except:
                1+1
            #lavimageprocessing() in another thread
            ################

        if mScreen:  # if the main screen is active it builds the input box
            popUpSearch = False
            txt_surface = font.render(text, True, black)  # configures how text should look

            gameDisplay.blit(txt_surface, (input_box.x + 5, input_box.y + 5))  # draws the text

            pygame.draw.rect(gameDisplay, white, input_box, 2)  # draws the box
        if cScreen:
            if nr == 1:
                gameDisplay.blit(one, (810, 25))  # draws the number on the camera screen
            if nr == 2:
                gameDisplay.blit(two, (810, 25))
            if nr == 3:
                gameDisplay.blit(three, (810, 25))
            if nr == 4:
                gameDisplay.blit(four, (810, 25))
            if nr == 5:
                gameDisplay.blit(five, (810, 25))

        if popUpSearch:
            mScreen = False
            txt_surface = font.render(text, True, black)  # configures how text should look

            gameDisplay.blit(txt_surface, (input_box_popup.x + 5, input_box_popup.y + 5))  # draws the text

            pygame.draw.rect(gameDisplay, white, input_box_popup, 2)  # draws the text

        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # happens when you press the x in the top right corner
                pygame.quit()
                cv2.destroyAllWindows()
                quit()

            if event.type == pygame.KEYDOWN:  # how we handle a keyboard input
                if active:  # the inputbox is active
                    if text == "Ingen resultater\r":  # if the box contains ingen resultater when a keyboard button is clicked
                        gameDisplay.fill(white)  # clears the screen
                        if mScreen:
                            gameDisplay.blit(mainScreen, (0, 0)) # draws the main screen again
                        if popUpSearch:
                            gameDisplay.blit(cameraScreen, (0, 0))
                            gameDisplay.blit(camSearch, (0, 0))
                        text = ""  # set the text to nothing

                    text += event.unicode  # adds the keyboard input to text
                    if event.key == pygame.K_BACKSPACE:
                        gameDisplay.fill(white)
                        text = text[:-2]  # deletes two inputs when pressing backspace
                        if mScreen:
                            gameDisplay.blit(mainScreen, (0, 0))
                        if popUpSearch:
                            gameDisplay.blit(cameraScreen, (0, 0))
                            gameDisplay.blit(camSearch, (0, 0))
                    if event.key == pygame.K_RETURN:

                        try:
                            print(int(text))

                            if int(text) == 1 or int(text) == 2 or int(text) == 3 or int(text) == 4 or int(text) == 5:
                                print("hej")
                                cScreen = True
                                active = False
                                mScreen = False
                                popUpSearch = False

                                gameDisplay.blit(cameraScreen, (0, 0))  # draw the camera screen
                                if (int(text)) == 1:

                                    nr = 1
                                elif (int(text)) == 2:

                                    nr = 2
                                elif (int(text)) == 3:
                                    nr = 3
                                elif (int(text)) == 4:
                                    nr = 4
                                elif (int(text)) == 5:
                                    nr = 5
                            else:
                                gameDisplay.fill(white)
                                if mScreen:
                                   gameDisplay.blit(mainScreen, (0, 0))
                                if popUpSearch:
                                   gameDisplay.blit(cameraScreen, (0, 0))
                                   gameDisplay.blit(camSearch, (0, 0))
                                text = "Ingen resultater\r"
                        except ValueError:
                            gameDisplay.fill(white)
                            if mScreen:
                                gameDisplay.blit(mainScreen, (0, 0))
                            if popUpSearch:
                                gameDisplay.blit(cameraScreen, (0, 0))
                                gameDisplay.blit(camSearch, (0, 0))
                            text = "Ingen resultater\r"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:

                    if input_box.collidepoint(event.pos):  # if the mouse is inside the input box, activate it

                        active = True

                    x, y = pygame.mouse.get_pos()  # pygame.mouse.get_pos() returns a touple (x,y)
                    print(pygame.mouse.get_pos())
                    if mScreen:  # listen to mouse events related to the main screen

                        if x > 775 and x < 820 and y > 485 and y < 530:  # mouse is on the search button

                            try:
                                if int(text) == 1 or int(text) == 2 or int(text) == 3 or int(text) == 4 or int(text) == 5:

                                    cScreen = True
                                    active = False
                                    mScreen = False
                                    popUpSearch = False
                                    gameDisplay.blit(cameraScreen, (0, 0))  # draw the camera screen if the input is 1
                                    if (int(text)) == 1:
                                        nr = 1

                                    elif (int(text)) == 2:
                                        nr = 2
                                    elif (int(text)) == 3:
                                        nr = 3
                                    elif (int(text)) == 4:
                                        nr = 4
                                    elif (int(text)) == 5:
                                        nr = 5
                                else:
                                    gameDisplay.fill(white)
                                    if mScreen:
                                        gameDisplay.blit(mainScreen, (0, 0))
                                    if popUpSearch:
                                        gameDisplay.blit(cameraScreen, (0, 0))
                                        gameDisplay.blit(camSearch, (0, 0))
                                    text = "Ingen resultater\r"

                            except ValueError:
                                gameDisplay.fill(
                                    white)  # if enter is pressed and the input is not 1, writes ingen resultater in the box
                                if mScreen:
                                    gameDisplay.blit(mainScreen, (0, 0))
                                if popUpSearch:
                                    gameDisplay.blit(camSearch, (0, 0))
                                text = "Ingen resultater\r"
                                active = True

                        if x > 1045 and x < 1065 and y > 15 and y < 35:  # mouse is within the exit button
                            mScreen = False
                            mainClose = True
                            gameDisplay.blit(mainQuit, (0, 0))  # draw the main help screen defined above

                        if x > 1025 and x < 1065 and y > 660 and y < 720:  # mouse is within the exit button
                            gameDisplay.blit(mainHelp, (0, 0))  # draw the main help screen defined above

                            mainHelpPopUp = True
                            mScreen = False

                    if mainHelpPopUp and x > 790 and x < 810 and y > 190 and y < 220:  # mouse is within exit button in the help popup on the main page
                        gameDisplay.blit(mainScreen, (0, 0))  # draw the main help screen defined above

                        mainHelpPopUp = False
                        mScreen = True

                    if cScreen:  # listen to mouse events related to the camera screen
                        runCam = False
                        gameDisplay.blit(cameraScreen, (0, 0))
                        cv2.destroyAllWindows()

                        if x > 925 and x < 1080 and y > 0 and y < 175:  # mouse is within the home button
                            gameDisplay.blit(mainScreen, (0, 0))  # draw the main screen defined above
                            cScreen = False
                            text = ""
                            active = True
                            mScreen = True

                        if x > 925 and x < 1080 and y > 176 and y < 350:  # mouse is within the example button
                            if nr == 1:
                                gameDisplay.blit(camEx1, (0, 0))
                            if nr == 2:
                                gameDisplay.blit(camEx2, (0, 0))
                            if nr == 3:
                                gameDisplay.blit(camEx3, (0, 0))
                            if nr == 4:
                                gameDisplay.blit(camEx4, (0, 0))
                            if nr == 5:
                                gameDisplay.blit(camEx5, (0, 0))
                            cScreen = False
                            popUp = True

                        if x > 925 and x < 1080 and y > 351 and y < 525:  # mouse is within the search button
                            gameDisplay.blit(camSearch, (0, 0))
                            cScreen = False
                            popUpSearch = True
                            active = True
                            text = ""

                        if x > 925 and x < 1080 and y > 526 and y < 700:  # mouse is within the help button
                            gameDisplay.blit(camHelp, (0, 0))
                            cScreen = False
                            popUp = True

                        if x > 165 and x < 760 and y > 210 and y < 510:  # mouse is within the activate camera button
                            runCam = True
                            start = time.time()

                    if popUp or popUpSearch:
                        if x > 735 and x < 775 and y > 160 and y < 190:  # mouse is within the exit button in a pop up
                            gameDisplay.blit(cameraScreen, (0, 0))
                            popUpSearch = False
                            text = ""
                            popUp = False
                            cScreen = True

                    if popUpSearch:
                        if x > 700 and x < 750 and y > 300 and y < 380:  # mouse is within the serach button in the search pop up
                            try:
                                if int(text) == 1 or int(text) == 2 or int(text) == 3 or int(text) == 4 or int(text) == 5:
                                    cScreen = True
                                    active = False
                                    mScreen = False
                                    popUpSearch = False
                                    gameDisplay.blit(cameraScreen, (0, 0))  # draw the camera screen if the input is 1
                                    if (int(text)) == 1:
                                        nr = 1
                                    elif (int(text)) == 2:
                                        nr = 2
                                    elif (int(text)) == 3:
                                        nr = 3
                                    elif (int(text)) == 4:
                                        nr = 4
                                    elif (int(text)) == 5:
                                        nr = 5
                                else:
                                    gameDisplay.fill(white)
                                    if mScreen:
                                        gameDisplay.blit(mainScreen, (0, 0))
                                    if popUpSearch:
                                        gameDisplay.blit(cameraScreen, (0, 0))
                                        gameDisplay.blit(camSearch, (0, 0))
                                    text = "Ingen resultater\r"

                            except ValueError:
                                gameDisplay.fill(white)
                                if mScreen:
                                    gameDisplay.blit(mainScreen, (0, 0))
                                if popUpSearch:
                                    gameDisplay.blit(cameraScreen, (0, 0))
                                    gameDisplay.blit(camSearch, (0, 0))
                                text = "Ingen resultater\r"
                                active = True

                    if mainClose:
                        if x > 300 and x < 500 and y > 450 and y < 512:  # mouse is within the no button in the search pop up
                            mainClose = False
                            mScreen = True
                            gameDisplay.blit(mainScreen, (0, 0))
                        if x > 585 and x < 790 and y > 450 and y < 512:  # mouse is within the quit button in the search pop up
                            pygame.quit()
                            quit()
        pygame.display.update()
        clock.tick(60)  # frames per second


game_loop()
