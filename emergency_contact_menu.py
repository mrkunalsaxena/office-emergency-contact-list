import tkinter # standard GUI library for Python
from tkinter import filedialog
from tkinter import messagebox

# Class for viewing and modifying the emergency contact list
# Used after the current user has entered their name
class emerContactListFrame(tkinter.Frame):
    def __init__(self, your_name, parent = None):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.config(bd = 5)
        self.your_name = your_name
        self.grid()
        self.make_widgets()

    def make_widgets(self):

        # Adding a menu bar
        self.menubar = tkinter.Menu(self.winfo_toplevel())

        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = "File", menu= self.filemenu)
        self.filemenu.add_command(label = "New", command = self.fileNewCallback)
        self.filemenu.add_command(label = "Open", command = self.fileOpenCallback)
        self.filemenu.add_separator()
        self.filemenu.add_command(label = "Exit", command = self.winfo_toplevel().quit)

        self.winfo_toplevel().config(menu = self.menubar)

        # Welcome message for the current user
        self.welcome_label = tkinter.Label(self, text = "Welcome " + self.your_name + "\n")
        self.welcome_label.grid(row = 0, column = 0, sticky = "W")

        # Area for creating a new user and adding their info
        self.add_user_label = tkinter.Label(self, text = "Add a new user:")
        self.add_user_label.grid(row = 1, column = 0, sticky = "W")

        self.user_name_add_label = tkinter.Label(self, text = "User's Name:")
        self.user_name_add_label.grid(row = 2, column = 0, sticky = "W")

        self.user_name_add_entry = tkinter.Entry(self, bd = 5, state = tkinter.DISABLED)
        self.user_name_add_entry.grid(row = 2, column = 1, sticky = "W")

        self.user_name_add_submit_button = tkinter.Button(self, text = "Submit", state = tkinter.DISABLED, command = self.userNameAddSubmitCallback)
        self.user_name_add_submit_button.grid(row = 2, column = 2, padx = 5, sticky = "W")

        # Area for selecting a user and viewing their info
        self.select_user_label = tkinter.Label(self, text = "Select a user:")
        self.select_user_label.grid(row = 1, column = 4, sticky = "W")

        self.user_name_select_label = tkinter.Label(self, text = "User's Name:")
        self.user_name_select_label.grid(row = 2, column = 4, sticky = "W")

        self.user_name_select_listbox = tkinter.Listbox(self, bd = 5, state = tkinter.DISABLED)
        self.user_name_select_listbox.grid(row = 2, column = 5, sticky = "W")

        self.user_name_select_submit_button = tkinter.Button(self, text = "Submit", state = tkinter.DISABLED)
        self.user_name_select_submit_button.grid(row = 2, column = 6, padx = 5, sticky = "W")

    def fileNewCallback(self):
        self.csv_header = "Modified by,Employee name,Employee phone,Emergency contact name,Emergency contact phone\n"

        self.f = open("office_emergency_contact_list.csv", "w+")
        self.f.write(self.csv_header)
        self.f.close()

        self.user_name_add_entry.config(state = tkinter.NORMAL)
        self.user_name_add_submit_button.config(state = tkinter.NORMAL)

    def fileOpenCallback(self):
        ftypes = [('.csv files', '*.csv')]
        self.file_open_dialog = filedialog.Open(self, filetypes = ftypes)
        self.file_name_open = self.file_open_dialog.show()

        if self.file_name_open != "":
            print(self.file_name_open)
        
        self.user_name_add_entry.config(state = tkinter.NORMAL)
        self.user_name_add_submit_button.config(state = tkinter.NORMAL)
        self.user_name_select_listbox.config(state = tkinter.NORMAL)
        self.user_name_select_submit_button.config(state = tkinter.NORMAL)

    def userNameAddSubmitCallback(self):
        self.user_name_add = self.user_name_add_entry.get().strip()
        if self.user_name_add == "":
            self.user_name_add_error_submit = messagebox.showerror("Error: No name given", "Please enter the person's name.")
        else:
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
        if self.user_name_add_entry.get().strip() == "":
            self.user_name_add_error_submit = messagebox.showerror("Error: No name given", "Please enter the person's name.")
        elif self.user_phone_add_entry.get().strip() == "":
            self.user_phone_add_error_submit = messagebox.showerror("Error: No user phone given", "Please enter the person's phone number.")
        elif self.user_emer_name_add_entry.get().strip() == "":
            self.user_emer_name_add_error_submit = messagebox.showerror("Error: No emergency name given", "Please enter the emergency contact's name.")
        elif self.user_emer_phone_add_entry.get().strip() == "":
            self.user_emer_phone_add_error_submit = messagebox.showerror("Error: No emergency phone number given", "Please enter the emergency contact's phone number.")
        else:
            self.user_info_add_success_submit = messagebox.showinfo("Success", self.user_name_add_entry.get().strip() + "'s emergency contact info was successfully saved.")
            self.new_user_info = self.your_name + "," + self.user_name_add_entry.get().strip() + "," + self.user_phone_add_entry.get().strip() + "," + self.user_emer_name_add_entry.get().strip() + "," + self.user_emer_phone_add_entry.get().strip() + "\n"
            
            self.f = open("office_emergency_contact_list.csv", "a")
            self.f.write(self.new_user_info)
            self.f.close()
                                 