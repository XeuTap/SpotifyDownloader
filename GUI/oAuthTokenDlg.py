
from PyQt5.QtWidgets import *
from GUI.addOAuthToken import *


class AddOAuthDlg(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connectSignals()
        self.setWindowTitle("Enter OAuth")
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def connectSignals(self):
        self.okButton.clicked.connect(self.onOkClicked)
        self.cancelButton.clicked.connect(self.onCancelClicked)

    def onOkClicked(self):
        self.accept()

    def onCancelClicked(self):
        self.close()

    def getToken(self):
        return self.lineEdit.text()
