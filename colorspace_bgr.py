# RGB, HSV, CMYK  are 3 color spaces to store images
import cv2

image = cv2.imread('ramudroidimg.jpg')

print('Color 3D image shape ', image.shape)
# B,G,R value for the first 0,0 pixel
B, G, R = image[0, 0]
print('BGR value for 0,0 pixel - ', B, G, R)
print('pixel value for 100,200 pixel - ', image[100, 200])

# convert to grayscale image
print('---------------------------------')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print('Grayscale Shape ', gray_img.shape)
print('pixel value for 100,200 pixel -', gray_img[100, 200])
