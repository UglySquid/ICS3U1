"""
Author: Christine Wei
Date: May 2, 2023,
Description:
GUI application that allows the user to select a rate category (from a set of Radio Buttons),
and enter an energy consumption value (in Watts) and time (in hours) into two Entry widgets.
When they click an “OK” button, a dialog box should display their total electricity cost.
"""

import tkinter
import tkinter.messagebox


class ElectricityGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()
        self.frame6 = tkinter.Frame()

        # Pack the frames.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
        self.frame6.pack()

        # Create the radio button widgets and IntVar object
        self.radio_peak = tkinter.IntVar()

        # Set the intVar object to 1, default
        self.radio_peak.set(1)

        # Create the Radiobutton widgets in the top_frame.
        self.rb1 = tkinter.Radiobutton(self.frame1, text='Off-Peak', variable=self.radio_peak, value=1)
        self.rb2 = tkinter.Radiobutton(self.frame2, text='Mid-Peak', variable=self.radio_peak, value=2)
        self.rb3 = tkinter.Radiobutton(self.frame3, text='On-Peak', variable=self.radio_peak, value=3)

        # Pack the Radio buttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create the entry widgets
        self.energy_consumption = tkinter.Label(self.frame4, text='Energy Consumption (Watts, Hours):')

        self.watts_label = tkinter.Label(self.frame5, text='Watts:')
        self.watts_entry = tkinter.Entry(self.frame5, width=10)
        self.time_label = tkinter.Label(self.frame5, text='Hours:')
        self.time_entry = tkinter.Entry(self.frame5, width=10)

        # Pack the entry widgets
        self.watts_label.pack(side='left')
        self.watts_entry.pack(side='left')
        self.time_label.pack(side='left')
        self.time_entry.pack(side='left')

        # Create the button widgets.
        self.calc_button = tkinter.Button(self.frame5, text='Convert', command=self.calculate)
        self.quit_button = tkinter.Button(self.frame5, text='Quit', command=self.main_window.quit)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def calculate(self):
        # Get the radio selection
        peak = self.radio_peak.get()

        # Get the watt and time entered
        watt = float(self.watts_entry.get())
        time = float(self.time_entry.get())

        # Calculate energy consumption
        if peak == 1:
            consumption = 0.051*time*watt
        elif peak == 2:
            consumption = 0.081*time*watt
        elif peak == 3:
            consumption = 0.099*time*watt

        # Display the results
        tkinter.messagebox.showinfo("Total Electricity Cost", f"Your Total Electricity Cost is {str(consumption)}")


def main():
    my_program = ElectricityGUI()


main()