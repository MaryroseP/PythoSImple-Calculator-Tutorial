import tkinter as tk
from constants import *


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        # Adding some display features and some buttons
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_button_frame()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=disp_h, bg=light_pink)
        frame.pack(expand=True, fill="both")
        return frame
    def create_button_frame(self):
        frame = tk.Frame(self.window, bg=but_color)
        frame.pack(expand=True, fill="both")
        return frame



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
