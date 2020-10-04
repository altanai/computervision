import cv2
# matplotlib to create histogram plots
import matplotlib.pyplot as plt

image = cv2.imread('ramudroidimg.jpg')

# CalcHist Calculates a histogram of a set of arrays params are images, channels, mask, histsize, ranges
histogram = cv2.calcHist([image], [0], None, [256], [0,256])

# plot a histogram, ravel() flatens our image array
plt.hist(image.ravel(),256,[0,256])
# plt.show()

# viewing seperate color channels
color = ('b','g','r')

# separate the color and plot each in histogram
for i, col in enumerate (color):
    print(" calculate hist for ", col)
    histogram2 = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot( histogram2, color=col)
    plt.xlim([0,256])
    plt.show()