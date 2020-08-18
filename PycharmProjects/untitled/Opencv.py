import cv2
print("imported")

imageRead = cv2.imread("C:/Users/prudvi/Pictures/CUSTOMISED-MARUTI-BALENO-PETES-1-1068x679.jpg.jpg")

cv2.imshow("Output",imageRead)
cv2.waitKey(2000)

video = cv2.VideoCapture("C:/Users/prudvi/Desktop/Movies/Othr_shit/757557_500382123357122_91463262_n.mp4")

while True :
    success, img = video.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break


video = cv2.VideoCapture(0)
video.set(3,640)
video.set(10,100)

while False :
    success, img = video.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break
