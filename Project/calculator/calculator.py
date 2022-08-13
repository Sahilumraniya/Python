from sre_constants import SUCCESS
import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self,pos,width,height,value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self,img):
        if self.value=='+' or self.value=='-' or self.value=='*' or self.value=='/' or self.value=='=':
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),(242,194,2), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),(0,0,0), 3)
            cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), cv2.FONT_HERSHEY_PLAIN,2, (50, 50, 50), 2)
        else:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),(49, 49,49), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),(0,0,0), 3)
            cv2.putText(img, self.value, (self.pos[0] + 30, self.pos[1] + 70), cv2.FONT_HERSHEY_PLAIN,2, (255,255,255), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and \
                self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3),
                          (self.pos[0] + self.width - 3, self.pos[1] + self.height - 3),
                          (255, 255, 255), cv2.FILLED)
            cv2.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv2.FONT_HERSHEY_PLAIN,
                        5, (255, 255, 255), 5)
            return True
        else:
            return False

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.5, maxHands=1)

myEquation = ''
dayer = 0

# Buttons
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '.', '/', '=']]
buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x * 100 + 600
        ypos = y * 100 + 85
 
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x]))

while True:
    _, img=cap.read()
    img=cv2.flip(img,1)
    hands , img=detector.findHands(img)

    cv2.rectangle(img, (600, 10), (600 + 400, 10 + 100),(143,188,143), cv2.FILLED)
    cv2.rectangle(img, (600, 10), (600 + 400, 10 + 100),(51, 50, 50), 3)

    for button in buttonList:
        button.draw(img)

    if hands:
        # Find distance between fingers
        lm = hands[0]['lmList']
        length,info,img = detector.findDistance(lm[8][:2], lm[12][:2], img)
        x,y=lm[8][:2]

        if length < 45 and dayer == 0:
                for i, button in enumerate(buttonList):
                    if button.checkClick(x, y):
                        myValue=buttonListValues[int(i%4)][int(i/4)]
                        if myValue == '=':
                            if myEquation[len(myEquation)-2]=='/' and myEquation[len(myEquation)-1]=='0':
                                myEquation = "undefine"
                            else:
                                myEquation = str(eval(myEquation))
                        else:
                            myEquation += myValue
                    dayer = 1
    if dayer != 0:
        dayer += 1
        if dayer > 10:
            dayer = 0
 
    # Write the Final answer
    cv2.putText(img, myEquation, (610, 60), cv2.FONT_HERSHEY_PLAIN,3, (0, 0, 0), 3)
    cv2.putText(img, "c for clear screen", (15, 50), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 2)
    cv2.putText(img, "r for clear last digit", (15, 75), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 2)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord('c'):
        myEquation = ''
    if key == ord('r'):
        myEquation = myEquation[:len(myEquation)-1]