from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pandas as pd
import uuid


class Bridge:

    # Времена начала/прекращения водного и назменого транспорта
    stop_land_trans     = []
    stop_water_trans    = []
    start_land_trans    = []
    start_water_trans   = []

    # Название моста
    name = "nu tipa most"

    # Название реки
    river = "reka"

    # Сслыка на сайт моста
    link = "gg"

    id = 0

# Возвращает уникальный id для моста
def get_random_id():
    return str(uuid.uuid4())

# Обрабатывает время
# разбиваея строку на массив подстрок по 4 символа
def strf(s):
    l = len(s)
    arr = []
    for i in range(0, l, 4):
        arr.append(s[i:i+4])
    return arr


def razbiv_bridge(bridge):
    res = []
    l = len(bridge.stop_water_trans)
    for i in range(0, l):
        a = Bridge()
        a.name = bridge.name
        a.river = bridge.river
        a.id = bridge.id
        a.link = bridge.link
        a.stop_water_trans = bridge.stop_water_trans[i]
        a.stop_land_trans = bridge.stop_land_trans[i]
        a.start_water_trans = bridge.start_water_trans[i]
        a.start_land_trans = bridge.start_land_trans[i]
        res.append(a)
    return res

def parse_bridges():
    # Скачивание сайта
    html = urlopen("https://mostotrest-spb.ru/razvodka-mostov").read().decode('utf-8')

    # Конвертация страницы в класс bs4
    soup = BeautifulSoup(html, 'html.parser')

    # Выборка только таблицы
    bridge = soup.find('tbody')
    bridge = soup.find_all("td")

    # Удаление всего лишнего (названия столбцов и мосты без расписания)
    for i in range(0, 6):
        bridge.pop(0)
    for i in range(0, 9):
        bridge.pop(-1)


    # Заполнение классов мостов
    res = []
    l = len(bridge)
    for i in range(0, l, 6):
        cl = Bridge()
        cl.name = bridge[i + 0].text
        cl.link = bridge[i + 0].find("a").get("href")
        cl.river = bridge[i + 1].text
        cl.stop_land_trans = strf(bridge[i + 2].text)
        cl.start_water_trans = strf(bridge[i + 3].text)
        cl.stop_water_trans = strf(bridge[i + 4].text)
        cl.start_land_trans = strf(bridge[i + 5].text)
        cl.id = get_random_id()
        res.append(cl)

    return res



arr = parse_bridges()

# Функция конвертации класса в словарь
def f(k):
    return k.__dict__

def cat_list(arr):
    l = len(arr)
    for i in range(1, l-1):
        arr[0] = arr[0] + arr[i]
    return arr[0]

# Конвертация массива классов в массив словарей

arr = list(map(razbiv_bridge, arr))



arr = cat_list(arr)
arr = list(map(f, arr))
# Создание Json и запись его в файл

j = json.dumps(arr, indent=4,ensure_ascii=False).encode("utf-8")
file = open("bridge.json", "w", encoding= "utf-8")
file.write(j.decode())
file.close()

df = pd.read_json (r'bridge.json')
df.to_csv (r'bridge.csv', index = None)

# read_file = pd.read_csv (r'bridge.csv')
# read_file.to_excel (r'bridge.xlsx', index = None, header=True)
# file.close()