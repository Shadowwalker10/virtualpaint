import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
cap.set(10,130)#For brightness


#These are the colors that we want to detect
myColors = {"orange":[5,107,0,19,255,255],"purple":[133,56,0,159,156,255],
            "green":[57,76,0,100,255,255]}

color_values = {"orange":[51,153,255],"purple":[255,0,255],
                "green":[0,255,0]}

myPoints = [] #can be [[x,y,color]]
    
def findContours(image):
    contour, hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #if the contour is not detected
    x,y,w,h = 0,0,0,0
    
    for cnt in contour:
        area = cv2.contourArea(cnt)
        
        if area>500:
            #cv2.drawContours(imgresult,cnt,-1,(255,0,0),2)
            
            peri = cv2.arcLength(cnt,closed = True)
            approx = cv2.approxPolyDP(cnt,epsilon = 0.03*peri,closed = True)
            
            x,y,w,h = cv2.boundingRect(approx)
            
    return x+w//2,y#we returned complete y because we need a structure like the tip of a pen
        
    
    

    
def findColor(image,color_dict):
    imghsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
    newPoints = []
    for key, value in color_dict.items():
        color = color_values[key]
            
        lower = np.array(value[0:3])
        upper = np.array(value[3:])
        
        mask = cv2.inRange(imghsv,lower,upper)
        x,y = findContours(mask)
        cv2.circle(imgresult,(x,y),10,color,cv2.FILLED)
        
        if x!=0 and y!=0:
            newPoints.append([x,y,color])
        
        #cv2.imshow(key,mask)
        
        #detecting the contours of the object and approximate the bounding box
        
    return newPoints


def drawOnCanvas(myPoints):
    for point in myPoints:
        cv2.circle(imgresult,(point[0],point[1]),10,point[2],cv2.FILLED)




while True:
    success,frame = cap.read()
    frame = cv2.flip(frame,1)
    imgresult = frame.copy()
    new_points = findColor(frame,myColors)
    if len(new_points)!=0:
        for new in new_points:
            myPoints.append(new)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints)
    cv2.imshow("Webcam",imgresult)
    
    
    
    
    
    
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()