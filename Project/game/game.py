import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap=cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# imges improt
backgroundImg=cv2.imread("Resources/Background.png")
gameoverImg=cv2.imread("Resources/gameover.png")
player1Img=cv2.imread("Resources/bat1.png",cv2.IMREAD_UNCHANGED)
player2Img=cv2.imread("Resources/bat2.png",cv2.IMREAD_UNCHANGED)
ballImg=cv2.imread("Resources/Ball.png",cv2.IMREAD_UNCHANGED)

detector = HandDetector(detectionCon=0.8, maxHands=2)

# Variables
ballPos = [100, 100]
speedX = 25
speedY = 25
gameOver = False
score = [0, 0]

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    imgRaw = img.copy()
    hands,img=detector.findHands(img,flipType=False)
    img = cv2.addWeighted(img, 0.2, backgroundImg, 0.8, 0)
    
    if hands:
        for hand in hands:
            x,y,w,h=hand['bbox']
            h1,w1,_=ballImg.shape
            y1=y-h//2
            y1=np.clip(y1,20,415)

            if hand['type']=="Left":
                img=cvzone.overlayPNG(img,player1Img,(59,y1))
                if 59 < ballPos[0] < 59 + w1 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] += 30
                    score[0] += 1
            
            if hand['type']=="Right":
                img=cvzone.overlayPNG(img,player2Img,(1195,y1))
                if 1195 - 50 < ballPos[0] < 1195 and y1 < ballPos[1] < y1 + h1:
                    speedX = -speedX
                    ballPos[0] -= 30
                    score[1] += 1
    # Game Over
    if ballPos[0] < 40 or ballPos[0] > 1200:
        gameOver = True

    if gameOver:
        img = gameoverImg
        cv2.putText(img, str(score[1] + score[0]).zfill(2), (585, 360), cv2.ACCESS_FAST,2.5, (200, 0, 200), 5)

    # If game not over move the ball
    else:
         # Move the Ball
        if ballPos[1] >= 500 or ballPos[1] <= 10:
            speedY = -speedY

        ballPos[0] += speedX
        ballPos[1] += speedY
        # overlap ball
        img =cvzone.overlayPNG(img,ballImg,ballPos)
        cv2.putText(img, str(score[0]), (300, 650), cv2.ACCESS_FAST, 3, (255, 255, 255), 5)
        cv2.putText(img, str(score[1]), (900, 650), cv2.ACCESS_FAST, 3, (255, 255, 255), 5)

    cv2.imshow("Image",img)
    key=cv2.waitKey(1)
    if key == ord('r'):
        ballPos = [100, 100]
        speedX = 15
        speedY = 15
        gameOver = False
        score = [0, 0]
        imgGameOver = cv2.imread("Resources/gameoverImg.png")