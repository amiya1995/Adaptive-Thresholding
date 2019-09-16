import cv2
import numpy as np
from matplotlib import pyplot as plt
#import necessary packages

img = cv2.imread('Image 11.JPG',0)#read image
img = cv2.medianBlur(img,5)#apply medianBlur

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#apply adaptive threshold


titles = ['Original Image', 'Global Thresholding (v = 127)']#Apply titles
images = [img, th1]

for i in xrange(2):#Apply for loop
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()#show Image
