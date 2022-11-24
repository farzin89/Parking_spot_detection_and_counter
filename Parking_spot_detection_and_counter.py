
import cv2

mask = 'mask_crop.png'
video_path = 'carpark_F9PvBt0D.mp4'

mask = cv2.imread(mask,0)
cap =cv2.VideoCapture(video_path)
ret = True
while True :
    ret,frame = cap.read()


    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()