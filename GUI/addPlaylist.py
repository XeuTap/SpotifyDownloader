from libs.utils import read_dir, get_image
import pickle

from PyQt5.QtWidgets import *
from GUI.addPlaylistDlg import *


class PlaylistDlg(QDialog, Ui_Dialog):
    def __init__(self, spotifyAPI):
        super().__init__()
        self.setupUi(self)
        self.connectSignals()
        self.setWindowTitle("Add Playlist")
        self.spotifyAPI = spotifyAPI
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def connectSignals(self):
        self.addButton.clicked.connect(self.onAddClicked)

    def onAddClicked(self):
        playlistName = self.lineEdit.text()
        self.find_playlist(playlistName)

    def find_playlist(self, playlist_name):
        """Ищет плейлист в спотифае и парсит сохраняя его в файл с названием плейлиста"""
        count = 0
        playlist = self.spotifyAPI.get_playlist(playlist_name)  # Ищем плейлист
        _dir = read_dir()
        for file in _dir:
            if file.split(".")[0] == playlist_name:
                print("Playlist already in dir")
                break
        if playlist is not None:
            with open(f'data/{playlist_name}.data', 'wb') as file:  # Открываем файл для записи
                a = self.spotifyAPI.search(playlist_name)
                self.stateImage.setPixmap(QtGui.QPixmap(":/resources/resources/ic_autorenew_white_24dp.png"))
                for index, b in enumerate(a):
                    if b is None:
                        continue
                    print(b)
                    self.stateLabel.setText("Founded: " + str(index + 1))
                    self.update()
                    QApplication.processEvents()
                    count += 1
                    ls_args = []
                    for arg in b:  # Пересобираем аргументы, что бы подшить обьект Image вместо ссылки
                        ls_args.append(arg)
                    ls_args[3] = get_image(b[3])
                    pickle.dump(ls_args, file)  # Сохраняем список в файл
            self.stateImage.setPixmap(QtGui.QPixmap(":/resources/resources/ic_check_circle_white_24dp.png"))
            self.stateLabel.setText("Completed")
        else:
            self.stateImage.setPixmap(QtGui.QPixmap(":/resources/resources/ic_error_outline_white_24dp.png"))
            self.stateLabel.setText("Playlist not found")
