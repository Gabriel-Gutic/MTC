import tkinter as tk
import zipfile
import io
from PIL import Image, ImageTk

from ReadTexture import read_default_texture

class Window(tk.Tk):
    def __init__(self, width, height):
        super(Window, self).__init__()
        self.title("MTC")
        self.geometry("1280x720")
        
        self.items_panel = tk.PanedWindow(bg="black", orient=tk.VERTICAL,)
        self.items_panel.pack(fill=tk.BOTH, expand=1)
        self.items_panel_canvas = tk.Canvas(self.items_panel) 
        self.scrollbar = tk.Scrollbar(self.items_panel, orient=tk.VERTICAL, command=self.items_panel_canvas.yview)
        
        self.items_panel_label = tk.Label(self.items_panel, text="Items", bd=4)
        self.items_panel.add(self.items_panel_label)
        
        path = 'data/Default 1.18.zip'
        archive = zipfile.ZipFile(path, 'r')
        images = read_default_texture(path)
        i = 0
        for image in images:
            i += 1
            if i  == 6:
                break
            imgdata = io.BytesIO(archive.read(image))
            img = Image.open(imgdata).resize((20, 20), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            img_label = tk.Label(master=self.items_panel, image=img)
            img_label.image = img
            self.items_panel.add(img_label)
            