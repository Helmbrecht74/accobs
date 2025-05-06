#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 15:30:42 2025

@author: peter
"""

import tkinter as tk

app = tk.Tk()
app.title("GUI App")
app.geometry("320x240")

label = tk.Label(
    app,
    font=("Helvetica", 16, "bold"),
)
label.pack()

def callback(text):
    def closure():
        label.config(text=text)

    return closure

def set_label(text):
    label.config(text=text)
    
def set_label_default():
    label.config("Defaulttext")

button = tk.Button(
    app,
    text="Greet",
    command= set_label #callback("Hallo allseits!"),
)
button.pack()

app.mainloop()
