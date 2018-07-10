import tkinter # standard GUI library for Python
from user_name_entry import userNameEntryFrame

# Creates the main parent window, sets the title
root = tkinter.Tk()
root.title("Office Emergency Contact List Manager")

# Sets the initial size of the window for user name entry
w = 400
h = 50

# Gets screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# Calculates x and y coordinates for the root window so it's centered
center_x = (ws/2) - (w/2)
center_y = (hs/2) - (h/2)

# Sets the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, center_x, center_y))

# Displays the current user name entry frame
user_name_entry_frame = userNameEntryFrame(root)

root.mainloop()