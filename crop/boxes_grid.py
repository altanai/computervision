import cv2 as _cv2


def draw_grid(img, line_color=(0, 255, 0), thickness=3, type_=_cv2.LINE_AA, pxstep=1000, pystep=1000):
    '''(ndarray, 3-tuple, int, int) -> void
    draw gridlines on img
    line_color:
        BGR representation of colour
    thickness:
        line thickness
    type:
        8, 4 or cv2.LINE_AA
    pxstep:
        grid line frequency in pixels
    '''
    x = pxstep
    y = pystep
    while x < img.shape[1]:
        _cv2.line(img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep

    while y < img.shape[0]:
        _cv2.line(img, (0, y), (img.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        y += pystep


image = _cv2.imread("../imgs/3.jpeg")

# print the dimensions
print(image.shape)
print('Height of image:', (image.shape[0], 'pixels'))
print('Width of image:', (image.shape[1], 'pixels'))

px = int(image.shape[1] / 3)
py = int(image.shape[0] / 3)

# get grids
draw_grid(image,(0, 255, 0),2, 4, px, py)

image_path_processed = '../imgs/3_processed.jpeg'
_cv2.imwrite(image_path_processed, image)
