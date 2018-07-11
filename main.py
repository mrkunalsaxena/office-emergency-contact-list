import tkinter # standard GUI library for Python
from emergency_contact_menu import emerContactListFrame

# Creates the main parent window, sets the title
root = tkinter.Tk()
root.title("Office Emergency Contact List Manager")

# Displays the emergency contact menu frame
emer_contact_menu_frame = emerContactListFrame(root)

root.mainloop()