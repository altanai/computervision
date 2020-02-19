import cv2
image = cv2.imread('ramudroidimg.jpg')

# opencv's split function splits the image into each color index
B,G,R = cv2.split(image)
cv2.imshow("Red",R)
cv2.imshow("Green",G)
cv2.imshow("Blue",B)

# make the original image by merging the individual color components
merged = cv2.merge([B,G,R])
cv2.imshow("merged",merged)

# amplifying the blue color
mergedb = cv2.merge([B+100,G,R])
cv2.imshow("merged with blue amplify",mergedb)

# amplifying the red color
# mergedr = cv2.merge([B,G,R+100])
# cv2.imshow("merged with blue amplify",mergedr)

# amplifying the green color
# mergedg = cv2.merge([B,G+100,R])
# cv2.imshow("merged with green amplify",mergedg)

# representing the shape of individual color components.
# the output wuld be only two dimension whih wouldbe height and width, since third element of RGB component is individually represented
print("Shape of Blue color component ", B.shape)
print("Shape of Red color component ", R.shape)
print("Shape of Green color component ",G.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()