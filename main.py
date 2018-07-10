import tkinter # standard GUI library for Python
from user_name_entry import userNameEntryFrame

# Creates the main parent window, sets the title
root = tkinter.Tk()
root.title("Office Emergency Contact List Manager")

# Displays the current user name entry frame
user_name_entry_frame = userNameEntryFrame(root)

# Gets the initial size of the window
w = root.winfo_reqwidth()
h = root.winfo_reqheight()

# Gets screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# Calculates x and y coordinates for the root window so it's centered
center_x = (ws/2) - (w/2)
center_y = (hs/2) - (h/2)

# Sets the window to be centered
root.geometry('+%d+%d' % (center_x, center_y))

root.mainloop()