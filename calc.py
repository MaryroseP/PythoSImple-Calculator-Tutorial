import tkinter as tk
from constants import *


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")


        # Adding number displays (total and current operation)
        self.total_expression = "0"
        self.current_expression = "0"

        # Adding some display features and some buttons
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.buttons_frame = self.create_button_frame()
    
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=light_pink, fg = black, padx = 24, font = small_font)
        total_label.pack(expand=True, fill= 'both')
        
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                               bg=light_pink, fg = black, padx = 24, font = large_font)
        label.pack(expand=True, fill= 'both')
        return total_label, label
    

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=disp_h, bg=light_pink)
        frame.pack(expand=True, fill="both")
        return frame
    def create_button_frame(self):
        frame = tk.Frame(self.window, bg=dark_pink)
        frame.pack(expand=True, fill="both")
        return frame



    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
