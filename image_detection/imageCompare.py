import cv2
import numpy as np
import sys
from datetime import datetime

# to install cv2:
# pip install opencv-contrib-python

# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   print(img1.size, img2.size)
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

def getDiff(imageName1, imageName2):
    start = datetime.now()
    img1 = cv2.imread(imageName1)
    img2 = cv2.imread(imageName2)
    # convert the images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    error, diff = mse(img1, img2)
    print("Image matching MSE Error between the two images:",error)
    end = datetime.now()
    print("time taken to run: ", end - start)
    # cv2.imshow("difference", diff)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# getDiff('hands1.jpeg', 'nohands1.jpeg')
# getDiff('hands1.jpeg', 'nohands2.jpeg')
# getDiff('nohands1.jpeg', 'nohands2.jpeg')

def main():
    args = sys.argv[1:]
    imageName1, imageName2 = args[0]+".jpg", args[1]+".jpg"
    print(imageName1 + ",  " + imageName2)
    getDiff(imageName1, imageName2)

main()

# hands1 nohands1 Matching Error: 42.11799529510838
# hands2 nohands2 Matching Error: 43.47860879498404
# hands3 nohands3 Matching Error: 45.02188003050072