from tkinter import *

from GUI.Content import Content

root = Tk()
content = Content(root)
root.wm_geometry('596x500')
root.title('SpotiParser')
root.wm_attributes()
root.resizable(False, False)


root.mainloop()