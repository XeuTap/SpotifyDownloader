import sys
import spotipy
from spotipy.exceptions import SpotifyException
from libs.ysearcher import Ysearcher
from libs.SpotifyOAuthException import SpotifyOAuthException


class SpotifyAPI:
    def __init__(self, key):
        self.token = key
        try:
            sp = spotipy.Spotify(auth=self.token)
            user = sp.current_user()
        except Exception as error:
            raise SpotifyOAuthException

    def get_playlist(self, playlist_name):
        sp = spotipy.Spotify(auth=self.token)
        try:
            user = sp.current_user()
            user_playlist = sp.user_playlists(user=user['id'])
            playlist_list = user_playlist["items"]
            for playlist in playlist_list:
                if playlist['name'] == playlist_name:
                    return playlist['name'], playlist['tracks']['total'],
            else:
                return None
        except Exception as err:
            print('Cant get playlist ', err)

    def get_total(self, playlist_name):
        sp = spotipy.Spotify(auth=self.token)
        try:
            user = sp.current_user()
            user_playlist = sp.user_playlists(user=user['id'])
            playlist_list = user_playlist["items"]
            for playlist in playlist_list:
                if playlist['name'] == playlist_name:
                    return playlist['tracks']['total']
                else:
                    pass
            print('Not found')
        except Exception as err:
            print('Exc', err)

    def search(self, playlist_name):
        sp = spotipy.Spotify(auth=self.token)
        print("Sucessfuly auth")
        try:
            user = sp.current_user()
            user_playlist = sp.user_playlists(user=user['id'])
            playlist_list = user_playlist["items"]  # Getting list of playlist

            for _id in playlist_list:
                if _id['name'] == playlist_name:
                    playlist_id = _id['id']
                    print('Found')
                    break
                else:
                    pass
            else:
                print('Cant find a playlist')
                return None

            total = self.get_total(playlist_name)
            for x in range(0, (total // 100) + 1):
                lim = 100
                if total - x * 100 < 100:
                    lim = total - x * 100
                tracks = sp.user_playlist_tracks(playlist_id=playlist_id, limit=lim, offset=0 + x * 100)  # 0+x*100

                for i in range(0, 100):
                    track = tracks["items"][i]
                    artist = track["track"]["album"]["artists"][0]["name"]
                    track_name = track["track"]["name"]
                    to_search = f"{artist} - {track_name}"
                    duration = int(track["track"]["duration_ms"]) // 1000
                    searcher = Ysearcher(name=to_search, duration=duration)
                    yield searcher.search()
        except SpotifyException:
            print("No such user")
        except Exception as err:
            print("Exc       ", sys.exc_info()[0], err)


if __name__ == '__main__':
    pass
