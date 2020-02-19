import cv2 as _cv2


def crop(img, pxstep=1000, pystep=1000):
    i = 0
    h = img.shape[0]
    w = img.shape[1]
    start_row, start_col = int(0), int(0)

    y = pystep
    while y <= h:
        start_col = 0
        x = pxstep
        while x <= w:
            end_row = int(x)
            end_col = int(y)

            # crop
            # _cv2.imshow("Cropped Top", cropped_img)
            i = i + 1
            print("box no : " + str(i))
            print(start_row, start_col)
            print(end_row, end_col)
            cropped_img = image[start_row:end_row, start_col:end_col]
            image_path_cropped = 'imgs/3_cropped_' + str(i) + '.jpeg'
            _cv2.imwrite(image_path_cropped, cropped_img)

            #  increment to next box
            start_col = x
            x += pxstep

        #  move to next horizontal box
        start_row = y
        y += pystep


image = _cv2.imread("imgs/3.jpeg")

h = image.shape[0]
w = image.shape[1]
print('Height of image:', (h, 'pixels'))
print('Width of image:', (w, 'pixels'))

px = int(w / 3)
py = int(h / 3)
print("width of each grid box ", (px, 'pixels'))
print("height of each grid box ", (py, 'pixels'))

crop(image, px, py)
