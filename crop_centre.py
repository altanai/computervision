import cv2 as _cv2

image = _cv2.imread("imgs/3.jpeg")

# print the dimensions
print(image.shape)
h = image.shape[0]
w = image.shape[1]
print('Height of image:', (h, 'pixels'))
print('Width of image:', (w, 'pixels'))

# Divide image into grid of 3x3

start_row = int(w/3)
start_col = int(h/3)
end_row = int(2*w/3)
end_col = int(2*h/3)

cropped_img = image[start_row:end_row, start_col:end_col]

# crop
# _cv2.imshow("Cropped Top", cropped_img)

image_path_cropped = 'imgs/3_cropped_centre.jpeg'
_cv2.imwrite(image_path_cropped, cropped_img)
