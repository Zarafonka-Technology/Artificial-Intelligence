import cv2
print(cv2.__version__)
dispW=1280
dispH=960
flip=2
cam=cv2.VideoCapture(0)
while True:
    ret, frame=cam.read()
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('piCam2',gray)
    cv2.moveWindow('piCam2',500,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()