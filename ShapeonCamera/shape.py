import cv2
print(cv2.__version__)
dispW=640
dispH=480
flip=2
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    ret,frame=cam.read()
    frame=cv2.rectangle(frame,(340,100),(100,300),(0,0,255),-1)
    frame=cv2.circle(frame,(340,240),50,(0,255,0),5)
    fnt=cv2.FONT_HERSHEY_DUPLEX
    frame=cv2.putText(frame,'MY FIRST TEXT',(240,320),fnt,1.5,(255,0,150),6)
    frame=cv2.line(frame,(10,10),(630,470),(0,0,0),4)
    frame=cv2.arrowedLine(frame,(10,470),(630,10),(0,255,255),1)
    cv2.imshow('piCam',frame)
    cv2.moveWindow('piCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()