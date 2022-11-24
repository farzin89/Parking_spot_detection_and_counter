
import cv2
from util import get_parking_spots_bboxes
mask = 'mask_crop.png'
video_path = 'parking_crop_loop.mp4'

mask = cv2.imread(mask,0)
cap =cv2.VideoCapture(video_path)

# get the location of parking spots(use mask to find location of parking spot)
connected_components = cv2.connectedComponentsWithStats(mask, 4, cv2.CV_32S)
spots =get_parking_spots_bboxes(connected_components)

ret = True
while True :
    ret,frame = cap.read()

    # plot how the bbox is look like
    for spot in spots:
        x1,y1,w,h = spot
        frame=cv2.rectangle(frame,(x1,y1),(x1 + w,y1 + h),(255,0,0),2)


    cv2.imshow('frame',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()