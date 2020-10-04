import cv2 as _cv2


class Box:
    boxes = [1, 2, 3, 4, 5, 6]

    def __init__(self, index, start_row, end_row, start_col, end_col):
        self.index = index
        self.start_row = start_row
        self.end_row = end_row
        self.start_col = start_col
        self.end_col = end_col


# def box():
#     b = dict();
#     b['index'] = 0
#     b['start_row'] = 0
#     b['endrow'] = 0
#     b['startcol'] = 0
#     b['endcol'] = 0
#     return b


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


def crop(img, pxstep=1000, pystep=1000):
    i = 0
    h = img.shape[0]
    w = img.shape[1]
    start_row, start_col = int(0), int(0)

    y = pystep
    while y <= h:
        start_row = 0
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
            start_row = x
            x += pxstep

            # box = Box(i , start_row , start_col , end_row , end_col)

            #  move to next horizontal box
        start_col = y
        y += pystep


image = _cv2.imread("../imgs/3.jpeg")

h = image.shape[0]
w = image.shape[1]
print('Height of image:', (h, 'pixels'))
print('Width of image:', (w, 'pixels'))

px = int(w / 3)
py = int(h / 2)
print("width of each grid box ", (px, 'pixels'))
print("height of each grid box ", (py, 'pixels'))

# get grids
draw_grid(image, (0, 255, 0), 2, 4, px, py)
image_path_processed = '../imgs/3_processed_3x2.jpeg'
_cv2.imwrite(image_path_processed, image)

# crop into 3x2 boxes
crop(image, px, py)
