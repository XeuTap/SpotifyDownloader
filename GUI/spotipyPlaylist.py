from libs.utils import del_symbols, read_data, load_cfg
import threading
import os
import subprocess
from libs.downloadTask import downloadTask
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QMutex
from GUI.spotipyPlaylistDlg import *
from GUI.spotipyTrack import TrackWidget
from GUI.addTrack import TrackDlg
from GUI.delTrack import DelTrackDlg


class PlaylistNonModalWidget(QDialog, Ui_Dialog):
    def __init__(self, playlistName):
        super().__init__()
        self.tracks = []
        self.threads = []
        self.trackDlg = None
        self.settings = load_cfg()
        self.setupUi(self)
        self.playlistName = playlistName
        self.setWindowTitle(self.playlistName)
        self.pushButtons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4]
        self.progressBar.hide()
        # self.setWindowModality(Qt.ApplicationModal)
        self.connectSignals()

    def connectSignals(self):
        self.pushButton.clicked.connect(self.addTrackSignal)
        self.pushButton_2.clicked.connect(self.downloadAll)
        self.pushButton_4.clicked.connect(self.openDir)
        self.pushButton_3.clicked.connect(self.deleteTrack)

    def addTrackSignal(self):
        self.trackDlg = TrackDlg(self.playlistName)
        if self.trackDlg.exec_() == QDialog.Rejected:
            if len(self.trackDlg.lineEdit.text()) != 0:
                self.clearLayout()
                self.loadTracks()

    def addTrack(self, title, author, duration, image, href, _id=0):
        pass
        track = TrackWidget(self.scrollAreaWidgetContents, title=title, author=author, duration=duration, link=href,
                            image=image, _id=_id)
        self.verticalLayout_2.addWidget(track)
        self.tracks.append(track)
        return track

    def clearLayout(self):
        while self.verticalLayout_2.count():
            child = self.verticalLayout_2.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def deleteTrack(self):
        self.trackDlg = DelTrackDlg(self, self.playlistName)
        if self.trackDlg.exec_() == QDialog.Rejected:
            if len(self.trackDlg.lineEdit.text()) != 0:
                self.clearLayout()
                self.loadTracks()

    def disableAllButtons(self):
        for button in self.pushButtons:
            button.setEnabled(False)

    def enableAllButtons(self):
        for button in self.pushButtons:
            button.setEnabled(True)

    def loadTracks(self):
        self.tracks.clear()
        print('Loading Tracks')
        tracks = read_data(self.playlistName)  # Обьект генератора содержащий списки данных о треках
        for index, track in enumerate(tracks):
            title = del_symbols(track[2])  # Убираем спец.символы
            ls = title.split('-')  # Отделяем автора от назвния трека
            author = ls[0]
            title = str(ls[1:len(ls)])
            title = title.strip("[']")
            duration = track[1]
            image = track[3]
            href = track[0]
            self.addTrack(title, author, duration, image, href, _id=index + 1)
            # if self.settings['save_logs'] == 1:
            #    try:
            #        with open(f'{os.getcwd()}/logs/{self.identifier}.log', 'a', encoding='utf-8') as file:
            #            pass
            #    except FileNotFoundError:
            #        os.makedirs('logs')
            #    finally:
            #        with open(f'{os.getcwd()}/logs/{self.identifier}.log', 'a', encoding='utf-8') as file:
            #            file.write(f'{track[0]}, {track[1]}, {author + " - " + title}, {track[3]}\n')

    def openDir(self):
        partialPath = r"\downloads\{0}".format(self.playlistName)
        fullPath = os.getcwd() + partialPath
        try:
            os.startfile(fullPath)
        except FileNotFoundError:
            print("Directory not found, trying to create")
            os.mkdir(fullPath)
            self.openDir()
        except Exception:
            subprocess.Popen(['xdg-open', fullPath])

    def downloadAll(self):
        print("Starting download")
        """Загрузка треков"""
        # print("downloads/{0}".format(self.playlistName))
        self.threads = []
        self.workers = []
        THREADS_NUMS = 8
        if len(self.tracks) < THREADS_NUMS:
            THREADS_NUMS = len(self.tracks)
        self.disableAllButtons()

        threadedList = createThreadedList(THREADS_NUMS, self.tracks)
        self.activeThreadsCount = THREADS_NUMS

        self.configureProgressBar(0, len(self.tracks), 0)
        self.progressBar.show()
        self.mutex = QMutex()

        for threadNumber in range(0, THREADS_NUMS):
            self.worker = Worker(self.playlistName, threadedList[threadNumber], self.increaseProgress, self.mutex)
            self.workers.append(self.worker)
            self.thread = QThread()
            self.threads.append(self.thread)
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.finished.connect(self.threadFinished)
            self.thread.start()

    def run(self):
        self.exec()

    def threadFinished(self):
        self.activeThreadsCount = self.activeThreadsCount - 1
        if self.activeThreadsCount == 0:
            print("ALL THREADS HAVE DONE")
            self.enableAllButtons()

    def configureProgressBar(self, _min, _max, current):
        self.progressBar.setMinimum(_min)
        self.progressBar.setMaximum(_max)
        self.progressBar.setValue(current)

    def increaseProgress(self):
        value = self.progressBar.value()
        print(value)
        self.progressBar.setValue(int(value) + 1)
        #self.update()
        QApplication.processEvents()


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, playlistName, argList, callback, qmutex):
        super().__init__()
        self.playlistName = playlistName
        self.argList = argList
        self.callback = callback
        self.mutex = qmutex

    def run(self):
        generator = downloadTask(self.playlistName, self.argList, lock=self.mutex)
        for _ in generator:
            self.mutex.lock()
            self.callback()
            self.mutex.unlock()
        self.finished.emit()

    pass

def createThreadedList(threadsAmount, tracks):
    threadedList = []
    start = 0
    step = len(tracks) // threadsAmount
    end = step
    for i in range(1, threadsAmount + 1):
        if i == threadsAmount:
            threadedList.append(tracks[start:])
        else:
            threadedList.append(tracks[start:end])
        start = start + step
        end = end + step
        if end >= len(tracks):
            end = len(tracks) - 1
    return threadedList
