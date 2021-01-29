import tkinter as tk
import tkinter.ttk as ttk
import requests
import random
import urllib.request
import textstat
#from PIL import Image, ImageTk

#from LabelLink import Labellink


class App(ttk.Frame):
    #constructor
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.entry = tk.Entry(fg="black", bg ="white", width =100)
        self.entry.pack()
        # self.entry_text = 

        self.button_frame = ttk.Frame(self, padding = (0,20 , 0 , 0))
        self.button_frame.pack()
        self.button = ttk.Button(self.button_frame, text = 'Check', padding ='20 10',command=self.check_age_range)
        self.button.pack()

        self.age_range = tk.StringVar()
        self.age_range_label = ttk.Label(self, textvariable=self.age_range)
        self.age_range_label.pack()
        self.age_range.set('3-5')

    def check_age_range(self):
        entry_text = self.entry.get()
        
        grade = textstat.flesch_reading_ease(entry_text)
        self.age_range.set(grade)



def main():
    root = tk.Tk()
    root.title('Reading Age')
    root.iconphoto(False, tk.PhotoImage(file='book.png'))
    App(root, padding=20, width=800, height=500).pack()
    root.mainloop()


if __name__ == '__main__':
    main()