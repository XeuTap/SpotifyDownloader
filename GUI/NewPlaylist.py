import _tkinter
from tkinter import Toplevel, Frame, Label, Entry, LEFT, N, Button, BOTTOM, S, StringVar

from PIL import Image, ImageTk

from utils import resource_path


class NewPlaylist(Toplevel):
    def __init__(self, master, parent):
        super().__init__()
        self.master = master
        self.overrideredirect(1)
        self.withdraw()
        self.parent = parent
        self.title('Add Playlist')
        self.width='500'
        self.height='200'
        self.wm_geometry('500x200')

        self.playlist_f = Frame(self)
        self.playlist_l = Label(self.playlist_f)
        self.playlist_e = Entry(self.playlist_f)



        self.finding_f = Frame(self)
        self.find_b = Button(self.finding_f, text='Find')
        image = Image.open(resource_path('resources/loading.jpg'))
        image = image.resize((15, 15), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)
        self.finding_img = Label(self.finding_f, image=self.image)
        self.finding_l = Label(self.finding_f, text='Finding')

        self.setup()

    def setup(self):
        def placer():

            self.playlist_f.pack(anchor=N)
            self.playlist_l.pack(side=LEFT)
            self.playlist_e.pack(side=LEFT)

            self.finding_f.pack(anchor=S, side=BOTTOM)
            self.find_b.pack(anchor=S, side=LEFT)

        self.playlist_l.configure(text="Playlist name")
        self.playlist = StringVar()
        self.playlist_e.configure(width=50, textvariable=self.playlist)

        self.finding_f.configure()
        self.finding_img.configure()
        self.finding_l.configure(text='Finding')

        self.find_b.configure(command=self.find_playlist)
        placer()
    
    def place_self(self):
        try:
            self.overrideredirect(0)
            self.geometry(f'{self.width}x{self.height}+{self.master.winfo_rootx()}+{self.master.winfo_rooty()}')
            self.deiconify()
        except _tkinter.TclError as err:
            self.__init__(self.master, self.parent)
            self.place_self()

    def find_playlist(self):
        """Оболочка для родительского метода find_playlist(PlaylistHolder)"""
        #self.finding_l.pack(side=RIGHT)
        self.finding_img.pack(side=LEFT)
        self.finding_l.pack(side=LEFT)
        self.update()
        self.parent.find_playlist(self.playlist.get())
        image = Image.open(resource_path('resources/sucess.jpg'))
        image = image.resize((15, 15), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(image)
        self.finding_img.configure(image=self.image)
        length = self.parent.playlists[self.playlist.get()].get_length()
        self.finding_l.configure(text=f'Found {length}')
        
    def change_text(self, txt):
        """Меняет статус"""
        self.finding_l.configure(text=txt)

