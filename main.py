import subprocess
global usrimage
from tkinter import *
from tkinter import Tk, Label
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
# so all the stuff above i have no idea how it workds becauese i followed a yt tutorial. 
#this one>>>> https://www.youtube.com/watch?v=p3tSLatmGvU <<<<if you are interested
def mains():
    loading_root.destroy()
    cmd = 'python mainwin.py'
    p = subprocess.Popen(cmd, shell=True)
    out,err = p.communicate()
    print(err)
    print(out)
    #this basicall just closes down the window and starts to run mainwin.py which is the other file, which is the core game. 
    #the reason I did this is because otherwise opencv would not work. I dunno why, it just didnt wanna run

def instructions():
    def destroy():
        instructions.destroy()
    instructions = Tk()

    Windowh = 1000
    Windowl = 200
    screenwidth = instructions.winfo_screenwidth()
    screenhieght = instructions.winfo_screenheight()
    x = (screenwidth / 2) - (Windowh / 2)
    y = (screenhieght / 2) - (Windowl / 2)
    instructions.geometry(f'{Windowh}x{Windowl}+{int(x)}+{int(y)}')

    instructions_l = Label(instructions,text="To play, you will first have to select a level, buy clicking forwards or back (difficulty is shown)",font=("Times",18))
    instructions_l.pack()
    instructions_l2 = Label(instructions,text="Then you view the image and try to find that location in real life.",font=("Times",18))
    instructions_l2.pack()
    instructions_l3 = Label(instructions, text="Once you find the location, you will have to line up the angle just right,",font=("Times",18))
    instructions_l3.pack()
    instructions_l4 = Label(instructions, text="Then you upload it to the program, and then it will tell you if you succeeded or not",font=("Times",18))
    instructions_l4.pack()

    instructions_back = Button(instructions,text="Return", font = ("Times",20),command = destroy)
    instructions_back.pack(pady=10)
    #this is the instructions tab that opens up. its pretty basic
def usure():
    def quitt():
        loading_root.quit()
        u.quit()
    def uitt():
        u.destroy()
    u = Tk()
    Windowh = 500
    Windowl = 360
    screenwidth = loading_root.winfo_screenwidth()
    screenhieght = loading_root.winfo_screenheight()
    x = (screenwidth / 2) - (Windowh / 2)
    y = (screenhieght / 2) - (Windowl / 2)
    u.geometry(f'{Windowh}x{Windowl}+{int(x)}+{int(y)}')
    #this centres the window the the middle of any screen on any computer. 
    u.title('u sure?')
    ulabel = Label(u,bg = "#52C7D5" , text = "Are you sure you want to quit?",font = ("Times",30))
    ulabel.pack()
    u.configure(bg = "#52C7D5")
    uno = Button(u,text = "I'm no wuss",bg = "#81C784" ,font =  ("Times",30),command = uitt)
    uno.pack(pady= 10)
    spacer = Label(u,bg = "#52C7D5")
    spacer.pack(pady=80)
    ubutton = Button(u,text = "Yes",bg = "#F4827B",font = ("Times",5),command = quitt)
    ubutton.pack(pady= 10)
    #this is the "you sure" button that comes up whenever you try to close anythign ever. 
    

loading_root = Tk()

Windowh = 500
Windowl = 360
screenwidth = loading_root.winfo_screenwidth()
screenhieght = loading_root.winfo_screenheight()
x = (screenwidth / 2) - (Windowh / 2)
y = (screenhieght / 2) - (Windowl / 2)
loading_root.geometry(f'{Windowh}x{Windowl}+{int(x)}+{int(y)}')
# agian this centres it

loading_root.configure(bg = "#52C7D5")
loading_root.title("launcher.exe")
#everything below this is just buttons. they are pretty self explanitory
loading_label = Label(loading_root, text="GEO PARTY",bg = "#52C7D5", font=("Times", 30))
loading_label.pack(pady=20)

loading_button = Button(loading_root, text="P  L  A  Y",bg = "#48C2D2", font=("Times", 30), command=mains)
loading_button.pack(pady=20)

loading_play = Button(loading_root, text="How To Play", bg = "#48C2D2", font=("Times", 18), command=instructions)
loading_play.pack(pady=20)

quit_button = Button(loading_root,bg = "#F4827B",text="I accdentally launched the program and dont want to play it so can I please leave",font=("Times", 11), command = usure)
quit_button.pack(pady=20)


mainloop()
