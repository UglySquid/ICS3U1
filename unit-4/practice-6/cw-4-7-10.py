import tkinter
import random


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        text_list = ["HI OMG HI", "Welcome!!!", "Welcome Ms. Huynh!"]

        random_text = random.choice(text_list)

        # Create two Label widget.
        self.label1 = tkinter.Label(self.main_window, text=random_text)

        # Call both Label widgets' pack method.
        self.label1.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()
        # Create an instance of the MyGUI class.
        my_gui = MyGUI()


def main():
    my_program = MyGUI()


main()
