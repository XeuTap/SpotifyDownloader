from libs.pickleex import *

from PyQt5.QtWidgets import *
from GUI.delTrackDlg import *


class DelTrackDlg(QDialog, Ui_Dialog):
    def __init__(self, parent, playlistName):
        super().__init__()
        self.setupUi(self)
        self.playlistName = playlistName
        self.connectSignals()
        self._parent = parent
        self.setWindowTitle("Delete Track")

    def connectSignals(self):
        self.addButton.clicked.connect(self.onAddClicked)

    def onAddClicked(self):
        videoID = self.lineEdit.text()
        for track in self._parent.tracks:
            if int(videoID) == track.getTrackId():
                self.delTrack(track.getLink())
                break

    def delTrack(self, url):
        delete_from_file(self.playlistName, url=url)
