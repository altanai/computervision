import cv2

# importing numpy
import numpy as np

image=cv2.imread('ramudroidimg.jpg')
cv2.imshow('hello_world', image)
#s hape function returns a tuple from img array which gives a dimension of an image
print(image.shape)

print('Height of image:',(image.shape[0],'pixels'))
print('Width of image:',(image.shape[1],'pixels'))

cv2.waitKey()
cv2.destroyAllWindows()

# savig an edited image
# cv2.imwrite('output.jpg',image)
# cv2.imwrite('output.png',image)