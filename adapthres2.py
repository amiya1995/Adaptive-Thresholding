import cv2
import numpy as np
from matplotlib import pyplot as plt
#import necessary packages
img = cv2.imread('Image 11.JPG',0)#read image
img = cv2.medianBlur(img,5)#apply medianBlur


th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)#apply adaptive threshold


titles = ['Original Image', 'Adaptive Mean Thresholding']#Apply titles
images = [img, th2]

for i in xrange(2):#Apply for loop
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()#show Image
