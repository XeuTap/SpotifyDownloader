from PyQt5.QtWidgets import *
from GUI.addTrackDlg import Ui_addTrackDlg


class TrackDlg(QDialog):
    def __init__(self):
        super().__init__()
        self.addTrackDlg = Ui_addTrackDlg()
        self.addTrackDlg.setupUi(self)
