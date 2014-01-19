# 
# Description: Starts webcam and takes a picture when spacebar is pressed
# Author:      Cody Ray Freeman Hoeft (OSU Mars Rover Team)
# Date:        Winter Term 2014
# Origin:      Based on OpenCV Tutorial: http://docs.opencv.org/trunk/doc/py_tutorials/py_gui/py_video_display/py_video_display.html#display-video
# Usage:       TBD
# 
import sys
import numpy as np
import cv2
import os

#constant format will be root000.ftype
root = "image"
ftype = ".png"

#This function is responsible for displaying the video on screen
def camera_loop(capture):
    loop_var = 1
    while(loop_var):
        # Capture frame-by-frame
        ret, frame = capture.read()

        frame = operations(frame)

        # Display the resulting frame
        cv2.imshow('frame',frame)
        loop_var = key_handle(cv2.waitKey(1), frame)

#This Function Handles the keypress values
#An output of 0 means end the program
#An output of anything else means it will continue
def key_handle(key,image):
    if key == -1:
        return 1
    elif key & 0xFF == 32: #Spacebar
        take_picture(image)
    elif key & 0xFF == ord('q'):
        return 0
    else:
        print key & 0xFF
    return 1

#This function can be used to 
def operations(frame):
#    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame

#This Function saves the image and shows the output file
def take_picture(image):
    cv2.imshow('Picture',image)
    cv2.imwrite(get_name(),image)

#This Function generates a filename for the image that has not been used yet
def get_name():
    postfix = 1
    #str(postfix).zfill(3) pads the numbers so they sort correct in file managers
    filename = root + str(postfix).zfill(3) + ftype 
    while os.path.isfile(filename):
        print filename + " is used already"
        postfix += 1
        filename = root + str(postfix).zfill(3) + ftype 
       
    print filename + " doesn't exist, using it"
    print "" 

    return filename

#Init Program

capture = cv2.VideoCapture(0)

camera_loop(capture)

#End Program Clean Up
capture.release()
cv2.destroyAllWindows()
