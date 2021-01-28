import tkinter as tk
import tkinter.ttk as ttk
import requests
import random
import urllib.request
#from PIL import Image, ImageTk

#from LabelLink import Labellink 

class App(ttk.Frame):
    #constructor 
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        


def main():
    root = tk.Tk()
    root.title('Reading Age')
    App(root, padding=20, width=800, height=500).pack()
    root.mainloop()


if __name__ == '__main__':
    main()