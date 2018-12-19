#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 12:39:44 2018

@author: sme
"""
#importing required libraries
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

#constructing the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())


#initializing dlib's face detector (HOG based) and then create 
#the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])


#before we can detect the features, we need to first detect the face in our
#image
image = cv2.imread(args["image"])
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detect faces in the grayscale image
rects = detector(gray,1)
count = 0

#lopoing over the face detections
for (i,rect) in enumerate(rects):
    #determine the facial landmarks for the face region, then
    #convert the facial landmark's co-ordinates to NumPy array.
    
    shape = predictor(gray,rect)
    shape = face_utils.shape_to_np(shape)
    
    #convert dlib's rectangle to a OpenCV-style bounding box
    # i.e. (x,y,w,h) then draw face boundin box
    (x,y,w,h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        
    #couting the face
    count = count+1
        
    #looping over the x,y coordinates for the facial landmarks
    #and drawing them on image
        
    for (x,y) in shape:
        cv2.circle(image,(x,y),1,(0,0,255),-1)

cv2.putText(image, "Heads = {}".format(count), (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)        
        
#display final image
cv2.imshow("Output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


