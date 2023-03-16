import cv2
filter = cv2.imread('ears.png')
img = cv2.imread('img.jpg')

ears = filter[10:330,30:330] #height. width
img[12:332, 330:630] = ears

txt1 = 'some memories never get old!'

cv2.putText(img,  
           txt1,
           (400, 360),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1.3,  
           color=(180, 200, 255)
           )

cv2.imshow("output",img)
cv2.waitKey(0)