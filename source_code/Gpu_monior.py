from tkinter import Label, Tk,Button
from tkinter import ttk
from tkinter.font import BOLD
from time import sleep
import threading
import sys
from GPUtil import getGPUs

def get_temps():
    gpus = getGPUs()
    for gpu in gpus:
        return f"{gpu.temperature} °C"

def get_gpu_name():
    gpus = getGPUs()
    for gpu in gpus:
        return gpu.name

def get_gpu_load():
    gpus = getGPUs()
    for gpu in gpus:
        return f"{int(gpu.load*100)}%"


def get_gpu_used_mem():
    gpus = getGPUs()
    for gpu in gpus:
        return f"{gpu.memoryUsed}MB/{gpu.memoryTotal} MB"


font_size=15



def core_1():
    while True:
        sleep(1)
        gpu_temp_lbl.config(text=get_temps())
        gpu_load_lbl.config(text=get_gpu_load())

def core_2():
    while True:
        sleep(1)
        gpu_mem_used_lbl.config(text=get_gpu_used_mem())
     
thread1=threading.Thread(target=core_1)
thread2=threading.Thread(target=core_2)

def hide():
    root.withdraw()
    
def unhide():
    print()
    root.deiconify()

def unlock():
    thread1.start()
    thread2.start()


root = Tk()
root.geometry("700x400")
root.config(bg="black")
root.attributes()
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", 'black')
root.overrideredirect(True)

ttk.Label(root,
    text="MONTIOR",
    font=("Helvetica",font_size, BOLD),
    foreground="red",
    background="black").grid(row=1, column=1, sticky="nsew")

ttk.Label(
    root,
    text=f'{get_gpu_name()} : ',
    font=("Helvetica",font_size, BOLD),
    foreground="green",
    background="black",
).grid(row=3, column=1, sticky="nsew")

ttk.Label(
    root,
    text='GPU LOADS : ',
    font=("Helvetica", font_size, BOLD),
    foreground="green",
    background="black",
).grid(row=4, column=1, sticky="nsew")

ttk.Label(
    root,
    text='GPU MEMORY USED : ',
    font=("Helvetica", font_size, BOLD),
    foreground="green",
    background="black",
).grid(row=5, column=1, sticky="nsew")


# +++++++++++++++++++++++++++++++++++

gpu_temp_lbl=Label(root,
    text=str(get_temps()),
    font=("Helvetica",font_size, BOLD),
    foreground="green",
    background="black")
gpu_temp_lbl.grid(row=3, column=2, sticky="nsew")

gpu_load_lbl=Label(root,
    text=str(get_gpu_load()),
    font=("Helvetica",font_size, BOLD),
    foreground="green",
    background="black")
gpu_load_lbl.grid(row=4, column=1)

gpu_mem_used_lbl=Label(root,
    text=str(get_gpu_load()),
    font=("Helvetica",font_size, BOLD),
    foreground="green",
    background="black")
gpu_mem_used_lbl.place(x=220,y=87)

unlock()

stop_button=Button(root,text="EXIT",border=0,bg="red",command=sys.exit)
stop_button.place(x=140,y=0)


# root.bind('<Control-Key-r>', lambda event: hide())
# root.bind('<Control-Key-plus>', lambda event: unhide())
root.mainloop()
