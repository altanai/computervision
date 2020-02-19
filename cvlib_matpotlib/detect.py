
# Install libs opencv-python , cvlib , matplotlib and tensorflow beforehand

import cv2
import matplotlib.pyplot as plt
import cvlib as cv

from cvlib.object_detection import draw_bbox
im = cv2.imread('apple-256261_640.jpg')

bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)

plt.imshow(output_image)
plt.show()

# https://towardsdatascience.com/object-detection-with-less-than-10-lines-of-code-using-python-2d28eebc5b11