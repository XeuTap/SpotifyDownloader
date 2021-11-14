import sys

import spotipy
from spotipy.exceptions import SpotifyException
from spotipy.oauth2 import SpotifyPKCE
import spotipy.util as util

from ysearcher import Ysearcher

TOKEN = None


def auth():
    global TOKEN
    _id = "58c4f04954df4b85836fab8a23197cd1"
    _auth = SpotifyPKCE(client_id=_id, redirect_uri='http://localhost:8080')
    try:
        TOKEN = _auth.get_access_token(check_cache=False)
    except spotipy.oauth2.SpotifyOauthError as error:
        validate_token = _auth.validate_token(TOKEN)
        print(validate_token)


def get_playlist(playlist_name):
    if TOKEN is None:
        auth()
    sp = spotipy.Spotify(auth=TOKEN)
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


def get_total(playlist_name):
    if TOKEN is None:
        auth()
    sp = spotipy.Spotify(auth=TOKEN)
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


def search(playlist_name):
    if TOKEN is None:
        auth()
    sp = spotipy.Spotify(auth=TOKEN)
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

        total = get_total(playlist_name)
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
    print(get_playlist('4Games'))
