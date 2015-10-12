# -*- coding: cp1252 -*-
from SimpleCV import Camera,Image,Display
from math import *
display=Display()
cam=Camera()
sung=Image("E:/sung2.png")
sung2=Image("E:/RAY-BAN-Mens-Unisex-Designer-Genuine-Sunglasses-Aviator-RayBan-RB-4180-RRP-£165-For-Sale-at-UsedLux.com-Preowned-Used-designer-clothing-in-London-3-182103112013w.jpg")
sung2=sung2.invert()
sungar=[sung,sung2]
i=0
img3=sungar[i]
while display.isNotDone:
    img=cam.getImage()
    faces=img.findHaarFeatures('face.xml')
    if faces is not None:
        faces=faces.sortArea()
        bigface=faces[-1]
        bigeye=img.findHaarFeatures('two_eyes_big.xml')
        if(bigeye is not None):
          bigeye=bigeye.sortArea()
          bigeye=bigeye[-1]
          print "yo"
        lefteye=img.findHaarFeatures('lefteye.xml')
        righteye=img.findHaarFeatures('right_eye.xml')
        if lefteye is not None and righteye is not None:
             if bigeye is not None:
               a=int((bigeye.width()))
               b=int((bigeye.height()))
               print a,b
               sungar[i]=sungar[i].resize(a+20,b+15)
             if bigeye is not None:
                xsung=bigeye.x-a/2-10
                ysung=bigeye.y-b/2
                c=a+20
                d=b+15
                img3=sungar[i]
                img3=img.crop(xsung,ysung,c,d,False)
                img3=img3-sungar[i]
                img=img.blit(img3,pos=(xsung,ysung),mask=None)
                bigface.draw()
        elif lefteye is None and righteye is not None:
            if i==0:
              i=i+1
              print "i"
        elif lefteye is not None and righteye is None:
            if i==1:
              i=i-1
              print i
            
    img.save(display)
