import cv2

#imput image
input_img=cv2.imread('images/mark_twain.jpg')
cv2.imshow('Input Image',input_img)
cv2.waitKey(0)

#output image method1
output_img1=cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('images/mark_twain.jpg',output_img1)
cv2.imshow('Output Image',output_img1)
cv2.waitKey(0)

#output method 2
input_img=cv2.imread('images/mark_twain.jpg',0)
cv2.imshow('Output Image method2',input_img)
cv2.imwrite('images/mark_twain.jpg',input_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
