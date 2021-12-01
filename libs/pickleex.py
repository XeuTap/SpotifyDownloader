import pickle
from io import BytesIO

import requests
from PIL import Image


def read_data(playlist_name):
    try:
        with open(f'data/{playlist_name}.data', 'rb') as pfile:
            while True:
                dumped = pickle.load(pfile)
                yield dumped
    except EOFError:
        print('End of file')
    except FileNotFoundError as err:
        print('No such name', err)


def append_to_file(playlist_name, _obj):
    try:
        print(playlist_name)
        with open(f'data/{playlist_name}.data', 'ab') as pfile:
            pickle.dump(_obj, pfile)
    except Exception as error:
        print(error)


def write_to_file(playlist_name, ls):
    try:
        print(playlist_name)
        with open(f'data/{playlist_name}.data', 'wb') as pfile:
            for _obj in ls:
                pickle.dump(_obj, pfile)
    except Exception as error:
        print(error)


def delete_from_file(playlist_name, _id=None, title=None, url=None, duration=None):
    readFile = read_data(playlist_name)
    listToWrite = []
    for _obj in readFile:
        if url is not None and _obj[0] == url:
            pass
        else:
            listToWrite.append(_obj)
    write_to_file(playlist_name, listToWrite)



# print(dumped.set_hello())
if __name__ == '__main__':
    # with open(f'a.data', 'wb') as file:
    #    response = requests.get('https://img.youtube.com/vi/2Eooc2A1l-0/default.jpg')
    #    image = Image.open(BytesIO(response.content))
    #    pickle.dump(image, file)
    with open(f'a.cfg', 'wb') as file:
        dic = {"123": 1, "2": 2}
        pickle.dump(dic, file)
    with open(f'a.cfg', 'rb') as file:
        dic2 = pickle.load(file)
        print(dic2)
