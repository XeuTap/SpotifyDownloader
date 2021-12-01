from libs.utils import load_cfg, read_data, fix_time

from PyQt5.QtWidgets import *
from GUI.spotipyPlaylistWidget import *
from GUI.spotipyPlaylist import PlaylistNonModalWidget


class PlaylistWidget(QWidget, Ui_Form):
    def __init__(self, parent, playlistName=None, _id=0):
        super().__init__(parent)
        self.setupUi(self)
        self.playlistNameLabel = self.label
        self.playlist = None
        self.id = _id
        if playlistName is not None:
            self.playlistName = playlistName
            self.playlistNameLabel.setText(playlistName)
        self._init()

    def _init(self):
        self.settings = load_cfg()
        print('Loading Tracks')
        tracks = read_data(self.playlistName)  # Обьект генератора содержащий списки данных о треках
        totalDuration = 0
        lastIndex = 0
        for index, track in enumerate(tracks):
            duration = track[1]
            totalDuration = totalDuration + duration
            lastIndex = index + 1
        self.playlistDuration = fix_time(totalDuration)
        self.label_5.setText(self.playlistDuration)
        self.label_4.setText(str(lastIndex))
        self.label_3.setText(str(self.id))

    def mousePressEvent(self, event):
        self.showPlaylistWidget()

    def showPlaylistWidget(self):
        print("Creating new window")
        self.playlist = PlaylistNonModalWidget(self.playlistName)
        self.playlist.loadTracks()
        self.playlist.run()
