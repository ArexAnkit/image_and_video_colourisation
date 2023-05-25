# importing the packages
import numpy as np
import cv2

#--------------------------------Part1: Pre-processing-----------------------------------------#

#Step1-Loading our pre-trained model
print("Pre-Trained Model Loading")
net = cv2.dnn.readNetFromCaffe('model/colorization_deploy_v2.prototxt', 'model/colorization_release_v2.caffemodel')
pts = np.load('model/pts_in_hull.npy')

#Step2-Load centers for ab channel quantization used for rebalancing(cluster centers as 1*1 convoltions)
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

#Step3
image = cv2.imread('images/mark_twain.jpg') #take grayscale input image
scaled = image.astype("float32") / 255.0 #scaling in range[0,1]
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB) #RGB to LAB color space

#Step4
resized = cv2.resize(lab, (224, 224)) #resize it to the required input dimensions for our network
L = cv2.split(resized)[0] #take the channel L
L -= 50 #mean subtraction

#Step5
print("Passing Input L channel into the network to pridict AB channel")
net.setInput(cv2.dnn.blobFromImage(L)) #passing L input into the network
ab = net.forward()[0, :, :, :].transpose((1, 2, 0)) #forward it  and extract the predicted ab value

#Step6
ab = cv2.resize(ab, (image.shape[1], image.shape[0])) #resize as our input image

#--------------------------------Part2: Post-processing-----------------------------------------#

#Step1
L = cv2.split(lab)[0] #take the L channel value
colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2) #concatenate with ab to form a colorized output image

#Step2
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR) #LAB-->RGB color space
colorized = np.clip(colorized, 0, 1)  #remove that fall outside the range[0,1]

#Step3
colorized = (255 * colorized).astype("uint8") #brining back the pixel intensity back to the range[0,255]

#Step4
cv2.imshow("Input Image", image)
cv2.imshow("Output Image", colorized)
cv2.waitKey(0)

print("Task Done")
