# HSV (Hue, Saturation & value/ Brightness)
# hue color value ranges from 0 – 180
# Saturation – Vibrancy of color (0-255)
# Value – Brightness or intensity (0-255)

import cv2
image=cv2.imread('ramudroidimg.jpg')

hsv_image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image',hsv_image)

cv2.imshow('Hue channel',hsv_image[:,:,0])

cv2.imshow('saturation channel',hsv_image[:,:,1])

cv2.imshow('value channel',hsv_image[:,:,2])

cv2.waitKey()
cv2.destroyAllWindows()