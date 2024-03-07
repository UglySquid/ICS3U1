"""
Author: Christine Wei
Date: May 1, 2023,
Description: GUI that will allow Ms. Huynh to enter three test scores and calculate then display the average.
"""

import tkinter
import tkinter.messagebox


class AvgGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two frames to group widgets.
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()

        # Pack the frames.
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        # Create the widgets for the top frame.
        self.prompt1_label = tkinter.Label(self.frame1, text='Enter the score for test 1:')
        self.score1_entry = tkinter.Entry(self.frame1, width=10)

        self.prompt2_label = tkinter.Label(self.frame2, text='Enter the score for test 2:')
        self.score2_entry = tkinter.Entry(self.frame2, width=10)

        self.prompt3_label = tkinter.Label(self.frame3, text='Enter the score for test 3:')
        self.score3_entry = tkinter.Entry(self.frame3, width=10)

        # Pack the prompt and entry widgets.
        self.prompt1_label.pack(side='left')
        self.prompt2_label.pack(side='left')
        self.prompt3_label.pack(side='left')
        self.score1_entry.pack(side='left')
        self.score2_entry.pack(side='left')
        self.score3_entry.pack(side='left')

        # Create average label and pack it
        self.avg_label = tkinter.Label(self.frame4, text="Average: ")
        self.score_label = None
        self.avg_label.pack(side='left')

        # Create the button widgets.
        self.calc_button = tkinter.Button(self.frame5, text='Convert', command=self.calculate)
        self.quit_button = tkinter.Button(self.frame5, text='Quit', command=self.main_window.quit)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def calculate(self):
        # Get the three scores entered by Mrs. Huynh.
        score1 = float(self.score1_entry.get())
        score2 = float(self.score2_entry.get())
        score3 = float(self.score3_entry.get())

        # Calculate average
        average = (score1 + score2 + score3) / 3

        # Display the results
        self.score_label = tkinter.Label(self.frame4, text=str(average))
        self.score_label.pack(side='left')


def main():
    my_program = AvgGUI()


main()
