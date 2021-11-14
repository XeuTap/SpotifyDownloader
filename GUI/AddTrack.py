from tkinter import Toplevel, Button, Label, Entry
import _tkinter
from ysearcher import Ysearcher


class AddTrack(Toplevel):
    def __init__(self, master, parent):
        super().__init__(master)
        self.master = master
        self.parent = parent
        self.wm_geometry('100x200')
        self.width = '500'
        self.height = '200'
        self.overrideredirect(1)
        self.withdraw()

        self.add_b = Button(self)
        self.track_entry = Entry(self)
        self.add_info = Label(self)
        self.state = Label(self)
        self.setup()

    def setup(self):
        self.add_b.config(text='Add', command=self.add_track)
        self.track_entry.config()
        self.add_info.config(text='Enter track url(Youtube):')
        #new_track = Ysearcher(name='',) # Добавить метод возвращающий информацию о видео через ссылку(возможно придется костылить с python-youtube-searcher
        self.state.config(text='state')

        def placer():
            self.add_b.place(relx=.5, rely=.5)
            self.track_entry.place(relx=.2, rely=.35, relwidth=.6)
            self.add_info.place(relx=.4, rely=.2)
            self.state.place(relx=.6, rely=.5)

        placer()

    def place_self(self):
        try:
            self.overrideredirect(0)
            self.geometry(f'{self.width}x{self.height}+{self.master.winfo_rootx()}+{self.master.winfo_rooty()}')
            self.deiconify()
        except _tkinter.TclError as err:
            self.__init__(self.master, self.parent)
            self.place_self()

    def add_track(self):
        self.state.config(text='loading')