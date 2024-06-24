from utils.settings import *

def app_configure_(root):
    root.title(app__name)
    root.geometry("700x400")
    root.config(bg="black")
    root.attributes('-topmost', True)
    root.wm_attributes("-transparentcolor", 'black')
    root.overrideredirect(True)