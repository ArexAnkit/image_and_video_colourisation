#Part1-import packages
from imutils.video import VideoStream
import numpy as np
import imutils
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

#Part4- else video
else:
	print("Video file's informations loading")
	vs = cv2.VideoCapture('images\pexels-free-videos-854141-1920x1080-25fps.mp4')
	W=int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))

#Part5-load the model
print("Loading model's informations")
net = cv2.dnn.readNetFromCaffe('model/colorization_deploy_v2.prototxt', 'model/colorization_release_v2.caffemodel')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
pts = np.load('model/pts_in_hull.npy')

#Part6-add the cluster centers 
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

#Part7-loop to get the frames from video 
while True:
	#take the next frame from the video
	frame = vs.read()
	frame = frame if webcam else frame[1]

	# end it if it is last frame
	if not webcam and frame is None:
		break

	frame = imutils.resize(frame, width=W) #resize
	scaled = frame.astype("float32") / 255.0 # scale it [0,1]
	lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB) #convert the frame from the BGR to Lab

	resized = cv2.resize(lab, (224, 224))# resize
	L = cv2.split(resized)[0] #split channels
	L -= 50 #extract the 'L' 

	#  channel through the network which will  channel values
	net.setInput(cv2.dnn.blobFromImage(L)) #pass the L
	ab = net.forward()[0, :, :, :].transpose((1, 2, 0)) #predict ab

	ab = cv2.resize(ab, (frame.shape[1], frame.shape[0])) #resize
	L = cv2.split(lab)[0] #grab the 'L'
	colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2) #concatenate L and ab

	colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
	colorized = np.clip(colorized, 0, 1) #clip
	colorized = (255 * colorized).astype("uint8") #again convert it

	#show the output
	cv2.imshow("Input Video", frame)
	cv2.imshow("Grayscale Video", cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
	cv2.imshow("Output Video", colorized)
	key = cv2.waitKey(50) & 0xFF

	# press E to exit
	if key == ord("E"):
		break

#Part8-stop webcam
if webcam:
	vs.stop()
#Part9-stop vedio file
else:
	vs.release()

#Part10-close windows
cv2.destroyAllWindows()
