"""
Author: Christine Wei
Date: May 3, 2023,
Description: Electronic Story Maker
"""

import tkinter
from tkinter import colorchooser
from tkinter.colorchooser import askcolor
import tkinter.font
import tkinter.messagebox
import tkinter.scrolledtext
import random


class StoryMaker:
    def __init__(self):
        # Create the main window widget.
        self.story_canvas = None
        self.root = tkinter.Tk()
        self.root.geometry("740x640")

        # Lets user choose colour
        self.colour = tkinter.colorchooser.askcolor(color=None)

        # Set Background Colour
        self.root.config(background=self.colour[1])

        # Create two frames to group widgets.
        self.frame1 = tkinter.Frame()
        self.frame2 = tkinter.Frame()
        self.frame3 = tkinter.Frame()
        self.frame4 = tkinter.Frame()
        self.frame5 = tkinter.Frame()
        self.frame6 = tkinter.Frame()
        self.frame7 = tkinter.Frame()
        self.frame8 = tkinter.Frame()
        self.story_label = None

        # Pack the frames.
        self.frame1.pack(anchor="w", padx="50", pady="10")
        self.frame2.pack(anchor="w", padx="50", pady="10")
        self.frame3.pack(anchor="w", padx="50", pady="10")
        self.frame4.pack(anchor="w", padx="50", pady="10")
        self.frame5.pack(anchor="w", padx="50", pady="10")
        self.frame6.pack(anchor="w", padx="50", pady="10")
        self.frame7.pack(anchor="w", padx="50", pady="10")
        self.frame8.pack(anchor="w", padx="50", pady="10")

        # Create prompt label
        self.prompt_label = tkinter.Label(self.frame1,
                                          text='Please enter information for a new story, '
                                               'then click the "Make Story" button.',
                                          font=('Calibri', 12))

        # Pack prompt label
        self.prompt_label.pack()

        # Create the entry widgets for Person, Plural Noun, and Verb
        self.person_label = tkinter.Label(self.frame2, text='Person        :')
        self.noun_label = tkinter.Label(self.frame3, text='Plural Noun:')
        self.verb_label = tkinter.Label(self.frame4, text='Verb           :')

        self.person_entry = tkinter.Entry(self.frame2, width=20)
        self.noun_entry = tkinter.Entry(self.frame3, width=20)
        self.verb_entry = tkinter.Entry(self.frame4, width=20)

        # Pack the entry widgets for Person, Plural Noun, and Verb
        self.person_label.pack(side='left')
        self.person_entry.pack(side='left')
        self.noun_label.pack(side='left')
        self.noun_entry.pack(side='left')
        self.verb_label.pack(side='left')
        self.verb_entry.pack(side='left')

        # Create three IntVar objects to use with the Check buttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        # Set the intVar objects to 0, by default not being selected.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        # Create the Checkbutton widgets for body part
        self.adjective_label = tkinter.Label(self.frame5, text='Adjective(s):')
        self.cb1 = tkinter.Checkbutton(self.frame5, text='wacky', variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.frame5, text='joyous', variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.frame5, text='electric', variable=self.cb_var3)

        # Pack the Radio buttons and its label
        self.adjective_label.pack(side='left')
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')

        # Create the radio button widgets and IntVar object
        self.body_radio = tkinter.IntVar()

        # Set the intVar object to 1, default
        self.body_radio.set(1)

        # Create the Radiobutton widgets for body part
        self.part_label = tkinter.Label(self.frame6, text='Body Part:')
        self.rb1 = tkinter.Radiobutton(self.frame6, text='forehead', variable=self.body_radio, value=1)
        self.rb2 = tkinter.Radiobutton(self.frame6, text='feet', variable=self.body_radio, value=2)
        self.rb3 = tkinter.Radiobutton(self.frame6, text='hands', variable=self.body_radio, value=3)

        # Pack the Radio buttons.
        self.part_label.pack(side='left')
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        self.rb3.pack(side='left')

        # Create the button widgets.
        self.make_button = tkinter.Button(self.frame7, text='Make Story!', command=self.make_story)
        self.quit_button = tkinter.Button(self.frame7, text='Quit', command=self.root.quit)
        self.color_button = tkinter.Button(self.frame7, text='Change Colour', command=self.change_color)
        self.refresh_button = tkinter.Button(self.frame7, text='New Story', command=self.refresh)

        # Pack the buttons.
        self.make_button.pack(side='left')
        self.refresh_button.pack(side='left')
        self.color_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Enter the tkinter main loop.
        tkinter.mainloop()

    def make_story(self):
        """
        Accepts: No arguments
        Description: This creates a story using the user's input and choices
        """

        # Get information
        person = self.person_entry.get()
        plural_noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        adjectives = []
        body_part = self.body_radio.get()

        # not_valid = True
        #
        # while not_valid:
        #     # Validate user input, if user input not valid user cannot continue
        #     if person == "":
        #         error_label = tkinter.Label(self.frame8, text="You must fill in a person!")
        #         error_label.pack()
        #         self.root.after(700, self.frame8.pack_forget)
        #         return
        #     if plural_noun == "":
        #         error_label = tkinter.Label(self.frame8, text="You must fill in a plural noun!")
        #         error_label.pack()
        #         self.root.after(700, self.frame8.pack_forget)
        #         return
        #     if verb == "":
        #         error_label = tkinter.Label(self.frame8, text="You must fill in a verb!")
        #         error_label.pack()
        #         self.root.after(700, self.frame8.pack_forget)
        #         return
        #
        #     if (self.cb_var1.get() == 0) and (self.cb_var2.get() == 0) and (self.cb_var3.get() == 0):
        #         error_label = tkinter.Label(self.frame8, text="You must choose an adjective!")
        #         error_label.pack()
        #         self.root.after(700, self.frame8.pack_forget)
        #         return

        # Check what choices the users chose
        if body_part == 1:
            body_part = "forehead"
        elif body_part == 2:
            body_part = "feet"
        elif body_part == 3:
            body_part = "hands"

        if self.cb_var1.get():
            adjectives.append("wacky")
        if self.cb_var2.get():
            adjectives.append("joyous")
        if self.cb_var3.get():
            adjectives.append("electric")

        if len(adjectives) == 0:
            adjectives.append("")

        # The story I have written
        my_story = f"One day, {person} was feeling particularly {random.choice(adjectives)}. \nThe sun was {random.choice(adjectives)}, and {person} had just finished reading their {random.choice(adjectives)} book. \n{person} closed their eyes, and leaned back, feeling {random.choice(adjectives)} and at ease. \nSuddenly, they heard a loud thud and felt something hit them on the {body_part}. \nOuch! {person} cried out, rubbing their {body_part}. \n{person} looked down and saw that some of their {plural_noun} had fallen off the shelf and hit them on the {body_part}. \n{person} picked up each of the {plural_noun} and examined it carefully, making sure the {plural_noun} weren't damaged. \nThen, an idea struck {person}. \nInstead of just having {plural_noun} sit on the shelf, why not {verb} with the {plural_noun}? {person} began to {verb} the {plural_noun}."

        # Typewriter effect that types out letter by letter animation
        self.story_canvas = tkinter.Canvas(self.frame8, width=700, height=250)
        self.story_canvas.pack()
        story_t = self.story_canvas.create_text(20, 20, text='', width=600, anchor="nw")
        delta = 70
        delay = 0

        for i in range(len(my_story) + 1):
            s = my_story[:i]
            new_text = lambda s=s: self.story_canvas.itemconfig(story_t, text=s)
            self.story_canvas.after(delay, new_text)
            delay += delta

        return True

    def change_color(self):
        """
        Accepts: No arguments
        Description: This function allows the user to choose a new background colour
        """

        colors = askcolor(title="Tkinter Color Chooser")
        self.root.configure(bg=colors[1])

    def refresh(self):
        """
        Accepts: No arguments
        Description: Clears all the entries and buttons, and the story so that user can enter new things.
        """
        # Remove texts entered by user
        self.person_entry.delete(0, 'end')
        self.noun_entry.delete(0, 'end')
        self.verb_entry.delete(0, 'end')

        # Deselect check buttons
        self.cb1.deselect()
        self.cb2.deselect()
        self.cb3.deselect()

        # Reset Radio Buttons
        self.body_radio.set(0)

        # Destroy generated story
        try:
            self.story_canvas.destroy()
        except AttributeError:
            return


def main():
    """Mainline logic"""

    # Creates GUI Application
    Story = StoryMaker()


# Run my GUI Story Maker program
main()
