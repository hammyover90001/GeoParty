from tkinter import *
from PIL import ImageTk, Image
import cv2
import numpy as np
from tkinter import Tk, Label
from tkinter import filedialog

import sys
import os
#https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
  #  """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
#^^^ that is the extension that will compare the two images and retun a % value of their similarity.
root = Tk()
difficulty = 0.7
#so these are the images
root.configure(bg = "#52C7D5")


root.title("geo party")
# i am so sorry, but you will have to change all of these to the file path with your imagaes if you want to download this code
# i know there is a better way, but i have not figured it out yet
image1 = ImageTk.PhotoImage(Image.open(resource_path("levels/l1.png")))
image2 = ImageTk.PhotoImage(Image.open(resource_path("levels/l2_2.jpg")))
image3 = ImageTk.PhotoImage(Image.open(resource_path("levels/l3.jpg")))
image4 = ImageTk.PhotoImage(Image.open(resource_path("levels/l4.jpg")))
image5 = ImageTk.PhotoImage(Image.open(resource_path("levels/l5.jpg")))
image6 = ImageTk.PhotoImage(Image.open(resource_path("levels/l6.jpg")))
image7 = ImageTk.PhotoImage(Image.open(resource_path("levels/l7.jpg")))
image8 = ImageTk.PhotoImage(Image.open(resource_path("levels/l8.jpg")))
image9 = ImageTk.PhotoImage(Image.open(resource_path("levels/l9.jpg")))
image10 = ImageTk.PhotoImage(Image.open(resource_path("levels/L10.jpg")))
image11 = ImageTk.PhotoImage(Image.open(resource_path("levels/l11_2.jpg")))
image12 = ImageTk.PhotoImage(Image.open(resource_path("levels/l12_2.jpg")))
image13 = ImageTk.PhotoImage(Image.open(resource_path("levels/l13_2.jpg")))
image14 = ImageTk.PhotoImage(Image.open(resource_path("levels/l14_2.jpg")))
image15 = ImageTk.PhotoImage(Image.open(resource_path("levels/l15_2.jpg")))
thanks = ImageTk.PhotoImage(Image.open(resource_path("levels/thanks.png")))
#made an image list to make it easier to use
image_list = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10,image11,image12,image13,image14,image15,thanks]
# arrray of images to keep them in order and make the level thing easier
# basically this just tells you which image/level you are on
status = Label(root, text= "Level 1 of " + str(len(image_list)), bg = "#52C7D5", bd=1, font=('Times', 20))#
#this is at the top and just tells you what level you are on. the variable level is also used for fingidn the referance image. 
level = 0
def find_template(level):
    global labl_results
    template = ""

    level = level-1
    if level ==1:
        template = resource_path("checks/c1.png")
    if level == 2:
        template = resource_path("checks/c1.png")
    if level == 3:
        template = resource_path("checks/c3.png")
    if level ==4:
        template = resource_path("checks/c4.png")
    if level == 5:
        template = resource_path("checks/c5.png")
    if level == 6:
        template = resource_path("checks/c6.png")
    if level ==7:
        template = resource_path("checks/c7.png")
    if level == 8:
        template = resource_path("checks/c8.png")
    if level == 9:
        template = resource_path("checks/c9.png")
    if level ==10:
        template = resource_path("checks/c10.png")
    if level == 11:
        template = resource_path("checks/c11.png")
    if level == 12:
        template = resource_path("checks/c12.png")
    if level == 13:
        template = resource_path("checks/c13.png")
    if level == 14:
        template = resource_path("checks/c14.png")
    if level == 15:
        template = resource_path("checks/c15.png")
    #the template is used as the referance image and it is used to search the submitted image to see if it is in there
    
    filepath = filedialog.askopenfilename()
    # Load the image
    img = cv2.imread(filepath)
    temp = cv2.imread(template)
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    #the threshold is basically the similarity. the higher it is, the more precice the image has to be. .6 is fairly easy and just tells me what location you are in, although it is easy to cheat
    #basically if one image is one tone of color, for example green grass. then any primarily green image that is submitted will be found to be the same
    # i could make the threshold .7 but then it becomes borderline impossible
    loc = np.where(res >= threshold)
    print(res)
    if len(loc[0]) == 0:
        print("fail")
        labl_results = Label(root, text="LEVEL FAILED YOU LOOSER",bg = "#52C7D5", font=('Times',25)).grid(row=9,column=0)
        return False
      #tells you if you passed or failed

    labl_results = Label(root, text="CONGRANTS. YOU DONE IT!",bg = "#52C7D5", font=('Times',25)).grid(row=9,column=0)
    print("pass")
    return True
# button loads the next image
def forward(level_num):
    global Labell
    global button_forward
    global button_back
    Labell.grid_forget()
    global level
    global button_print
    global DIFFICULTY
    global labl_results
    labl_results = Label(root, text = "           Submit to get results           " ,bg = "#52C7D5", font=('Times', 25)).grid(row=9, column=0)
    #^rests the box so the next image can load
    Labell = Label(image = image_list[level_num-1])
    #^this gets the image
    button_forward = Button(root, text="Next",font=("times",18), bg = "#64B5F6", command = lambda: forward(level_num+1))
    button_back=Button(root, text="Previous",font=("times",18), bg = "#64B5F6", command= lambda : back(level_num-1))

    #^ forward and backwards
    if level_num == 16:
        button_forward = Button(root, text="Next",font=("times",18), bg = "#64B5F6", state= DISABLED)
        button_print = Button(root, text="Submit Image", font=('Times', 25), bg="#4CAF50",state=DISABLED).grid(row=10, column=1, columnspan=40, pady=20)
    #^stops it from going past 10
    if level_num<5:
        DIFFICULTY = Label(root, bg="#66BB6A", text="DIFFICULTY = GREEN (baby)", font=("Times", 30)).grid(row=9, column=1)
    if level_num >= 5:
        DIFFICULTY = Label(root, bg="#FFD54F", text="DIFFICULTY = ORANGE ( :/ )", font=("Times", 30)).grid(row=9, column=1)
    if level_num>= 10:
        DIFFICULTY = Label(root, bg="#FF7043", text="    DIFFICULTY = RED ( >:) )  ", font=("Times", 30)).grid(row=9, column=1)
    Labell.grid(row=1, column=0, columnspan=3)
    button_back.grid(row = 2, column=0,padx=280)
    button_forward.grid(row = 2, column=1)
    #^the position

    status = Label(root, text="Level "+ str(level_num) +" of " + str(len(image_list)), bd=1, font=('Times', 20), bg = "#52C7D5")
    status.grid(row=0, column=0, columnspan=3, sticky=W + E)
    level = level_num


#this is the exact same as the forward button
def back(level_num):
    global Labell
    global button_forward
    global button_back
    global level
    Labell.grid_forget()
    global DIFFICULTY
    global labl_results
    global button_print
    button_print = Button(root, text="Submit Image", font=('Times', 25), bg="#4CAF50",command=lambda: find_template(level + 1)).grid(row=10, column=1, columnspan=40, pady=20)
    labl_results = Label(root, text="           Submit to get results           ", bg="#52C7D5",font=('Times', 25)).grid(row=9, column=0)
    if level_num < 5:

        DIFFICULTY = Label(root, bg="#66BB6A", text="DIFFICULTY = GREEN (baby)", font=("Times", 30)).grid(row=9, column=1)
    if level_num >= 5:
        DIFFICULTY = Label(root, bg="#FFD54F", text="DIFFICULTY = ORANGE ( :/ )", font=("Times", 30)).grid(row=9, column=1)
    if level_num >= 10:
        DIFFICULTY = Label(root, bg="#FF7043", text="    DIFFICULTY = RED ( >:) )  ", font=("Times", 30)).grid(row=9, column=1)
    Labell.grid_forget()
    Labell = Label(image=image_list[level_num - 1])
    button_forward = Button(root, text="Next", bg = "#64B5F6", font=("times",18), command=lambda: forward(level_num + 1))
    button_back = Button(root, text="Previous", bg = "#64B5F6",font=("times",18), command=lambda: back(level_num - 1))
    if level_num == 1:
        button_back = Button(root, text="Previous", bg = "#64B5F6",font=("times",18), state=DISABLED)

    Labell.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=2, column=0,padx=280)
    button_forward.grid(row=2, column=1)

    status = Label(root, text="Level "+ str(level_num) +" of " + str(len(image_list)), bd=1, font=('Times', 20), bg = "#52C7D5")
    status.grid(row=0, column=0, columnspan=3, sticky=W + E)
    level = level_num

Labell = Label(image = image1)
Labell.grid(row=1, column=0,columnspan=3)


#the first image should be the tutorial thing
#it will basically explain how the game works and how to submit
#or like first 3 images
#then the game actually starts
labl_results = Label(root,bg = "#52C7D5", text="           Submit to get results           ", font=('times',25)).grid(row=9,column=0)
#usrimage = np.array(Image.open(usrin))
#down below are all the buttons and whatnot

button_print = Button(root,text="Submit Image",font=('Times',25),bg = "#4CAF50", command = lambda: find_template(level+1)).grid(row = 10 ,column=1,columnspan=40, pady=20)
DIFFICULTY = Label(root, bg = "#66BB6A", text="DIFFICULTY = GREEN (baby)",font=("Times", 30)).grid(row = 9, column=1)
button_back = Button(root,text="Previous", bg = "#64B5F6", font=('Times', 18), command = back).grid(row = 2, column=0,padx=280)
button_forward = Button(root,text="Next", bg = "#64B5F6", font=('Times', 18), command = lambda : forward(2)).grid(row = 2, column=1)

status.grid(row=0, column=0, columnspan=3, sticky= W+E)
root.mainloop()
