# pylint:disable=E0001
# pylint:disable=E0611
# pylint:disable=E0401
import platform
from tkinter import *

import youtube_dl
from PIL import Image

import os
from GUI.AddTrack import AddTrack
from GUI.Track import Track
from utils import del_symbols, read_data, load_cfg
from utils import resource_path
import time
import pprint
import pickle


class TracksHolder(Frame):
    def __init__(self, master, playlistname):
        self.playlistname = playlistname
        self.pseudo_master = Frame(master)  # Костыль сделанны для канваса, тк его нельзя лифтить
        self.canvas = Canvas(self.pseudo_master)
        self.settings = load_cfg()
        super().__init__(self.canvas)
        self.add_menu = AddTrack(self.master, self)
        self.master = master
        self.sub_height = self.master.winfo_rooty()
        self.identifier = int(time.time())

        self.tracks = []
        # self.tracks.append(Track(self, duration=132, title='UltraNumb', author='Blue Stahli'))
        self.menu = Frame(self.pseudo_master)
        self.download_b = Button(self.menu)
        self.add_track_b = Button(self.menu)
        self.open_folder_b = Button(self.menu)
        self.load_tracks(playlistname)
        self.scroll_bar = Scrollbar(self.pseudo_master)

        self.width = self.master.winfo_width() - self.scroll_bar.winfo_reqwidth() # Узнаем размер рут окна
        if platform.system() == "Linux":
            self.width = self.master.winfo_screenwidth() - self.scroll_bar.winfo_reqwidth()
        self.setup()

    def setup(self):
        self.download_b.config(text='Download All',
                               command=self.start_download,
                               fg='white',
                               bd=0,
                               highlightthickness=0,
                               bg='gray')
        self.add_track_b.config(text='Add track',
                                command=self.add_menu.place_self,
                                fg='white',
                                bd=0,
                                highlightthickness=0,
                                bg='gray')
        self.open_folder_b.config(text='Open Folder',
                                command=self.open_folder,
                                fg='white',
                                bd=0,
                                highlightthickness=0,
                                bg='gray')
        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.config(orient=VERTICAL, command=self.canvas.yview)


        def placer():
            self.add_track_b.pack(side=LEFT, padx=5)
            self.download_b.pack(side=LEFT)
            self.open_folder_b.pack(side=RIGHT)
            self.pseudo_master.pack(fill=BOTH, expand=True)
            self.menu.pack(side=TOP, fill=X)
            self.scroll_bar.pack(side=RIGHT, fill=Y)
            self.canvas.pack(fill=BOTH, expand=True)
            self.window = self.canvas.create_window((0, 0), window=self, anchor=NW, width=self.width)
            self.pseudo_master.pack_forget()

        def binder():
            self.canvas.bind('<Configure>', self.on_configure)

        placer()
        self.get_duration()
        binder()

    def open_folder(self):
        os.startfile(os.getcwd() + '/downloads/')

    def load_tracks(self, playlistname):
        self.settings = load_cfg()
        print('Loading Tracks')
        self.playlistname = playlistname
        tracks = read_data(playlistname)  # Обьект генератора содержащий списки данных о треках
        img = Image.open(resource_path('resources/play-button.png'))
        self.play_img = img.resize((35, 35), Image.ANTIALIAS)
        img = Image.open(resource_path('resources/fail.png'))
        self.del_img = img.resize((15, 15), Image.ANTIALIAS)
        for track in tracks:
            title = del_symbols(track[2])  # Убираем спец.символы
            ls = title.split('-')  # Отделяем автора от назвния трека
            author = ls[0]
            title = str(ls[1:len(ls)])
            title = title.strip("[']")
            self.tracks.append(
                Track(self, duration=track[1], title=title, author=author, image=track[3], href=track[0],
                      play_img=self.play_img, delete_img=self.del_img))
            if self.settings['save_logs'] == 1:
                try:
                    with open(f'{os.getcwd()}/logs/{self.identifier}.log', 'a', encoding='utf-8') as file:
                        pass
                except FileNotFoundError:
                    os.makedirs('logs')
                finally:
                    with open(f'{os.getcwd()}/logs/{self.identifier}.log', 'a', encoding='utf-8') as file:
                        file.write(f'{track[0]}, {track[1]}, {author + " - " + title}, {track[3]}\n')
        print('Tracks Loaded')

    def add_track(self, href, duration, title, image=None):
        try:
            self.settings = load_cfg()
            title = del_symbols(title)
            ls = title.split('-')
            author = ls[0]
            title = str(ls[1:len(ls)])
            title = title.strip("[']")
        except IndexError as err:
            print('An error ocured, skipping', err)
            return
        except ValueError as err:
            print("Title error", err)
        else:
            self.tracks.append(
                Track(self, duration=duration, title=title, author=author, image=image, href=href, play_img=self.play_img,
                      delete_img=self.del_img))
            if self.settings['save_logs'] == 1:
                try:
                    with open(f'{os.getcwd()}/logs/{self.identifier}.log', 'a', encoding='utf-8') as file:
                        pass
                except FileNotFoundError:
                    os.makedirs('logs')
                finally:
                    with open(f'{os.getcwd()}/logs/{self.identifier}.log', 'a', encoding='utf-8') as file:
                        file.write(f"{href}, {duration}, {author + ' - ' +title}, {image}\n")

    def del_track(self, title):
        ls = []
        with open(f'data/{self.playlistname}.data', 'wb') as file:
            for track in self.tracks:
                if track.title == title:
                    index = self.tracks.index(track) # Получаем позицию в списке
                    self.tracks[index].hide() # Прячем виджет дабы избежать повторного нажатия на кнопку удаления
                    self.tracks.pop(index-1) # Убираем элемнт из списка для коррентного отображения длины плейлиста
                    print('Deleted')
                else:
                    pickle.dump(track.get_to_dump(), file)  # Записываем новый список в файл

    def place_self(self):
        self.pseudo_master.pack(fill=BOTH, expand=True)
        self.pseudo_master.lift()
        self.scroll_bar.lift()
        self.scroll_bar.focus()
        self.master.update()
        self.master.update_idletasks()
        self.master.event_generate('<<AlwaysOnTop>>')  # Эвент для поднятия нижней панели

    def on_leaved(self, event):
        print("Canvas withdrawn")
        self.canvas.pack_forget()
        self.scroll_bar.pack_forget()
        self.master.update()
        self.master.update_idletasks()
        self.update_idletasks()
        self.canvas.update_idletasks()

    def on_configure(self, event=0):
        """Магическая функция для корректной работы скролл бара"""
        # update scrollregion after starting 'mainloop'
        # when all widgets are in canvas
        print('Configured')
        self.update_idletasks()
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def start_download(self):
        """Загрузка треков"""
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            if not len(self.tracks) == 0:
                for track in self.tracks:
                    try:
                        ydl.download([track.href])
                    except youtube_dl.utils.DownloadError as err:
                        print('Youtube internal error', err)
                        print('Trying again')
                        ydl.download([track.href])
            else:
                print("Empty Playlist")

    def get_length(self):
        return len(self.tracks)

    def get_duration(self):
        dur = 0
        for track in self.tracks:
            dur += track.duration
        mins = dur // 60
        hours = mins // 60
        secs = dur - mins * 60
        mins = mins - hours * 60
        valid_date = f'{hours}:{mins}:{secs}'
        return valid_date
