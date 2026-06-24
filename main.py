import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import time
import random

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(maxHands=1)

timer = 0
stateResults = False
StartGame = False
initialTime = 0
imgAI = None
scores =[0,0] #[AI,Player]

while True:
    imgBG = cv2.imread("Resources/BG.png")
    imgBG = cv2.resize(imgBG, (1280, 720))

    success, img = cap.read()

    imgScaled = cv2.resize(img, (0, 0), None, 0.875, 0.875)
    imgScaled = imgScaled[:, 80:480]

    # Find Hands
    hands, imgScaled = detector.findHands(imgScaled)

    if StartGame:

        if stateResults is False:
            timer = time.time() - initialTime

            cv2.putText(imgBG, str(int(timer)), (605, 435), cv2.FONT_HERSHEY_PLAIN, 6, (255, 0, 255), 4)

            if timer >= 3:
                stateResults = True
                timer = 0

                if hands:
                    playerMove = None
                    hand = hands[0]
                    fingers = detector.fingersUp(hand)

                    if fingers == [0, 0, 0, 0, 0]:
                        playerMove = 1      # Rock

                    if fingers == [1, 1, 1, 1, 1]:
                        playerMove = 2      # Paper

                    if fingers == [0, 1, 1, 0, 0]:
                        playerMove = 3      # Scissors

                    randomNumber = random.randint(1, 3)

                    imgAI = cv2.imread(
                        f"Resources/{randomNumber}.png",
                        cv2.IMREAD_UNCHANGED
                    )
                    imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))



                    # Player wins
                    if (playerMove == 1 and randomNumber ==3)or\
                        (playerMove == 2 and randomNumber ==1)or\
                         (playerMove == 3 and randomNumber ==2):
                         scores[1] +=1

                    #AI wins
                    elif (playerMove == 3 and randomNumber ==1)or\
                        (playerMove == 1 and randomNumber ==2)or\
                         (playerMove == 2 and randomNumber ==3):
                         scores[0] +=1
                      
                    print(playerMove)

    imgBG[233:653, 795:1195] = imgScaled

    if stateResults and imgAI is not None:
        imgBG = cvzone.overlayPNG(imgBG, imgAI, (149, 310))

    cv2.putText(imgBG, str(int(scores[0])), (410, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)    
    cv2.putText(imgBG, str(int(scores[1])), (1112, 215), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 6)


    cv2.imshow("Image", imgBG)

    key = cv2.waitKey(1)

    if key == ord('s'):
        StartGame = True
        initialTime = time.time()
        stateResults = False