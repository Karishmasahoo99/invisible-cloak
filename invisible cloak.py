import cv2
import numpy as np
cap=cv2.VideoCapture(0)
background=0
#for capturing the background image
for i in range(30):
    ret,background=cap.read()
background=np.flip(background,axis=1)
#cv2.imshow("backgrnd",background)

while(cap.isOpened()):
    ret,img=cap.read()
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #range for blue color
    lower_blue=np.array([94,80,20])
    upper_blue=np.array([126,255,255])
    mask1=cv2.inRange(hsv, lower_blue, upper_blue)
    #cv2.imshow("mask1",mask1)
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
    #cv2.imshow("mask1",mask1)
    mask2=cv2.bitwise_not(mask1)
    #cv2.imshow("mask2",mask2)
    #getting the cloth out
    res1=cv2.bitwise_and(img,img,mask=mask2)
    #cv2.imshow("res1",res1)
    res2=cv2.bitwise_and(background, background,mask=mask1)
    final_output=cv2.addWeighted(res1, 1, res2,1,0)
    cv2.imshow("magic",final_output)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    