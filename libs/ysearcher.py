from youtubesearchpython import SearchVideos
import pprint
from libs.TimeConverter import TimeConverter


def sortcloser(ls, val, index=0):
    def sorter(i):
        if type(i) == type(tuple()):
            if i[index] > val:
                return i[index] - val
            else:
                return val - i[index]
        else:
            if i > val:
                return i - val
            else:
                return val - i

    return sorted(ls, key=sorter)


class Ysearcher:
    def __init__(self, name="None", duration=0, max_results=20, mode="dict"):
        self.duration = duration
        self.name = name
        self.pretify = pprint.PrettyPrinter()
        self.max_results = max_results
        self.mode = mode

    def search(self):
        search = SearchVideos(self.name, max_results=20, mode="dict")
        result = search.result()["search_result"]
        tconverter = TimeConverter()
        dic = [(item["link"], tconverter.convertosec(item["duration"]), item["title"], item['thumbnails'][0]) for item
               in result if not item['duration'] == 'LIVE']
        closedur = sortcloser(dic, self.duration, index=1)  # Sorted by closer duration
        for i in range(0, 19):
            item = closedur[i]
            if "instrumental" in item[2].lower() and "instrumental".lower() in self.name:
                answ = closedur[i]
                break
            elif "live" in item[2].lower() and "live" in self.name.lower():
                answ = closedur[i]
                break
            elif "cover" in item[2].lower() and "cover" in self.name.lower():
                answ = closedur[i]
                break
            elif "remix" in item[2].lower() and "remix" in self.name.lower():
                answ = closedur[i]
                break
            elif 'alternate version' in item[2].lower() and 'alternate version' in self.name.lower():
                answ = closedur[i]
                break
            elif 'mix' in item[2].lower() and 'mix' in self.name.lower():
                answ = closedur[i]
                break
            elif 'single version' in item[2].lower() and 'single version' in self.name.lower():
                answ = closedur[i]
                break
            elif 'mashup' in item[2].lower() and 'mashup' in self.name.lower():
                answ = closedur[i]
                break
            elif 'club' in item[2].lower() and 'club' in self.name.lower():
                answ = closedur[i]
                break
            elif 'reaction' in item[2].lower() and 'reaction' in self.name.lower():
                answ = closedur[i]
                break
            elif 'karaoke version' in item[2].lower() and 'karaoke version' in self.name.lower():
                answ = closedur[i]
                break
            elif 'old version' in item[2].lower() and 'old version' in self.name.lower():
                answ = closedur[i]
                break
            elif 'react' in item[2].lower() and 'react' in self.name.lower():
                answ = closedur[i]
                break
            elif 'reacts' in item[2].lower() and 'reacts' in self.name.lower():
                answ = closedur[i]
                break
            elif 'cover' in item[2].lower() or ("live" in item[2].lower()
                                                or 'amv' in item[2].lower()
                                                or '8d audio' in item[2].lower()
                                                or 'remix' in item[2].lower()
                                                or '12d audio' in item[2].lower()
                                                or "instrumental" in item[2].lower()
                                                or "alternate version" in item[2].lower()
                                                or "single version" in item[2].lower()
                                                or "mashup" in item[2].lower()
                                                or "club" in item[2].lower()
                                                or "reaction" in item[2].lower()
                                                or "karaoke version" in item[2].lower()
                                                or "old version" in item[2].lower()
                                                or "react" in item[2].lower()
                                                or "reacts" in item[2].lower()):
                pass
            elif len(item[2].split('-')) == 1:
                pass
            else:
                answ = closedur[i]
                break
        else:
            answ = None
        print(answ[2])
        return answ


if __name__ == "__main__":
    searcher = Ysearcher("Blue Stahli - Ultranumb", duration=260)
    track = searcher.search()
    print(track)
