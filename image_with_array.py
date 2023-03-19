import numpy as np
import cv2

# Create a black image
black = np.zeros([360,360])

# f_row = black[1:2]
# print(f_row)

# # f_col = black[:,1:2]
# # print(f_col)

black[20:60,60:300] = 10
print(black)

cv2.imshow("black",black)
cv2.waitKey(0)

