# PRO-C104
---
. . . . 

## project C104 with Whitehat :  Reading and creating images 
- in this class we learnt how to read and create images using the `openCv` package by python
- `openCv` was introduced and installed in the system
- displaying an image 
- displaying a grayscale image
- creating a black-white image using `numpy` package
- adding text and image in an image

## In this class i learnt :  
- in [read_img.py](https://github.com/DhRiTiD/PRO-C104/blob/main/read_img.py) I learnt various uses of the `cv2` package
- these are :
    - `image = cv2.imread(<image_name>)` - it reads the image in matrix / 3D array format 
    - `cv2.imshow(<window_name>, <read_img_variable_name>)` - it returns a window with the mentioned name along with the passed image 
    - `print(image)` - returns a 2D or 3D matrix based on the number of color channels present in the image. [documentation](https://pythonexamples.org/python-opencv-read-image-cv2-imread/)
    - `image.shape` - returns a list with [height, width, channels]
    - `cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)` concerts the entered image to grayscale [you can also change filters by changing the second agrument here]
    - `cv2.waitKey(0)` - allows the display screen to stay without diappearing [takes argument in milliseconds] 
    
- in [create_card.py](https://github.com/DhRiTiD/PRO-C104/blob/main/create_card.py) we foucsed on adding an image and text to the image as required
- `cv2.putText` was introduced to insert text in the image
- `image[10:330,30:330]` is used to take out the given coords of h and w from the read image

- in [image_with_array.py](https://github.com/DhRiTiD/PRO-C104/blob/main/image_with_array.py) I created a simple image using arrays 
- here we took thehelp of `numpy` package to create a 2D array using 1s and 0s

## Project - Our Solar System
- in [label_img.py](https://github.com/DhRiTiD/PRO-C104/blob/main/label_img.py) i labelled a given image of colar system using `cv2.putText()`
