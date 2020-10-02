import cv2
import numpy as np
import time

cap=cv2.VideoCapture(0)
time.sleep(1)
count=0
bg=0
for i in range(60):
    ret,bg=cap.read()
    if ret==False:
        continue
bg=np.flip(bg,axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    count=count+1
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_end=np.array([94,80,20])
    upper_end=np.array([126,255,255])
    mask1=cv2.inRange(hsv,lower_end,upper_end)
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),
                                 iterations=2)
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    mask2=cv2.bitwise_not(mask1)
    res1=cv2.bitwise_and(bg,bg,mask=mask1)
    res2=cv2.bitwise_and(img,img,mask=mask2)
    final_output=cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('INVISIBLE MAN',final_output)
    k=cv2.waitKey(10)
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()

    