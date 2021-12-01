from libs.utils import get_image
from youtubesearchpython import Video, ResultMode
from libs.TimeConverter import TimeConverter
from libs.pickleex import *

from PyQt5.QtWidgets import *
from GUI.addTrackDlg import *


class TrackDlg(QDialog, Ui_addTrackDlg):
    def __init__(self, playlistName):
        super().__init__()
        self.setupUi(self)
        self.playlistName = playlistName
        self.connectSignals()
        self.setWindowTitle("Add Track")

    def connectSignals(self):
        self.addButton.clicked.connect(self.onAddClicked)

    def onAddClicked(self):
        videoUrl = self.lineEdit.text()
        self.addTrack(videoUrl)

    def addTrack(self, url):
        try:
            videoInfo = Video.get(url, mode=ResultMode.json)
            result = [videoInfo['link']]
            durationDict: dict = videoInfo["duration"]
            result.append(TimeConverter.convertosec(TimeConverter(), durationDict["secondsText"]))
            result.append(videoInfo['title'])
            imageUrl: dict = dict(videoInfo['thumbnails'][0])
            result.append(get_image(imageUrl["url"]))
            append_to_file(self.playlistName, result)
        except Exception as error:
            print(error)
