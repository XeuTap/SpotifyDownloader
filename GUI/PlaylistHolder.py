# pylint:disable=E0401
# pylint:disable=E0611
import pickle
from tkinter import Frame, Button, TOP, NE, Toplevel

from GUI.NewPlaylist import NewPlaylist
from GUI.Playlist import Playlist
from spotify import search, get_total, get_playlist
from utils import read_dir, get_image


class PlaylistOptions(Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.wm_geometry('200x200')


class PlaylistHolder(Frame):
    def __init__(self, master, parent):
        super().__init__(master)
        self.master = master
        self.parent = parent
        self.new_playlist = NewPlaylist(self.master, self)
        self.add_b = Button(self)
        self.playlists = {} # Словарь плейлистов
        # self.playlists.append(Playlist(self, title='4Games', tracks=471))
        # self.playlists[0].pack()
        self.setup()

    def load_playlists(self):
        """Подругажет сохраненные плейлисты в виджет"""
        _files = read_dir() # Считываем сохраненные в директорию файлы
        for file in _files:
            file_name = file.split('.')
            playlist_name = file_name[0]
            self.playlists[playlist_name] = Playlist(self, self.master, title=f'{playlist_name}',
                                                     playlistname=playlist_name)  # Забиваем данными плейлисты
            self.playlists[playlist_name].pack()

    def setup(self):
        """Общая инициализация виджетов"""
        self.configure(bg='grey')
        self.add_b.config(text='Add Playlist', command=self.add_playlist)

        def placer():
            self.add_b.pack(side=TOP, anchor=NE)
        placer()
        self.load_playlists()

    def add_playlist(self):
        self.new_playlist.place_self()
        # self.new_playlist(self.master, self)

    def find_playlist(self, playlist_name):
        """Ищет плейлист в спотифае и парсит сохраняя его в файл с названием плейлиста"""
        count = 0
        playlist = get_playlist(playlist_name) # Ищем файл с одноименным названием
        if playlist is not None:
            self.playlists[playlist_name] = Playlist(self, self.master, title=playlist[0], tracks=0)
            self.playlists[playlist_name].pack()
        else:
            return 0
        with open(f'data/{playlist_name}.data', 'wb') as file: # Открываем файл для записи
            a = search(playlist_name)
            total = get_total(playlist_name) # Общее кол-во треков
            for b in a:
                if b is None:
                    continue
                print(b)
                count += 1
                self.new_playlist.change_text(f'{count}/{total}')
                self.update()
                ls_args = []
                for arg in b: # Пересобираем аргументы, что бы подшить обьект Image вместо ссылки
                    ls_args.append(arg)
                ls_args[3] = get_image(b[3])
                self.playlists[playlist_name].add_track(*ls_args) # Добавляем трек в виджет
                self.playlists[playlist_name].set_len(count) # Костыль прогресс_бара

                pickle.dump(ls_args, file) # Сохраняем список в файл

    def show_self(self):
        self.place(relx=0, rely=0, relheight=1, relwidth=1)
