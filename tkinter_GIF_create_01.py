from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from functools import partial

root = tk.Tk()
root.title("image resize")
root.geometry('220x50')

def GIFs():

    filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select Images", filetypes=filetypes)
    print("Selected images:")
    
    frames = []
    for filename in filenames:
        frame = Image.open(filename)
        frames.append(frame)

    frames[0].save('mygif.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)

buttonCal = tk.Button(root, text="Image_upload", width=10,command=GIFs).grid(row=3, column=0)
