# colored images are 3 D while gray scale images are 2D
# reduces noise
# faster processing

import cv2

# load our input image
image=cv2.imread('ramudroid2.jpg')
# cv2.imshow('original', image)
cv2.waitKey()

#we use cvtcolor, to convert to greyscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', gray_image)
cv2.waitKey()
cv2.destroyALLWindows()