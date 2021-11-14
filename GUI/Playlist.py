import platform
from tkinter import Frame, Label, Button, NW, X, Menubutton, Menu

from PIL import ImageTk, Image

from GUI.TracksHolder import TracksHolder
from utils import resource_path

class Playlist(Frame):
    def __init__(self, master, root, image=None, title='Title', tracks='0', playlistname=''):
        super().__init__(master)
        self.bg = '#d3d3d3'
        self.widget_height = 50
        if platform.system() == "Linux":
            self.widget_height = self.master.winfo_screenheight() // 10
        self.configure(bg=self.bg, height=self.widget_height)
        self.pack(anchor=NW, fill=X)
        self.master = master.master
        # self.place(relx=0, rely=.3, relwidth=1, relheight=.3)
        if image is None:
            image = Image.open(resource_path('resources/blank.png'))
            image = image.resize((self.widget_height, self.widget_height), Image.ANTIALIAS)
        else:
            image = image.resize((self.widget_height, self.widget_height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image)
        self.logo = Label(self, image=self.img)
        self.title = Label(self, text=title)
        self.tracks_count = Label(self, text=f'Tracks: {tracks}')
        # self.author = Label(self, text='Author')
        # self.author.pack()
        self.tracks = TracksHolder(self.master, playlistname=playlistname)  # Фрейм с треками
        self.total_duration = Label(self, text=f'Время: {self.tracks.get_duration()}')
        self.set_len(self.get_length())

        self.settings_b = Menubutton(self) # Кнопка меню
        self.settings_menu = Menu(self.settings_b, tearoff=0) # Выпадающее меню
        self.setup()

    def force_update(self):
        print('Force updating')

    def setup(self):

        self.logo.configure(bg=self.bg)
        self.title.configure(bg=self.bg)
        self.tracks_count.configure(bg=self.bg)
        self.total_duration.config(bg=self.bg)
        image = Image.open(resource_path('resources/settings-button.png'))
        image = image.resize((self.widget_height // 3, self.widget_height // 3), Image.ANTIALIAS)
        self.set_img = ImageTk.PhotoImage(image)
        self.settings_b.config(bg=self.bg,
                               image=self.set_img,
                               bd=0,
                               highlightthickness=0,
                               activebackground=self.bg,)
        self.settings_menu.add_command(label='Force Update', command=self.force_update) # Строка для выпадающего меню
        self.settings_b['menu'] = self.settings_menu # Сделать кнопку активной
#command=self.settings_popup.show
        def packer():
            self.logo.place(relx=0, rely=0, relheigh=1)
            self.title.place(relx=.25, relwidth=.5)
            self.settings_b.place(relx=.95, rely=0)
            self.settings_menu.place()
            self.tracks_count.place(relx=.7, rely=.6, relheight=.3)
            self.total_duration.place()

        def binder():
            self.bind('<Button-1>', self.to_tracks)
            self.logo.bind('<Button-1>', self.to_tracks)
            self.title.bind('<Button-1>', self.to_tracks)
            self.tracks_count.bind('<Button-1>', self.to_tracks)
            self.total_duration.bind('<Button-1>', self.to_tracks)

        packer()
        binder()

    def to_tracks(self, event):
        """Отобразить треки"""
        self.tracks.place_self()

    def add_track(self, *args, **kwargs):
        self.tracks.add_track(*args)

    def get_length(self):
        return self.tracks.get_length()

    def set_len(self, len):
        self.tracks_count.config(text=f'Треков: {len}')
