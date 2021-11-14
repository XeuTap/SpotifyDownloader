import pickle
import os
import time
import requests
from PIL import Image, ImageTk
from io import BytesIO
import sys


def closer(i):
    if i > 10:
        return i - 10
    else:
        return 10 - i


def del_symbols(_str):
    """Функция для удаления спец.символов юникода неподдерживаемых UTF-8"""
    char_list = [_str[j] for j in range(len(_str)) if ord(_str[j]) in range(65536)]
    result = ''
    for j in char_list:
        result = result + j
    return result


def read_data(playlist_name):
    """Считываем построчно данные с файла(Предполагается что файл содержит списки)"""
    try:
        with open(f'data/{playlist_name}.data', 'rb') as file:
            while True:
                dumped = pickle.load(file)
                yield dumped
    except EOFError as err:
        print('End')
    except FileNotFoundError as err:
        print('No such name', err)


def read_dir():
    """Проверяем директорию data"""
    try:
        path = f'{os.getcwd()}/data'
        with os.scandir(path) as listOfEntries:
            for entry in listOfEntries:
                if entry.is_file():
                    yield entry.name
    except FileNotFoundError:
        print('No Such Directory')
        os.makedirs(f'{os.getcwd()}/data')


def save_cfg(dic):
    path = os.getcwd()
    with open(f'{path}/settings.cfg', 'wb') as file:
        pickle.dump(dic, file)
        return True


def load_cfg() -> dict:
    """Возвращает словрь с настройками"""
    try:
        path = os.getcwd()
        with open(f'{path}/settings.cfg', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError as err:
        print('Config not found, creating the default one')
        create_cfg()
        load_cfg()


def create_cfg():
    """Создает конфигурационный файл settings.cfg со значениями по умолчанию"""
    path = os.getcwd()
    dic={
        'save_logs' : 0,
    }
    with open(f'{path}/settings.cfg', 'wb') as file:
        pickle.dump(dic, file)
        return True


def get_image(url) -> Image:
    """Возвращает Image обьект из ссылки на картинку"""
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def limit_text_perline(text, symb_per_line=0):
    if symb_per_line == 0:
        symb_per_line = 21
    correct_line = ''
    temp = ''
    end_line_chars = ', .!'
    num_lines = 0
    for iter in range(0, len(text)):
        temp += text[iter]
        if len(temp) % symb_per_line == 0 and not iter == len(text) - 1:
            if text[iter + 1] in end_line_chars or text[iter] in end_line_chars:
                correct_line += temp + '\n'
                num_lines += 1
                temp = ''
            # elif ss[iter-1] in end_line_chars:
            #    correct_line += temp + '\n'
            elif text[iter - 1] in end_line_chars:
                correct_line += temp[0:len(temp) - 1] + '\n'
                num_lines += 1
                temp = text[iter]
            else:
                correct_line += temp + '-' + '\n'
                num_lines += 1
                temp = ''
    else:
        correct_line += temp + '\n'
        num_lines += 1
    return correct_line, num_lines


if __name__ == '__main__':
    a = read_dir()
    ls = []
    for x in range(0, 100000):
        t1 = time.time()
        ls.append(x)
        t2 = time.time()
        print(t2 - t1)
