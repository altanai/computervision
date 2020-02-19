import cv2

img = cv2.imread("imgs/4.jpg")

start_x = img.shape[1]/2
start_y = 0
end_x = img.shape[1]/2
end_y = img.shape[0]

cv2.line(img, (start_x, start_y), (end_x, end_y), (255, 0, 0), 1, 1)

img_path_processed = 'imgs/4_processed.jpg'
cv2.imwrite(img_path_processed, img)
