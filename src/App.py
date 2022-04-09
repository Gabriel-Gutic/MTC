import tkinter as tk


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=1280, height=720)
        self.canvas.grid(rowspan=3, columnspan=3)
    
    def run(self):
        self.window.mainloop()
        

app = App()
app.run()