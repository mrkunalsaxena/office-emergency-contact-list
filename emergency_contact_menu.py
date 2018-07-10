import tkinter # standard GUI library for Python

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
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Save as...")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command = self.winfo_toplevel().quit)

        self.winfo_toplevel().config(menu = self.menubar)

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

        self.user_name_add_submit_button = tkinter.Button(self, text = "Submit")
        self.user_name_add_submit_button.grid(row = 2, column = 2, padx = 5, sticky = "W")

        # Area for selecting a user and viewing their info
        self.select_user_label = tkinter.Label(self, text = "Select a user:")
        self.select_user_label.grid(row = 1, column = 4, sticky = "W")

        self.user_name_select_label = tkinter.Label(self, text = "User's Name:")
        self.user_name_select_label.grid(row = 2, column = 4, sticky = "W")

        self.user_name_select_entry = tkinter.Entry(self, bd = 5)
        self.user_name_select_entry.grid(row = 2, column = 5, sticky = "W")

        self.user_name_select_submit_button = tkinter.Button(self, text = "Submit")
        self.user_name_select_submit_button.grid(row = 2, column = 6, padx = 5, sticky = "W")

        # Gets the initial size of the window
        w = self.winfo_toplevel().winfo_reqwidth()
        h = self.winfo_toplevel().winfo_reqheight()

        # Gets screen width and height
        ws = self.winfo_toplevel().winfo_screenwidth()
        hs = self.winfo_toplevel().winfo_screenheight()

        # Calculates x and y coordinates for the root window so it's centered
        center_x = (ws/2) - (w/2)
        center_y = (hs/2) - (h/2)

        # Sets the window to be centered
        self.winfo_toplevel().geometry('+%d+%d' % (center_x, center_y))