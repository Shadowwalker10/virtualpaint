import cv2
import numpy as np

cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)


def empty(a):
    pass
#Max value of hue is 360 but in opencv it is till 179
cv2.createTrackbar("Hue Min","TrackBar",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBar",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBar",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBar",255,255,empty)
cv2.createTrackbar("Value Min","TrackBar",0,255,empty)
cv2.createTrackbar("Value Max","TrackBar",255,255,empty)

#Reading from webcam
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
cap.set(10,150)

while True:
    
    success,img = cap.read()
    img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBar")
    v_min = cv2.getTrackbarPos("Value Min","TrackBar")
    v_max = cv2.getTrackbarPos("Value Max","TrackBar")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(img_hsv,lower,upper)
    
    imgResult = cv2.bitwise_and(img,img,mask = mask)
    
    

    #Defining the hue,saturation and value limits for detection and grab
    #As we are not aware about which value is optimal, we introduce trackbar

    cv2.imshow("Original Image",img)
    cv2.imshow("HSV Image",img_hsv)
    cv2.imshow("Mask",mask)
    cv2.imshow("Final Result",imgResult)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

myColors = {"orange":[5,107,0,19,255,255],"purple":[133,56,0,159,156,255],
            "green":[57,76,0,100,255,255]}




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