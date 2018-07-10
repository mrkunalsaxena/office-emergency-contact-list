import tkinter # standard GUI library for Python
from tkinter import messagebox
from emergency_contact_menu import emerContactListFrame

# Class for entering current user's name and storing it
# Used before actually viewing or modifying emergency contact list
class userNameEntryFrame(tkinter.Frame):
    # Constructor and initial attributes
    def __init__(self, parent = None):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.config(bd = 5)
        self.grid()
        self.make_widgets()

    # Used to display widgets
    def make_widgets(self):
        self.your_name_label = tkinter.Label(self, text = "Your Name:")
        self.your_name_label.grid(column = 0, row = 0, sticky = "W")

        self.your_name_entry = tkinter.Entry(self, bd = 5)
        self.your_name_entry.grid(column = 1, row = 0, sticky = "W")

        self.your_name_submit_button = tkinter.Button(self, text = "Submit", command = self.yourNameSubmitCallback)
        self.your_name_submit_button.grid(column = 2, row = 0, sticky = "W")

    # Callback for submit button
    # Moves onto the emergency contact menu if a name was entered
    def yourNameSubmitCallback(self):
        your_name = self.your_name_entry.get().strip()
        if your_name == "":
            self.your_name_error_submit = messagebox.showerror("Error: No name given", "Please enter your name.")
        else:
            self.pack_forget()
            self.destroy()
            emer_contact_menu_frame = emerContactListFrame(your_name, self.parent)


