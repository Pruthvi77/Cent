import cv2
import numpy as np
print("Yayy!!!!!!!!!! OpenCV & Numpy has Importeddd")


def getContors(img):
   contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       #to get all shapes from canny image
   for cnt in contours:
       area = cv2.contourArea(cnt)
           #to get the area of each shape
       print(area)
       if area>500:    #all shapes greater than 50 pixels
           cv2.drawContours(shapes, cnt, -1, (255, 0, 0), 1)
               # to get a blue line on each shape
           peri = cv2.arcLength(cnt, True)
           #print(peri)
           approx=  cv2.approxPolyDP(cnt,0.02*peri, True)
               #this will give all corner points of each shape
           print(len(approx))
           objCor = len(approx)
           x, y, w, h = cv2.boundingRect(approx)
           if objCor == 3: objectType = "Tri"
           elif objCor ==4:
               aspectRatio = w/float(h)
               if aspectRatio > 0.95 and aspectRatio < 1.05:  objectType="Square"
               else:objectType="Rectangle"
           elif objCor == 5:
               objectType = "pentagon"
           elif objCor == 6:
               objectType = "Hexagon"
           elif objCor > 7:
               objectType = "amay be circle"
           else: objectType="None"
           cv2.rectangle(shapes,(x,y),(x+w,y+h), (255,198,25),2)
           cv2.putText(shapes, objectType, (x+(w//2)-10, y +(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,178,0),1)
               #to find the triangle in image


#loading an image
img = cv2.imread('C:/Users/prudvi/PycharmProjects/OWN/Resources/Julia_Ann.jpg')
juli = cv2.imread('C:/Users/prudvi/PycharmProjects/OWN/Resources/Juliii.jpg')
car = cv2.imread('C:/Users/prudvi/PycharmProjects/OWN/Resources/baleno.jpg')
#define kernel

kernel = np.ones((5,5), np.uint8)
#make image gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#make image blur
imgBlurr = cv2.GaussianBlur(imgGray,(7,7),0)
#find boundaries and shapes
imgCanny = cv2.Canny(img,100,100)
#make the borders thicker
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1 )
#make the borders thinner
imgroadded = cv2.erode(imgDilation, kernel , iterations=1)
imgText = cv2.putText(img, "what a circles", (150,500), cv2.FONT_HERSHEY_COMPLEX, 2, (98,0,46),2)
   #to write text on image
   # cv2.putText(img, "what a circles", (150,500), cv2.FONT_HERSHEY_COMPLEX, size of text , (98,0,46),thickness of text)



cv2.imshow("OutPut",img)
cv2.waitKey(1000)
cv2.imshow("OutPut",imgGray)
cv2.waitKey(1000)
cv2.imshow("OutPut",imgBlurr)
cv2.waitKey(1000)
cv2.imshow("OutPut",imgCanny)
cv2.waitKey(1000)
cv2.imshow("OutPut",imgDilation)
cv2.waitKey(1000)
cv2.imshow("OutPut",imgroadded)
cv2.waitKey(1000)


#print the size of image
print(img.shape)
#to resize the image
imgResize = cv2.resize(img, (1000,500))
imgCrop = img[300:500, 150:450]

cv2.imshow("OutPut",imgResize)
cv2.waitKey(1000)
cv2.imshow("OutPut",imgCrop)
cv2.waitKey(1000)




cap = cv2.VideoCapture('C:/Users/prudvi/PycharmProjects/OWN/Resources/12094568_10153987994069578_547661877_n.mp4')
#while True:
   #success, image = cap.read()
   #cv2.imshow('video', image)
   #if cv2.waitKey(1) & 0xFF ==ord('q'):
    #   break

cv2.imshow("OutPut",imgText)
cv2.waitKey(1000)


image2 = np.zeros((512,512,3),np.uint8)
image2[:]=255,23,197
   #to colour RGB for an
   # ':' means it will range whole image

cv2.imshow("Image", image2)
cv2.waitKey(1000)

image2[200:300, 250:350]=255,0,0
   #to colour only a part of image using array index
cv2.imshow("Image", image2)
cv2.waitKey(1000)

cv2.line(image2,(0,0), (300,1556), (7,8,6),3)
   # (image2, (x1.y1), (x2,y2), (R,G,B), thickness)
cv2.imshow("Image", image2)
cv2.waitKey(1000)
cv2.line(image2,(0,0), (image2.shape[1],image2.shape[0]), (7,8,6),3)
   # image2.shape will give the shape of it, to draw a dull diagonal line
cv2.imshow("Image", image2)
cv2.waitKey(1000)

cv2.rectangle(image2,(1,1), (100,122), (96,56,163), cv2.FILLED)
   #to fill rectangle with a colour
cv2.imshow("Image", image2)
cv2.waitKey(1000)

cv2.circle(image2, (300,250),30, (255,255,0),5)
   #to draw a circle
cv2.imshow("Image", image2)
cv2.waitKey(1000)

width,height=120,120
points1 = np.float32([[112,430],[120,590],[260,449],[271,612]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(points1,points2)
imgOut =  cv2.warpPerspective(img,matrix,(width,height))
   #to take 4 points on image and make it proper as cam scanner document scanning
cv2.imshow("Image", imgOut)
cv2.waitKey(1000)


imgHorizonta = np.hstack((img,img))
cv2.imshow("Commbination", imgHorizonta)
   #to view 2 images side by side
cv2.waitKey(1000)
   #to view two images vertically
   #both images should have same size & RGB
imgVertical = np.vstack((img,img))
cv2.imshow("Combination", imgVertical)
cv2.waitKey(1000)

imgHSV = cv2.cvtColor(car,cv2.COLOR_BGR2HSV)
cv2.imshow("Combination", imgHSV)
cv2.waitKey(1000)



def empty(a):
   pass


cv2.namedWindow("Trackbars")
   #to creates a window with name 'Trackbars'
cv2.resizeWindow("Trackbars", 640,220)
   #to give a sixe to the window created above
cv2.createTrackbar("Hue Min","Trackbars",91,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",60,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",106,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)

   #to create a track bar inside window which ranges from 0-179

count = 0
while (count < 1000):
   car = cv2.imread('C:/Users/prudvi/PycharmProjects/OWN/Resources/baleno.jpg')
   imgHSV = cv2.cvtColor(car,cv2.COLOR_BGR2HSV)
   hue_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
   hue_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
   sat_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
   sat_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
   val_min = cv2.getTrackbarPos("Val Min", "Trackbars")
   val_max = cv2.getTrackbarPos("Val Max", "Trackbars")
   print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)
   lower = np.array([hue_min,sat_min, val_min])
   max = np.array([hue_max, sat_max, val_max])
   mask = cv2.inRange(imgHSV, lower, max)
   imgResult = cv2.bitwise_and(car,car,mask=mask)
       #to get the colour image
   cv2.imshow("Original", img)
   cv2.imshow("Combination", imgHSV)
   cv2.imshow("Combination", imgResult)
   cv2.imshow("Mask", mask)
   cv2.waitKey(1)
   count = count + 1
   print(count)
   if count == 999:
       break


def getContors(img):
   contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       #to get all shapes from canny image
   for cnt in contours:
       area = cv2.contourArea(cnt)
           #to get the area of each shape
       print(area)
       if area>500:    #all shapes greater than 50 pixels
           cv2.drawContours(shapes, cnt, -1, (255, 0, 0), 1)
               # to get a blue line on each shape
           peri = cv2.arcLength(cnt, True)
           #print(peri)
           approx=  cv2.approxPolyDP(cnt,0.02*peri, True)
               #this will give all corner points of each shape
           print(len(approx))
           objCor = len(approx)
           x, y, w, h = cv2.boundingRect(approx)
           if objCor == 3: objectType = "Tri"
           elif objCor ==4:
               aspectRatio = w/float(h)
               if aspectRatio > 0.95 and aspectRatio < 1.05:  objectType="Square"
               else:objectType="Rectangle"
           elif objCor == 5:
               objectType = "pentagon"
           elif objCor == 6:
               objectType = "Hexagon"
           elif objCor > 7:
               objectType = "amay be circle"
           else: objectType="None"
           cv2.rectangle(shapes,(x,y),(x+w,y+h), (255,198,25),2)
           cv2.putText(shapes, objectType, (x+(w//2)-10, y +(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,255,178,0),1)
               #to find the triangle in image

############# to detect number plate ####################

framewidth = 640
frameheight = 480
plateCascade = cv2.CascadeClassifier("C:/Users/prudvi/PycharmProjects/OWN/Resources/russianplate.xml")
color = (255,0,255)
   #what colour should number plate should highlight with
cap = cv2.VideoCapture(0)
   #0 to capture webcam video
cap.set(3, framewidth)
cap.set(3, frameheight)
cap.set(10,130)

while True:
   success, img = cap.read()
   carGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
   nplates = plateCascade.detectMultiScale(carGray,1.1,4)

   for (x,y,w,h) in nplates:
       cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),1)
       cv2.putText(img, "Number_Plate" , (x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,color,2)
       imgCrop = img[y:y+h, x:x+w]
           #to crop number plate pixels
       cv2.imshow("CarPlate", imgCrop)

   cv2.imshow("Cam", img)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break



shapes = cv2.imread('C:/Users/prudvi/PycharmProjects/OWN/Resources/shapes.jpg')
shapeGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
shapeBlur = cv2.GaussianBlur(shapeGray, (7,7), 1)
cv2.imshow("Combination", shapes)
cv2.waitKey(1000)
cv2.imshow("Combination", shapeGray)
cv2.waitKey(1000)
cv2.imshow("Combination", shapeBlur)
cv2.waitKey(1000)
imageCanny2 =  cv2.Canny(shapeBlur, 50 ,5)
   #to get the edges
cv2.imshow("Canny", imageCanny2)
cv2.waitKey(1000)

getContors(imageCanny2)
cv2.imshow("Combination", shapes)
   #it will show images with shapes with blue line on it
cv2.waitKey(10000)

facecascade = cv2.CascadeClassifier("C:/Users/prudvi/PycharmProjects/OWN/Resources/doontknow.xml")
julia = cv2.imread('C:/Users/prudvi/PycharmProjects/OWN/Resources/Julia_Ann.jpg')
juliaGray = cv2.cvtColor(julia,cv2.COLOR_BGR2GRAY)
faces = facecascade.detectMultiScale(juliaGray,1.1,4)

for (x,y,w,h) in faces:
   cv2.rectangle(julia, (x,y),(x+w,y+h),(255,0,0),1)

cv2.imshow("Face",julia)
cv2.waitKey(1000)




framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)
   #0 to capture webcam video
cap.set(3, framewidth)
cap.set(3, frameheight)
cap.set(10,130)
   #set brightness

myColors = [[5,92,72,90,16,255],
           [133,56,130,159,225,255],
           [26,76,13,100,225,255]]
   #this is the filer like trackbars above

myColorValues = [[51,153,255],
               [255,0,255],
               [0,255,0]]



def getContors(img):
   contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
       #to get all shapes from canny image
   for cnt in contours:
       area = cv2.contourArea(cnt)
           #to get the area of each shape
       print(area)
       if area>500:    #all shapes greater than 50 pixels
           cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 1)
               # to get a blue line on each shape
           peri = cv2.arcLength(cnt, True)
           #print(peri)
           approx=  cv2.approxPolyDP(cnt,0.02*peri, True)
               #this will give all corner points of each shape
           print(len(approx))
           objCor = len(approx)
           x, y, w, h = cv2.boundingRect(approx)

def findColor(img,myColors):
   imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
   count = 0
       #to get HSV image
   for colors in myColors:
       lower = np.array(colors[0:3])
       max = np.array(colors[3:6])
       mask = cv2.inRange(imgHSV, lower, max)
       getContors(mask)
       #cv2.imshow("img", mask)

count = 0
while (count < 1000):
   success, img = cap.read()
   imgResult = img.copy()
   findColor(img, myColors)
       #calling above function
   cv2.imshow("Cam", imgResult)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   count = count + 1
   print(count)
   if count == 999:
       break
