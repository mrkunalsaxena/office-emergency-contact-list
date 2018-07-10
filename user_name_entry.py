import tkinter # standard GUI library for Python
from tkinter import messagebox

# Class for entering current user's name and storing it
# Used before actually viewing or modifying emergency contact list
class userNameEntryFrame(tkinter.Frame):
    def __init__(self, parent = None):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.config(bd = 5)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        self.your_name_label = tkinter.Label(self, text = "Your Name:")
        self.your_name_label.pack(side = tkinter.LEFT)

        self.your_name_entry = tkinter.Entry(self, bd = 5)
        self.your_name_entry.pack(side = tkinter.LEFT)

        self.your_name_submit_button = tkinter.Button(self, text = "Submit", command = self.yourNameSubmitCallback)
        self.your_name_submit_button.pack(side = tkinter.LEFT)

    def yourNameSubmitCallback(self):
        self.your_name = self.your_name_entry.get().strip()
        if self.your_name == "":
            self.your_name_error_submit = messagebox.showerror("Error: No name given", "Please enter your name.")
        

