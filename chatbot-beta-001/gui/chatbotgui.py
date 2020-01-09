#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
from datetime import datetime

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
        tk.Label(self.frame, text = datetime.now().strftime("%d.%m.%Y %H:%m"),font = ("Helvetica", 7),bg="light grey").grid(row=0,column=0,sticky="w",padx=5)
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
 
if __name__  == "__main__":
    root = tk.Tk()
    root.title("Bot Docs B GUI Alpha- 001")
    root.geometry("500x500") 

    root.config(bg="light grey")

    canvas = tk.Canvas(root, width=500, height=300,bg="white")
    canvas.grid(row=0,column=0,columnspan=2)

    entry = tk.Entry(root,width=26)
    entry.grid(row=1,column=0)
    tk.Button(root,text="Send",command = lambda:[print_message("send", entry.get())]).grid(row=1,column=1)

    root.mainloop()