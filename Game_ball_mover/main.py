import cvzone
import cv2
from cvzone.ColorModule import ColorFinder
import socket

camera=cv2.VideoCapture(0)
# set the width
camera.set(3,1280)
# set the height of window
camera.set(4,720)

#  for datm a transfer
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverAddressPort=("127.0.0.1",5052)

        # debug mode if you are finding the color then make it True , else if you have already the color then make if
# false.
myColorFinder=ColorFinder(False) #True


# this is the dictionary ,in which there are different color modules and different parameters -> by which we can idnetify the proper color.
hsvVals = {'hmin': 16, 'smin': 124, 'vmin': 130, 'hmax': 36, 'smax': 255, 'vmax': 255}

while True:
    ret,frame=camera.read()
    h,w=frame.shape[:2]

    frame=cv2.flip(frame,1)
    # .update() is provides the colored image and mask
    imgColor,mask= myColorFinder.update(frame,hsvVals)
    # where to find and which color-> specify in hsvVals
    # findcontours -> gives the image contour and also the values itself
    # by default minArea is 1000, anything below 1000 is ignored, some noise or green object here and there, if large objects then write 5000,otherwise 1000 no need to write.
    imgContour,contours=cvzone.findContours(frame,mask)

    if contours: # here, contours is a list of contours.
        data = contours[0]['center'][0],h-contours[0]['center'][1],int(contours[0]['area'])
              #x coord value of center|  #y coord of center of that contour || #coz area in float
        print(data)
        data=str.encode(str(data))
        sock.sendto(data,serverAddressPort)

    # to show multiple images/frames
    # imgStack=cvzone.stackImages([frame,imgColor,mask,imgContour],2,0.5)
    # cv2.imshow("frame",frame)
    # cv2.imshow("colored image",imgColor)
    # cv2.imshow("imagestack",imgStack)

    imgContour=cv2.resize(imgContour,(0,0),None,0.3,0.3)
    cv2.imshow("imgContour",imgContour)
    key=cv2.waitKey(1)

    if key==ord('m'):
        break

camera.release()
cv2.destroyAllWindows()


# steps:
# 1.after setting up the basic code
# 2.Find color which you want to detect.(cvzone has color and contour module both.
# (from color finder take any default value of 'hsvVals' and with the .update() method find the proper values for the 'hsvVals'-> by taking different iteration.

# 3.now based upon mask draw the rectangle on choosen hsvVals object/contour by 'findContours()'
# (findContours method returns the contours in frame drawn and its values. So take the values of the x,y coordinates of center and area)
# problem: cv2 convention in y axis upper- 0 and go down value increase, so set reverse for that minus y coordinate from the height which we are setted earlier.

# 4.now create the socket and make the connnection for data transfer from pycharm to unity or let's say python to c sharp