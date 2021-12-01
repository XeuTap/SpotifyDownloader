import webbrowser
from PIL.ImageQt import ImageQt
from libs.utils import fix_time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from GUI.spotipyTrackWidget import *


class TrackWidget(QWidget, Ui_Form):
    def __init__(self, parent, _id=0, title="Error", author=None, duration=0, link="", image=None):
        super().__init__(parent)
        self.setupUi(self)
        self.updateWidget(title, author, duration, image, _id)
        self.link = link
        self.connectSignals()
        self.id = _id

    def updateWidget(self, title, author, duration, image, _id):
        if type(duration == int()):
            duration = fix_time(duration)
        self.trackName.setText(title)
        self.trackAuthor.setText(author)
        self.trackDuration.setText(duration)
        self.trackNo.setText(str(_id))
        im = image.convert("RGBA")
        qim = ImageQt(im)
        pixmap = QPixmap.fromImage(qim)
        self.trackImg.setPixmap(pixmap)

    def connectSignals(self):
        self.openInBrowser.clicked.connect(self.openLink)

    def getTrackId(self):
        return self.id

    def getLink(self):
        return self.link

    def openLink(self):
        webbrowser.open(self.link)
