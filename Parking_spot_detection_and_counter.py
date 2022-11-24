
import cv2


video_path = 'carPark.mp4'

cap =cv2.VideoCapture(video_path)
ret = True
while True :
    ret,frame = cap.read()


    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()