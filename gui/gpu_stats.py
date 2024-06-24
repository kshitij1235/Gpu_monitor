
from tkinter import StringVar,Label
from utils.settings import *

def gpt_status_(self):
    self.gpu_temp_var = StringVar()
    self.gpu_temp_lbl = Label(
            self.root,
            textvariable=self.gpu_temp_var,
            font=app_font,
            foreground="green",
            background="black")
    self.gpu_temp_lbl.grid(row=3, column=2, sticky="nsew")

    self.gpu_load_var = StringVar()
    self.gpu_load_lbl = Label(
        self.root,
        textvariable=self.gpu_load_var,
        font=app_font,
        foreground="green",
        background="black")
    self.gpu_load_lbl.grid(row=4, column=2, sticky="nsew")
    self.gpu_mem_used_var = StringVar()
    self.gpu_mem_used_lbl = Label(
        self.root,
        textvariable=self.gpu_mem_used_var,
        font=app_font,
        foreground="green",
        background="black")
    self.gpu_mem_used_lbl.grid(row=5, column=2, sticky="nsew")
