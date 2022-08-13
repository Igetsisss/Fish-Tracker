# Importing all modules
from multiprocessing.spawn import import_main_path
from types import coroutine
import cv2
import numpy as np
import discord
import random
from tkinter import *
from tkinter import ttk
import time
import math
window = Tk()
# set window title
window.title("my fucking fish window")
# set window width and height
window.configure(width=500, height=300)
lbl=Label(window, text="absulty fucking nothing is dedacted", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
# set window background color
window.configure(bg='blue')


font = cv2.FONT_HERSHEY_COMPLEX
# Specifying upper and lower ranges of color to detect in hsv format
lower = np.array([90, 150, 20])
upper = np.array([130, 255, 255]) # (These ranges will detect Yellow)

# Capturing webcam footage
webcam_video = cv2.VideoCapture(0)

while True:
    success, video = webcam_video.read() # Reading webcam footage

    img = cv2.cvtColor(video, cv2.COLOR_BGR2HSV) # Converting BGR image to HSV format

    mask = cv2.inRange(img, lower, upper) # Masking the image to find our color

    mask_contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Finding contours in mask image

    # Finding position of all contours
    if len(mask_contours) != 0:
        for mask_contour in mask_contours:
            if cv2.contourArea(mask_contour) > 500 : # You can change the number here to how big or small the cotour can be
                x, y, w, h = cv2.boundingRect(mask_contour)
                cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 3) #drawing rectangle
                cv2.putText(video, str(x) + " " + str(y) , (x, y),font, 0.5, (255, 0, 0)) 
                lbl.config(text="")
                lbl=Label(window, text=(x,y), fg='red', font=("Helvetica", 16))
                lbl.place(x=20, y=20)
                window.update()
                if (0, 0) <= (x, y) <= (100, 100):
                  print("t")
                  lbl=Label(window, text="Blue SHit at top Left", fg='red', font=("Helvetica", 16))
                  lbl.place(x=50,  y=50)
                  window.update()
            if cv2.contourArea(mask_contour) < 500:
                lbl.config(text="")
                lbl=Label(window, text="", fg='red', font=("Helvetica", 16))
                lbl.place(x=50, y=50)
                lbl=Label(window, text="No BLue shit", fg='red', font=("Helvetica", 16))
                lbl.place(x=20, y=20)
    
    cv2.imshow("mask image", mask) # Displaying mask image

    cv2.imshow("window", video) # Displaying webcam image
    
    cv2.waitKey(1)
    
    window.update()