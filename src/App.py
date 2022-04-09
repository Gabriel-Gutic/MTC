import tkinter as tk

from Window import Window

class App:
    def __init__(self):
        self.window = Window(1280, 720)
    
    def run(self):
        self.window.mainloop()


app = App()
app.run()