#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from datetime import datetime
import py_files.controller as con

bubbles = []

class BotBubble:
    def __init__(self,master, kindOfMessage, message=""):
        self.master = master
        self.frame = tk.Frame(master,bg="light grey")
        if kindOfMessage == "recieved":
            position = [350, 160]
            func = self.draw_triangle_reverse
        else:
            position = [100, 160]
            func = self.draw_triangle
        self.i = self.master.create_window(position[0],position[1],window=self.frame)
        tk.Label(self.frame, text = datetime.now().strftime("%d.%m.%Y %H:%M:%S"),font = ("Helvetica", 7),bg="light grey").grid(row=0,column=0,sticky="w",padx=5)
        tk.Label(self.frame, text = message,font = ("Helvetica", 9),bg = "light grey").grid(row=1, column=0,sticky="w",padx=5,pady=3)
        root.update_idletasks()
        self.master.create_polygon(func(self.i), fill="light grey", outline="light grey")

    def draw_triangle(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x1, y2 - 10, x1 - 15, y2 + 10, x1, y2
    
    def draw_triangle_reverse(self,widget):
        x1, y1, x2, y2 = self.master.bbox(widget)
        return x2, y2 - 10 , x2 + 15 , y2 + 10, x1, y1

def print_message(kindOfMessage, query):
    if bubbles:
        canvas.move(tk.ALL, 0, -65)
    a = BotBubble(canvas, kindOfMessage, message = query)
    bubbles.append(a)
    
def splitStringInLinesWithCharNum(string, charNum):
    newString = ""
    stringArray = string.split()
    if len(stringArray) == 1:
        return string
    for i in range(0, len(stringArray), 2):
        if len(stringArray[i] + " " + stringArray[i+1]) > charNum:
            newString += "\n" + stringArray[i] + " " + stringArray[i+1]
        else:
            newString += " " + stringArray[i] + " " + stringArray[i+1]
    return newString

def getResultFromServer(query):
    c = con.ControlManager(query)
    c.initSession()
    c.crawlQuery()
    result = c.executeFiltering()
    c.closeSession()
    return result

def mouse_move_callback(event):
    # use event.y with a previous remembered y value to determine
    # directions
    directions = event.y # just as an example, could also be -1

    # scroll the listbox vertically. 
    # to increase scrolling speed, either multiply counter by some value >1
    # or replace 'units' which means scroll 1 character in the current setting 
    # by 'pages' for larger steps. 'pages' should scroll the visible 
    # area of the listbox further.
    canvas.yview_scroll(-1, 'units')

def key(event):
    print("pressed", repr(event.char))
    
def callback(event):
    print("clicked at", event.x, event.y)
    
if __name__  == "__main__":
    root = tk.Tk()
    #menu = tk.Menu(root)
    root.title("Bot Docs B GUI Alpha- 001")
    root.geometry("500x500") 

    root.config(bg = "light grey")
    #root.config(menu = menu)
    
    #menu.add_cascade(label="Help")

    canvas = tk.Canvas(root, width=500, height=300,bg="white")
    canvas.bind("<Key>", key)
    canvas.bind("<B1-Motion>", mouse_move_callback)
    canvas.grid(row=0,column=0,columnspan=2)
    

    entry = tk.Entry(root,width=26)
    entry.grid(row=1,column=0)
    tk.Button(root,text="Send",command = lambda:[print_message("send", splitStringInLinesWithCharNum(entry.get(), 5)), print_message("recieved", splitStringInLinesWithCharNum(getResultFromServer(entry.get()), 10))]).grid(row=1,column=1)
    
    #print(splitStringInLinesWithCharNum("Hallo ich bin ein test. Den man mag.", 3))

    root.mainloop()