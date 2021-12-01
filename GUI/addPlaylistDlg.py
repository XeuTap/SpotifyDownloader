# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPlaylistDlg.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(460, 130)
        Dialog.setStyleSheet("*{\n"
"background-color: #181818;\n"
"}\n"
".QLabel{\n"
"color:#929292;\n"
"background-color: transparent;\n"
"}\n"
".QPushButton{\n"
"color:#929292;\n"
"background-color: #282828;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: white;\n"
"}\n"
".QLineEdit{\n"
"color:#929292;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(50, 0, 50, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.frame = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setMinimumSize(QtCore.QSize(50, 0))
        self.addButton.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.stateImage = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stateImage.sizePolicy().hasHeightForWidth())
        self.stateImage.setSizePolicy(sizePolicy)
        self.stateImage.setMinimumSize(QtCore.QSize(20, 20))
        self.stateImage.setMaximumSize(QtCore.QSize(20, 20))
        self.stateImage.setText("")
        self.stateImage.setPixmap(QtGui.QPixmap(":/resources/resources/ic_check_circle_white_24dp.png"))
        self.stateImage.setScaledContents(True)
        self.stateImage.setObjectName("stateImage")
        self.horizontalLayout_2.addWidget(self.stateImage)
        self.stateLabel = QtWidgets.QLabel(self.frame_4)
        self.stateLabel.setMinimumSize(QtCore.QSize(50, 0))
        self.stateLabel.setMaximumSize(QtCore.QSize(500, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stateLabel.setFont(font)
        self.stateLabel.setText("")
        self.stateLabel.setScaledContents(False)
        self.stateLabel.setWordWrap(False)
        self.stateLabel.setObjectName("stateLabel")
        self.horizontalLayout_2.addWidget(self.stateLabel)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Spotify Playlist Name:"))
        self.addButton.setText(_translate("Dialog", "Add"))
import spotipy_resources_rc