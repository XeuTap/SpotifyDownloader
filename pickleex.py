import pickle
from io import BytesIO

import requests
from PIL import Image


def read_data(playlist_name):
    try:
        with open(f'GUI/{playlist_name}.data', 'rb') as pfile:
            while True:
                dumped = pickle.load(pfile)
                yield dumped
    except EOFError:
        print('End of file')
    except FileNotFoundError as err:
        print('No such name', err)


# print(dumped.set_hello())
if __name__ == '__main__':
    #with open(f'a.data', 'wb') as file:
    #    response = requests.get('https://img.youtube.com/vi/2Eooc2A1l-0/default.jpg')
    #    image = Image.open(BytesIO(response.content))
    #    pickle.dump(image, file)
    with open(f'a.cfg', 'wb') as file:
        dic = {"123": 1, "2": 2}
        pickle.dump(dic, file)
    with open(f'a.cfg', 'rb') as file:
        dic2 = pickle.load(file)
        print(dic2)
