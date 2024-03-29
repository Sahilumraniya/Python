import cv2
import mediapipe as mp

mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw=mp.solutions.drawing_utils

video=cv2.VideoCapture(0)

video.set(3, 1280)
video.set(4, 720)


img_1 = cv2.imread('magic_circles/magic_circle_ccw.png', -1)
img_2 = cv2.imread('magic_circles/magic_circle_cw.png', -1)

deg=0

def position_data(lmlist):
    global wrist, thumb_tip, index_mcp, index_tip, midle_mcp, midle_tip, ring_tip, pinky_tip
    wrist = (lmlist[0][0], lmlist[0][1])
    thumb_tip = (lmlist[4][0], lmlist[4][1])
    index_mcp = (lmlist[5][0], lmlist[5][1])
    index_tip = (lmlist[8][0], lmlist[8][1])
    midle_mcp = (lmlist[9][0], lmlist[9][1])
    midle_tip = (lmlist[12][0], lmlist[12][1])
    ring_tip  = (lmlist[16][0], lmlist[16][1])
    pinky_tip = (lmlist[20][0], lmlist[20][1])


def calculate_distance(p1,p2):
    x1, y1, x2, y2 = p1[0], p1[1], p2[0], p2[1]
    lenght = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1.0 / 2)
    return lenght


def transparent(targetImg, x, y, size=None):
    if size is not None:
        targetImg = cv2.resize(targetImg, size)

    newFrame = img.copy()
    b, g, r, a = cv2.split(targetImg)
    overlay_color = cv2.merge((b, g, r))
    mask = cv2.medianBlur(a, 1)
    h, w, _ = overlay_color.shape
    roi = newFrame[y:y + h, x:x + w]

    img1_bg = cv2.bitwise_and(roi.copy(), roi.copy(), mask=cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, overlay_color, mask=mask)
    newFrame[y:y + h, x:x + w] = cv2.add(img1_bg, img2_fg)

    return newFrame
 

while True:
    _,img=video.read()
    img=cv2.flip(img, 1)
    rgbimg=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result=hands.process(rgbimg)
    cv2.putText(img, "Q for exit", (15, 50), cv2.FONT_HERSHEY_PLAIN,2, (255, 0, 0), 2)
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:
            lmList=[]
            for id, lm in enumerate(hand.landmark):
                h,w,c=img.shape
                coorx, coory=int(lm.x*w), int(lm.y*h)
                lmList.append([coorx, coory])
            position_data(lmList)
            palm = calculate_distance(wrist, index_mcp)
            distance = calculate_distance(index_tip, pinky_tip)
            ratio = distance / palm
            if (ratio >0.5):
                    centerx = midle_mcp[0]
                    centery = midle_mcp[1]
                    shield_size = 3.0
                    diameter = round(palm * shield_size)
                    x1 = round(centerx - (diameter / 2))
                    y1 = round(centery - (diameter / 2))
                    h, w, _ = img.shape
                    if x1 < 0:
                        x1 = 0
                    elif x1 > w:
                        x1 = w
                    if y1 < 0:
                        y1 = 0
                    elif y1 > h:
                        y1 = h
                    if x1 + diameter > w:
                        diameter = w - x1
                    if y1 + diameter > h:
                        diameter = h - y1
                    shield_size = diameter, diameter
                    ang_vel = 2.5
                    deg = deg + ang_vel
                    if deg > 360:
                        deg = 0
                    h, w,_ = img_1.shape
                    center = (w // 2, h // 2)
                    M1 = cv2.getRotationMatrix2D(center, round(deg),1)
                    M2 = cv2.getRotationMatrix2D(center, round(360 - deg),1)
                    rotated1 = cv2.warpAffine(img_1, M1, (w+2, h+10))
                    rotated2 = cv2.warpAffine(img_2, M2, (w+2, h+10))
                    if (diameter != 0):
                        img = transparent(rotated1, x1, y1, shield_size)
                        img = transparent(rotated2, x1, y1, shield_size)

    cv2.imshow("Image",img)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

video.release()
cv2.destroyAllWindows()