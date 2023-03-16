import cv2

image = cv2.imread('ears.jpg') # reading the img by pixels
cv2.imshow('memories', image) # displaying the read image 

print(image) # displays the color scheme in 3d array/matrix
print(image.shape)

# converting the img to greyscale
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # other filters - BGR2Luv, BGR2HSV
cv2.imshow('grey', gray_img)
print(gray_img)

cv2.waitKey(0) # allows the display screen to stay for more than a milli second [takes argument in milliseconds] 