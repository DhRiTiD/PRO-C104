import cv2

ss = cv2.imread('images/solar-system.jpg')

# dictionary to store name of planets and there text posions on the image 'ss'
ss_dict= { 'Mercury' : (116, 245), 'Venus': (210, 175), 'Earth': (300, 260), 'Moon': (336, 158), 'Mars': (400, 178), 'Jupiter': (640, 350), 'Saturn': (715, 270), 'Uranus': (900, 162),'Neptune': (1090, 278) }

# displaying SUN
cv2.putText(ss,  
           'SUN',
           (100,90),  
           fontFace=cv2.FONT_HERSHEY_DUPLEX,
           fontScale=1.3,  
           color=(66, 255, 252)
           )

for name, position in ss_dict.items():
    #print(name, ':', position)

    cv2.putText(ss,  
           name,
           position,  
           fontFace=cv2.FONT_HERSHEY_SIMPLEX,
           fontScale=0.55,  
           color=(255, 255, 255)
           )
 
cv2.imwrite('images/labelled_image.jpg', ss) # saving the new img
cv2.imshow('labelled img',ss) # displaying the new image
cv2.waitKey(0)

# new labelled image saved in the images folder for refrence
