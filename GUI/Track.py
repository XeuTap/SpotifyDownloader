import platform
import webbrowser
from tkinter import *

from PIL import Image, ImageTk


class Track(Frame):
    def __init__(self, master, image=None, title='Title', duration=123, author='Author', href=0, play_img=None,
                 delete_img=None):
        super().__init__(master)
        self.bg = '#d3d3d3'
        self.widget_height = 50
        if platform.system() == "Linux":
            self.widget_height = self.master.winfo_screenheight() // 10
        self.href = str(href)
        self.play_img = ImageTk.PhotoImage(play_img)
        self.delete_img = ImageTk.PhotoImage(delete_img)
        self.duration = duration
        self.image_raw = image
        self.image = self.image_init(image)
        self.title = title
        self.author = author

        self.title_l = Label(self, text=title)
        self.duration_l = Label(self, text=f'Duration: {self.format_duration()}')
        self.author_l = Label(self, text=author)
        self.play_b = Button(self)
        self.delete_b = Button(self)
        self.img_preview = Label(self)

        self.setup()

    def image_init(self, image):
        if image is None:
            image = Image.open('resources/blank.png')
            image = image.resize((self.widget_height, self.widget_height), Image.ANTIALIAS)
        else:
            image = image.resize((self.widget_height, self.widget_height), Image.ANTIALIAS)
        return ImageTk.PhotoImage(image)

    def hide(self):
        self.delete_b.config(state=DISABLED, command=0)
        self.play_b.config(state=DISABLED)
        self.delete_b.place_forget()
        self.master.update_idletasks()
        self.master.update()
        self.pack_forget()

    def get_to_dump(self):
        return self.href, self.duration, self.author + ' - ' + self.title, self.image_raw

    def format_duration(self):
        mins= self.duration // 60
        secs = self.duration - mins * 60
        if secs < 10:
            secs = '0' + str(secs)
        if mins >= 60:
            hours = mins // 60
            mins = mins - hours * 60
            return f'{hours}:{mins}:{secs}'
        else:
            return f'{mins}:{secs}'

    def open_in_browser(self, event=0):
        if not event == 0:
            webbrowser.open(self.href)
        else:
            print('Run only by Bind')

    def del_track(self):
        self.master.del_track(self.title)

    def setup(self):
        self.title_l.configure(font="Times 7", bg=self.bg, bd=0, pady=2)
        self.duration_l.configure(font="Times 7", bg=self.bg, bd=0, padx=10)
        self.author_l.configure(font="Times 7", padx=5, bg=self.bg, bd=0)
        self.play_b.configure(activebackground=self.bg, bg=self.bg,
                              image=self.play_img,
                              padx=10,
                              bd=0,
                              highlightthickness=0)
        self.delete_b.config(activebackground=self.bg,
                             bg=self.bg,
                             image=self.delete_img,
                             padx=10,
                             bd=0,
                             highlightthickness=0,
                             command=self.del_track)
        self.img_preview.config(image=self.image)
        self.configure(bg=self.bg, width=595, height=self.widget_height)

        def placer():
            self.pack(anchor=NW, fill=X)
            self.img_preview.place(relx=0, rely=0, relheight=1)
            self.play_b.place(relx=.85, rely=0, relheight=.8)
            self.author_l.place(relx=.15, rely=.5)
            self.duration_l.place(relx=.7, rely=.6, relheight=.3)
            self.title_l.place(relx=.25, relwidth=.5)
            self.delete_b.place(relx=.95, rely=0, relheight=.3)

        def binder():
            self.img_preview.bind('<Button-1>', self.open_in_browser)

        placer()
        binder()
