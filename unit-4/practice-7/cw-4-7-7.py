"""
Author: Christine Wei
Date: May 1, 2023,
Description: GUI program that converts Celsius temperatures to Fahrenheit temperatures.
"""

import tkinter
import tkinter.messagebox


class TempGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Create the widgets for the top frame.
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a temperature in Celsius:')
        self.celsius_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets.
        self.prompt_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        # Create the button widgets for the bottom frame.
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.quit)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def convert(self):
        # Get the value entered by the user into the celsius_entry widget.
        celsius = float(self.celsius_entry.get())

        # Convert celsius to fahrenheit
        fahrenheit = celsius*(9/5) + 32

        # Display the results in an info dialogue box.
        tkinter.messagebox.showinfo("Results",
                                    f"Results: {str(celsius)} celsius is equal to {str(fahrenheit)} fahrenheit.")


def main():
    my_program = TempGUI()


main()
