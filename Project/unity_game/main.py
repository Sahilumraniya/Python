import cv2
from cvzone.HandTrackingModule import HandDetector
import socket

cam=cv2.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)
success, img = cam.read()
h,w,_=img.shape

detector=HandDetector(maxHands=2,detectionCon=0.8)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    success,img=cam.read()
    hands,img=detector.findHands(img)
    data=[]
    if hands:
        hand=hands[0]
        lmList=hand["lmList"]
        for l in lmList:
            data.extend([l[0],h-l[1],l[2]])
        sock.sendto(str.encode(str(data)), serverAddressPort)
    print(data)
    cv2.imshow("Image",img)
    cv2.waitKey(1)