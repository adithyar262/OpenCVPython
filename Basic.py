# Based on https://www.geeksforgeeks.org/introduction-to-opencv/?ref=next_article

import cv2
import numpy as np
import matplotlib.pyplot as plt

print("Hello")


# To read image from disk, we use
# cv2.imread function, in below method,
# Syntax: cv2.imread(path, flag)
# Parameters:
# path: A string representing the path of the image to be read.
# flag: It specifies the way in which image should be read. It’s default value is cv2.IMREAD_COLOR
# Return Value: This method returns an image that is loaded from the specified file.
# Flag values - 
# cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected.
# It is the default flag. Alternatively, we can pass integer value 1 for this flag.
# cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass
# integer value 0 for this flag.
# cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively,
#  we can pass integer value -1 for this flag.

# Note: 
# The image should be in the working directory or a full path of image should be given.
# By default, OpenCV stores colored images in BGR(Blue Green and Red) format.


image = cv2.imread('testImage.jpg')

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array

cv2.imshow("Org", image)

# Matplotlib library uses RGB color format to read a colored image. Here we are demonstrating an
# example of reading an image using this library.
# # Note: See the difference in colors of images read by cv2 and matplotlib library. Because cv2 uses
# BGR color format and matplotlib uses RGB color format. To convert BGR to RGB, we us a function:

plt.imshow(image)
plt.waitforbuttonpress()
plt.close('all')

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.

cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
# cv2.destroyAllWindows()

# Extracting the height and width of an image
h, w, z = image.shape[:3]
# Displaying the height and width
print("Height = {}, Width = {}, Depth = {}".format(h, w, z))
# Extracting RGB values.
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = image[100, 100]

# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))

# We can also pass the channel to extract
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

# We will calculate the region of interest
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700]
cv2.imshow("ROI", roi)
cv2.waitKey(0)
roi1 = image[100 : 500, 200 : 700, 0]
cv2.imshow("ROI1", roi1)
cv2.waitKey(0)
roi2 = image[100 : 500, 200 : 700, 1]
cv2.imshow("ROI2", roi2)
cv2.waitKey(0)
roi3 = image[100 : 500, 200 : 700, 2]
cv2.imshow("ROI3", roi3)
cv2.waitKey(0)

# resize() function takes 2 parameters,
# the image and the dimensions
resize = cv2.resize(image, (500, 500))
cv2.imshow("Resized Image", resize)
cv2.waitKey(0)

# Calculating the ratio
ratio = 800 / w

# Creating a tuple containing width and height
dim = (800, int(h * ratio))

# Resizing the image
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(0)

# We are copying the original image,
# as it is an in-place operation.
output = image.copy()

# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900),
                        (600, 400), (255, 0, 0), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

# Copying the original image
output = image.copy()

# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550),
                cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)


