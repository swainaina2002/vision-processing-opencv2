import cv2
import numpy as np 

# print ('package is installed successfully')

# # read an image and show 
# img  = cv2.imread("Resources/image1.jpg")

# # to show the image 
# cv2.imshow("Read Image", img)
# cv2.waitKey(0)

# read a video and display it

# cap =cv2.VideoCapture("Resources/VID1.mp4")

# to display it

# while True:

#     success, img =cap.read()

#     cv2.imshow("Video", img)

#     if cv2.waitKey(1) &0xFF ==ord('q'):
#         break 


# read a webcam and display it.

# webcam = cv2.VideoCapture(0)
# define the width and height 
# 3 = width, 4 = height

# webcam.set(3,640)
# webcam.set(4,480)

# to display the webcam

# while True:

#     success, img = webcam.read()

#     cv2.imshow("webcam", img)

#     if cv2.waitKey(1) &0xFF ==ord('q'):
#         break 


# converting an image to grayscale

# img = cv2.imread("Resources/image1.jpg")

# cv2.imshow("Image",img)

# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(img, (3,9), 0)

# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)

# cv2.waitKey(0)

# image eroding
# img = cv2.imread("Resources/image1.jpg")

# cv2.imshow("Image",img)
# kernel = np.ones((5, 5), np.uint8)

# imgErode = cv2.erode(img, kernel, iterations=3)
# cv2.imshow("eroded ", imgErode)
# cv2.waitKey(0)

# edge detection 
# img = cv2.imread("Resources/image1.jpg")
# imgCanny = cv2.Canny(img, 100,100)
# cv2.imshow("Edges", imgCanny)
# cv2.waitKey(0)

# # Using the Canny filter to get contours
# edges = cv2.Canny(imgGray, 20, 30)
# # Using the Canny filter with different parameters
# edges_high_thresh = cv2.Canny(imgGray, 60, 120)
# # Stacking the images to print them together
# # For comparison
# images = np.hstack((imgGray, edges, edges_high_thresh))

# # Display the resulting frame
# cv2.imshow('img', canny_images)
# img = cv2.imread("Resources/image1.jpg")
# cv2.line(img,(0,0),(300,300), (255,0,0), 5)
# cv2.imshow("draw on image", img)
# cv2.waitKey(0)



import cv2
#import numpy as np

#to create a blank image
#img = np.zeros(shape=[512, 512, 3], dtype=np.uint8  

#call an image in the directory
# img = cv2.imread('Resource/image1.jpg')

# position = (100,50)
# cv2.putText(
#      img, #image on which text is written
#      "This is a tomb raider image", #text
#      position, #position at which writing has to start
#      cv2.FONT_HERSHEY_COMPLEX, #font family
#      1, #font size
#      (0, 0, 255), #font color
#      3) #font stroke
# cv2.imshow('Read Image', img)
# cv2.waitKey(0)

cv2.imshow("Image", img)
