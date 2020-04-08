#Author:Sisquoc
from PIL import Image
import os 
import cv2
import numpy

#gamma transmission of images
#sources' path
img = cv2.imread("./sources/xxx.png")
#Do it twice to choose the best image
for gamma1 in range(15,20):
    for gamma2 in range(6,9):
        fgamma1=gamma1/10
        fgamma2=gamma2/10
        img_t= cv2.convertScaleAbs(img)
        img_gamma1 = numpy.power((img_t/255.0),fgamma1)*255.0
        img_gamma2=numpy.power((img_gamma1/255.0),fgamma2)*255.0
        cv2.imwrite(str(fgamma1)+str(fgamma2)+"xxx.png",img_gamma2)
