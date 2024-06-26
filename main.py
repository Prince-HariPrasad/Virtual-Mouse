import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

pyautogui.FAILSAFE = False 

wCam, hCam = 640, 480
frameR=100 #frameReduction
smoothening = 7

plocX,plocY=0,0
clocX,clocY=0,0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime=0
detector = htm.handDetector(maxHands=1)
wScr,hScr=pyautogui.size()

# print(wScr,hScr)

while True:
    # 1) Find HandLandmarks
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break
    if img is None or img.size == 0:
        print("Captured image is empty")
        break
    img= detector.findHands(img)
    lmList,bbox=detector.findPosition(img)
    # 2) Get the tip of index and middle fingers
    if len(lmList)!=0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        # 3) Check which fingers are up
        fingers=detector.fingersUp()
        # 4) Only Index finger : moving mode
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR,hCam-frameR),(255,0,255),2)
        if fingers[1]==1 and fingers[2]==0:
            # 5) convert  Coordinates
            x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1,(frameR,hCam-frameR),(0,hScr))
            # 6) Smoothen the values
            clocX=plocX+(x3-plocX)/smoothening
            clocY=plocY+(y3-plocY)/smoothening

            # 7) Move Mouse
            pyautogui.moveTo(clocX, clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX,plocY=clocX,clocY
        # 8) Both index and Middle fingers are up : Clicking Mode
        if fingers[1]==1 and fingers[2]==1:
            # 9) Find distance between fingers
            length, img, lineInfo = detector.findDistance(8,12,img)
            # 10) Click mouse if distance is short
            print(length)
            if(length<40):
                cv2.circle(img,(lineInfo[4],lineInfo[5]),15,(0,255,0),cv2.FILLED)
                pyautogui.click()
        
       

    # 11) Frame rate
    cTime=time.time()
    fps = 1 / (cTime - pTime)
    pTime =cTime
    cv2.putText(img, str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)

    # 12) Display
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


