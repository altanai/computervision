import cv2
import numpy as np

# creating a black square
image = np.zeros((512,512,3),np.uint8)

# black and white
# image_bw = np.zeros((512,512),np.uint8)
# cv2.imshow("black rectangle(color)",image)
# cv2.imshow("black rectangle(B&W)",image_bw)

# create a line over black square
# cv2.line(image, starting coordinates, ending coordinates, color, thickness)
# drawing a diagonal line of thickness 5 pixels
cv2.line(image,(0,0),(511,511),(255,127,0),5)
cv2.imshow("blue line",image)


#create a rectangle over a black square
#cv2.rectangle(image,starting coordinates, ending coordinates, color, thickness)
#drawing a rectangle of thickness 5 pixels
# image=np.zeros((512,512,3),np.uint8)
cv2.rectangle(image,(30,50),(100,150),(255,127,0),5)
cv2.imshow("rectangle",image)

# stop gap measure to prevent program from exiting
# input('Press ENTER to exit')

cv2.waitKey()
cv2.destroyALLWindows()