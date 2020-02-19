import cv2 as _cv2

def draw_grid(img, line_color=(0, 255, 0), thickness=1, type_=_cv2.LINE_AA, pxstep=400):
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
    y = pxstep
    while x < img.shape[1]:
        _cv2.line(img, (x, 0), (x, img.shape[0]), color=line_color, lineType=type_, thickness=thickness)
        x += pxstep

    while y < img.shape[0]:
        _cv2.line(img, (0, y), (img.shape[1], y), color=line_color, lineType=type_, thickness=thickness)
        y += pxstep


img = _cv2.imread("imgs/4.jpg")
draw_grid(img)
img_path_processed = 'imgs/4_processed.jpg'
_cv2.imwrite(img_path_processed, img)