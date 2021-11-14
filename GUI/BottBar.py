from tkinter import Button, Frame


class BottBar(Frame):
    def __init__(self, master, parent):
        super().__init__(master)
        self.master = master
        self.parent = parent

        self.home_b = Button(self)
        self.playlists_b = Button(self)
        self.settings_b = Button(self)

        self.setup()

    def setup(self):
        self.home_b.configure(text='Home', highlightthickness=0, bd=0, command=self.parent.show_home)
        self.playlists_b.configure(text='Playlists', highlightthickness=0, bd=0, command=self.parent.show_playlist)
        self.settings_b.configure(text='Settings', highlightthickness=0, bd=0, command=self.parent.show_settings)

        def placer():
            self.home_b.place(relx=0, rely=0, relheight=1, relwidth=.33)
            self.playlists_b.place(relx=.33, rely=0, relheight=1, relwidth=.34)
            self.settings_b.place(relx=.67, rely=0, relheight=1, relwidth=.33)
            self.place(relx=0, rely=0.92, relwidth=1, relheight=.1)

        placer()
