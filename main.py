import os.path

from PyQt5.QtWidgets import *
from libs.spotify import *
from libs.utils import read_dir
from libs.SpotifyOAuthException import SpotifyOAuthException
import webbrowser

from GUI.spotipyMain import Ui_MainWindow
from GUI.addPlaylist import PlaylistDlg
from GUI.playlistWidget import PlaylistWidget
from GUI.oAuthTokenDlg import AddOAuthDlg

SPOTIFY_OAUTH_URL = "https://developer.spotify.com/console/get-current-user-playlists/?limit=&offset="

sys.path.append(os.path.dirname(__file__))

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.playlistDlg = None
        self.spotifyOAuthDlg = None
        self.playlists = {}
        self.setupUi(self)
        self.connectSignals()
        self.loadPlaylists()
        self.setWindowTitle("Spotify Downloader")
        self.spotifyAuth = None

    def connectSignals(self):
        self.authorizeButton.clicked.connect(self.do_auth)
        self.addPlaylistButton.clicked.connect(self.addPlaylistDlg)

    def do_auth(self):
        try:
            webbrowser.open(SPOTIFY_OAUTH_URL)
            self.spotifyOAuthDlg = AddOAuthDlg()
            if self.spotifyOAuthDlg.exec_() == QDialog.Accepted:
                self.spotifyAuth = SpotifyAPI(self.spotifyOAuthDlg.getToken())
                self.authorizeButton.setText("Authorized")
        except SpotifyOAuthException:
            print('Wrong Token')
            self.authorizeButton.setText("Wrong Token")

    def addPlaylistDlg(self):
        if not self.spotifyAuth: self.do_auth()
        self.playlistDlg = PlaylistDlg(self.spotifyAuth)
        if self.playlistDlg.exec_() == QDialog.Rejected:
            if len(self.playlistDlg.lineEdit.text()) != 0:
                self.loadPlaylists()

    def addPlaylist(self, playlistName, _id):
        self.playlists[playlistName] = PlaylistWidget(self.scrollAreaWidgetContents, playlistName, _id=_id)
        self.verticalLayout_3.addWidget(self.playlists[playlistName])

    def loadPlaylists(self):
        """Подругажет сохраненные плейлисты в виджет"""
        _files = read_dir()  # Считываем сохраненные в директорию файлы
        for index, file in enumerate(_files):
            file_name = file.split('.')
            playlist_name = file_name[0]
            if self.playlists.get(playlist_name, 0) == 0:
                self.addPlaylist(playlist_name, index + 1)


if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec()
