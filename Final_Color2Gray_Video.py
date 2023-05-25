#Part1-import packages
import imutils
from imutils.video import VideoStream
import cupy as np
import time
import cv2

#Part2-To check...is it webcam or video file
print("Enter 0 for Webcam ")
print("Enter 1 for Video File ")
x=int(input())
if x==1:
        webcam=False
elif x==0:
        webcam=True
        
print("Enter 'E' for Exit ")

#Part3-if webcam
if webcam:
	print("Webcam vedio's information loading")
	vs = VideoStream(src=0).start()
	time.sleep(2.0)
	W=640

#Part4- else vedio
else:
	print("Vedio file's informations loading")
	vs = cv2.VideoCapture('images\pexels-free-videos-854141-1920x1080-25fps.mp4')
	W=int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))


#Part5-loop to get the frames from video
	
while True:
 print("Running")
 #take the next frame from the video
 frame = vs.read()
 frame = frame if webcam else frame[1]

 # end it if it is last frame
 if not webcam and frame is None:
      break

 frame = imutils.resize(frame, width=W) #resize

 #output image method1
 output_img1=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

 #show the output
 cv2.imshow("Input Video", frame)
 cv2.imshow("Output Video", output_img1)
 key = cv2.waitKey(1) & 0xFF

 # press E to exit
 if key == ord("E"):
      break

#Part6-stop webcam
if webcam:
	vs.stop()
#Part7-stop vedio file
else:
	vs.release()

#Part8-close windows
cv2.destroyAllWindows()
