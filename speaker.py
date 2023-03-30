import os 
import pyttsx3
import tkinter
from tkinter import ttk
from tkinter import *

engine = pyttsx3.init()

def speak():
   if __name__ == "__main__":
      while True:
           text = inp.get()
           engine.say(text)
           engine.runAndWait()
           break
      

def clear():
    inp.delete(0, END)
            
# GUI 

col1 = "white"
col2 = "yellow"
col3 = "red"
f1 = "blue"
root = Tk()
root.title("Personal Speaker")
root.geometry("420x150")
root.resizable(height = False , width = False)
# upper frame
frame_up = Frame(root , width = 720 , height = 70 , bg =col3)
frame_up.grid(row = 0 , column = 0)
heading = Label (frame_up , text = "Type What You Want To Speak -", bg = col3 , fg ="black",font =("ivy 20 italic") )
heading.place(x = 0, y = 10)
line = Label(frame_up,  width =380,text = "" , height = 1 , bg = col2 ,  anchor = "nw")
line.place(x = 0 , y = 65)
# framedown
frame_down = Frame(root , width = 720 , height = 480, bg =col1 )
inp = Entry(frame_down,width = 55 , justify = "center" , font=("arial  10") , highlightthickness=2)
inp.place(x = 10 , y = 10)
frame_down.grid(row = 1, column = 0)
# Attendence Button
btn_speak = Button(frame_down , text ="Speak", width = 15  , fg = "black", command = speak)
btn_speak.place(x = 15, y =50)
btn_clear = Button(frame_down , text ="Clear", width = 15  , fg = "black", command = clear)
btn_clear.place(x = 175, y =50)
text = Label(frame_down,text="THANKS!✌️" , bg = col1)
text.place(x=350,y=50)
root.mainloop()