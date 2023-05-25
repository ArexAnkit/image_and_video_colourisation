import cv2
print("GPU available:", cv2.cuda.getCudaEnabledDeviceCount() > 0)
