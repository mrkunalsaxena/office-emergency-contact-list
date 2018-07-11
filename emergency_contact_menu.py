import tkinter # standard GUI library for Python
from tkinter import messagebox
import re
import sqlite3

# Class for viewing and modifying the emergency contact list
# Used after the current user has entered their name
class emerContactListFrame(tkinter.Frame):
    def __init__(self, your_name, parent = None):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.config(bd = 5)
        self.your_name = your_name
        self.conn = sqlite3.connect("emergency_contacts.db")
        self.c = self.conn.cursor()
        self.users = []
        self.grid()
        self.make_widgets()
        

    def make_widgets(self):

        # Welcome message for the current user
        self.welcome_label = tkinter.Label(self, text = "Welcome " + self.your_name + "\n")
        self.welcome_label.grid(row = 0, column = 0, sticky = "W")

        # Area for creating a new user and adding their info
        self.add_user_label = tkinter.Label(self, text = "Add a new user:")
        self.add_user_label.grid(row = 1, column = 0, sticky = "W")

        self.user_name_add_label = tkinter.Label(self, text = "User's Name:")
        self.user_name_add_label.grid(row = 2, column = 0, sticky = "W")

        self.user_name_add_entry = tkinter.Entry(self, bd = 5)
        self.user_name_add_entry.grid(row = 2, column = 1, sticky = "W")

        self.user_name_add_submit_button = tkinter.Button(self, text = "Submit", command = self.userNameAddSubmitCallback)
        self.user_name_add_submit_button.grid(row = 2, column = 2, padx = 5, sticky = "W")

        # Area for selecting a user and viewing their info
        self.select_user_label = tkinter.Label(self, text = "Select a user:")
        self.select_user_label.grid(row = 1, column = 4, sticky = "W")

        self.user_name_select_label = tkinter.Label(self, text = "User's Name:")
        self.user_name_select_label.grid(row = 2, column = 4, sticky = "W")

        self.user_name_select_listbox = tkinter.Listbox(self, bd = 5)
        self.user_name_select_listbox.grid(row = 2, column = 5, sticky = "W")
        
        # Gets employees that already exist in database
        self.c.execute("SELECT employee_name FROM emergency_contacts")
        self.users = self.c.fetchall()
        for user in self.users:
            user = "".join(user)
            self.user_name_select_listbox.insert(tkinter.END, user)

        self.user_name_select_submit_button = tkinter.Button(self, text = "Submit", command = self.userNameSelectSubmitCallback)
        self.user_name_select_submit_button.grid(row = 2, column = 6, padx = 5, sticky = "W")

    def userNameAddSubmitCallback(self):
        # Makes sure that a name has been entered
        self.user_name_add = self.user_name_add_entry.get().strip()
        if self.user_name_add == "":
            self.user_name_add_error_submit = messagebox.showerror("Error: No name given", "Please enter the person's name.")
        else:
            # Displays entry boxes for the rest of the needed information
            self.user_name_add_submit_button.config(state = tkinter.DISABLED)
            self.user_phone_add_label = tkinter.Label(self, text = "User's Phone #:")
            self.user_phone_add_label.grid(row = 3, column = 0, sticky = "W")

            self.user_phone_add_entry = tkinter.Entry(self, bd = 5)
            self.user_phone_add_entry.grid(row = 3, column = 1, sticky = "W")

            self.user_emer_name_add_label = tkinter.Label(self, text = "Emergency Contact Name:")
            self.user_emer_name_add_label.grid(row = 4, column = 0, sticky = "W")

            self.user_emer_name_add_entry = tkinter.Entry(self, bd = 5)
            self.user_emer_name_add_entry.grid(row = 4, column = 1, sticky = "W")

            self.user_emer_phone_add_label = tkinter.Label(self, text = "Emergency Contact Phone #:")
            self.user_emer_phone_add_label.grid(row = 5, column = 0, sticky = "W")

            self.user_emer_phone_add_entry = tkinter.Entry(self, bd = 5)
            self.user_emer_phone_add_entry.grid(row = 5, column = 1, sticky = "W")

            self.user_info_add_submit_button = tkinter.Button(self, text = "Submit", command = self.userInfoAddSubmitCallback)
            self.user_info_add_submit_button.grid(row = 6, column = 1, sticky = "E")

    def userInfoAddSubmitCallback(self):
        # Make sure that all fields have an input
        if self.user_name_add_entry.get().strip() == "":
            self.user_name_add_error_submit = messagebox.showerror("Error: No name given", "Please enter the person's name.")
        elif self.user_phone_add_entry.get().strip() == "":
            self.user_phone_add_error_submit = messagebox.showerror("Error: No user phone given", "Please enter the person's phone number.")
        elif self.user_emer_name_add_entry.get().strip() == "":
            self.user_emer_name_add_error_submit = messagebox.showerror("Error: No emergency name given", "Please enter the emergency contact's name.")
        elif self.user_emer_phone_add_entry.get().strip() == "":
            self.user_emer_phone_add_error_submit = messagebox.showerror("Error: No emergency phone number given", "Please enter the emergency contact's phone number.")
        else:
            # Writes the user emergency contact info to the database
            self.c.execute("INSERT INTO emergency_contacts VALUES(?, ?, ?, ?)", (self.user_name_add_entry.get().strip(), self.user_phone_add_entry.get().strip(), self.user_emer_name_add_entry.get().strip(), self.user_emer_phone_add_entry.get().strip()))
            self.conn.commit()
            self.user_info_success_submit = messagebox.showinfo("Success", self.user_name_add_entry.get().strip() + "'s emergency contact information was saved.")

            # Rest of needed information is not needed anymore
            self.user_phone_add_label.destroy()
            self.user_phone_add_entry.destroy()
            self.user_emer_name_add_label.destroy()
            self.user_emer_name_add_entry.destroy()
            self.user_emer_phone_add_label.destroy()
            self.user_emer_phone_add_entry.destroy()
            self.user_info_add_submit_button.destroy()

            # Adds newly added user to the user selection listbox
            self.user_name_select_listbox.insert(tkinter.END, self.user_name_add_entry.get().strip())

            # Re-enables add new user submit button for adding new users
            self.user_name_add_submit_button.config(state = tkinter.NORMAL)

    def userNameSelectSubmitCallback(self):
        # Gets the user's selection from the listbox
        self.user_selection = self.user_name_select_listbox.get(self.user_name_select_listbox.curselection()[0])
        
        # Forms the key to retrieve the corresponding emergency information
        (key1, key2) = re.split(": ", self.user_selection)


        
