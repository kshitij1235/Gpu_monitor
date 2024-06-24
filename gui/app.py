import threading
from tkinter import *
from tkinter import ttk
from utils.scan_stats import scan  # Assuming scan().get_detail() retrieves GPU details
from tkinter.font import BOLD
from utils.settings import *
from gui.app_configure import app_configure_
from gui.key_labels import *
from gui.gpu_stats import *
class Gui:
    def __init__(self, root):
        self.root = root
        
        app_configure_(self.root)
        key_labels_(self.root)

        gpt_status_(self)

        stop_button = Button(root, text="EXIT", border=0, bg="red", command=root.destroy)
        stop_button.place(x=140, y=0)

        self.gpu_monitor = threading.Thread(target=self.update_gpu_detail)
        self.gpu_monitor.start()

    def update_gpu_detail(self):
        while True:
            gpu = scan().get_detail()
            self.root.after(1000, self.update_gpu_temp, gpu.temperature)
            self.root.after(1000, self.update_gpu_load, gpu.load)
            self.root.after(1000, self.update_gpu_mem_used, gpu.memoryUsed, gpu.memoryTotal)

    def update_gpu_temp(self, temperature):
        self.gpu_temp_var.set(f"{temperature} °C")

    def update_gpu_load(self, load):
        self.gpu_load_var.set(f"{int(load * 100)}%")

    def update_gpu_mem_used(self, used, total):
        self.gpu_mem_used_var.set(f"{used} MB / {total} MB")

def start():
    root = Tk()
    app = Gui(root)
    root.mainloop()
