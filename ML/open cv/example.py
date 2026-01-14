import cv2
# cv2 is computer vision

img = cv2.imread("X:\\Python\\ML\\open cv\\res\\5.1.jpg")
# reading and image , the path specified is in double backslash because single is used for excape sequence

cv2.imshow("DODGE",img)
cv2.waitKey(1000)

#capture a video or webcam
vid = cv2.VideoCapture(1, cv2.CAP_DSHOW)

for i in range(5):
    vid = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    print(f"camera {i}",vid.isOpened())
    vid.release()


vid.set(3,640)   #width function number is 3
vid.set(4,480)   # height function number is 4
vid.set(10,100)   #brightness is 10

# to ruun the webcam or video we use while loop
while True:
    success , img2 = vid.read()

    if not success:
        print("No camera")
        break

    cv2.imshow("Cam",img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

