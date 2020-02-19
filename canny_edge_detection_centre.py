import cv2 as _cv2
import numpy as np

image = _cv2.imread("imgs/1.jpeg")

# print the dimensions
print(image.shape)
h = image.shape[0]
w = image.shape[1]
print('Height of image:', (h, 'pixels'))
print('Width of image:', (w, 'pixels'))

# Divide image into grid of 3x3

start_row = int(w / 3)
start_col = int(h / 3)
end_row = int(2 * w / 3)
end_col = int(2 * h / 3)


# cropped_img = image[start_row:end_row, start_col:end_col]


# # converting BGR to HSV
# hsv = _cv2.cvtColor(image, _cv2.COLOR_BGR2HSV)
#
# # define range of red color in HSV
# lower_red = np.array([30, 150, 50])
# upper_red = np.array([255, 255, 180])
#
# # create a red HSV colour boundary and
# # threshold HSV image
# mask = _cv2.inRange(hsv, lower_red, upper_red)
#
# # Bitwise-AND mask and original image
# res = _cv2.bitwise_and(image, image, mask=mask)
#
# # Display an original image
# _cv2.imshow('Original', image)

# sharpening image with gaussian smoothing filter
def unsharp_mask(image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = _cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened


sharpened_image = unsharp_mask(image)
_cv2.imwrite('3_sharpened.jpeg', sharpened_image)
# whole image
edges = _cv2.Canny(sharpened_image, h, w)

# 1st grid
# edges = _cv2.Canny(image,end_row,end_col)
_cv2.imshow('Edges', edges)

image_path_processed = 'imgs/3_edges.jpeg'
_cv2.imwrite(image_path_processed, edges)

_cv2.waitKey()
_cv2.destroyAllWindows()
