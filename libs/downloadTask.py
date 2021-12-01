import youtube_dl
import os
import sys


def downloadTask(playlistName, tracksList, recursionCircle=None, lock=None):
    if recursionCircle is None:
        recursionCircle = 0
    linkList = None
    if lock:
        lock.lock()
        linkList = readDownloadInfo(playlistName)
        lock.unlock()
    skippedList = []
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/{0}/%(title)s.%(ext)s'.format(playlistName),
        "nooverwrites": True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if not len(tracksList) == 0:
            for track in tracksList:
                if linkList:
                    if track.link in linkList:
                        yield 1
                        continue
                try:
                    ydl.download([track.link])
                    appendDownloadInfo(playlistName, track.link)
                    yield 1
                except youtube_dl.utils.DownloadError as err:
                    print('Youtube internal error')
                    print(err)
                    if err.exc_info[0] == youtube_dl.utils.ExtractorError:
                        print(err.exc_info)
                    else:
                        print('Trying again')
                        skippedList.append(track)
                except youtube_dl.utils.UnavailableVideoError as error:
                    print("Video can't be downloaded")
                except Exception as error:
                    print("Some awful happened")
                    skippedList.append(track)
        else:
            print("Empty Playlist")
            return
        if recursionCircle >= 10:
            print("Recursion depth exceeded, quitting")
            return
        print(skippedList)
        print(recursionCircle)
        if len(skippedList) > 0:
            yield from downloadTask(playlistName, list(skippedList), recursionCircle=recursionCircle+1, lock=lock)


def readDownloadInfo(playlistName):
    fileName = "downloads.txt"
    path = f"downloads/{playlistName}/"
    linkList = []
    try:
        with open(path + fileName, "r") as file:
            for line in file.readlines():
                line = line[:-1]
                linkList.append(line)
            return linkList
    except FileNotFoundError:
        print("Info file not founded, creating an empty file")
        os.makedirs(path, 0o755)
        with open(path + fileName, "x") as file:
            pass


def appendDownloadInfo(playlistName, line, lock=None):
    fileName = "downloads.txt"
    path = f"downloads/{playlistName}/"
    try:
        with open(path + fileName, "a") as file:
            file.write(line+"\n")
    except FileNotFoundError:
        print("Info file not founded, creating an empty file")
        os.makedirs(path, 0o755)
        with open(path + fileName, "x") as file:
            pass
        appendDownloadInfo(playlistName, line)
