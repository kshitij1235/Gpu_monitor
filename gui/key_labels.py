
from tkinter import ttk
from utils.scan_stats import scan
from utils.settings import *

def key_labels_(root):
    
    ttk.Label(
        root,
        text="MONITOR",
        font=app_font,
        foreground="red",
        background="black").grid(row=1, column=1, sticky="nsew")
    ttk.Label(
        root,
        text=f'{scan().get_gpu_name()} : ',
        font=app_font,
        foreground="green",
        background="black",
    ).grid(row=3, column=1, sticky="nsew")
    ttk.Label(
        root,
        text='GPU LOADS : ',
        font=app_font,
        foreground="green",
        background="black",
    ).grid(row=4, column=1, sticky="nsew")
    ttk.Label(
        root,
        text='GPU MEMORY USED : ',
        font=app_font,
        foreground="green",
        background="black",
    ).grid(row=5, column=1, sticky="nsew")
