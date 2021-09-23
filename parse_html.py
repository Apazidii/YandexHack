from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pandas as pd
import uuid


class Bridge:
    # Времена начала/прекращения водного и назменого транспорта
    stop_land_trans = []
    stop_water_trans = []
    start_land_trans = []
    start_water_trans = []

    # Название моста
    name = "nu tipa most"
    fullname = "most nu tipa most"

    # Название реки
    river = "reka"

    # Сслыка на сайт моста
    link = "gg"

    # уникальный индентификатор
    id = 0

    # Местоположение
    location = []


# Возвращает уникальный id для моста
def get_random_id() -> str:
    return str(uuid.uuid4())


# Обрабатывает время
# разбиваея строку на массив подстрок по 4 символа
def strf(s) -> list:
    arr = []
    while (":" in s):
        k = s.find(":")
        arr.append(s[:k + 3])
        s = s[k + 3:]
    return arr


loc = {
    "Володарский": [[59.877646, 30.453283], "Володарского моста"],
    "Александра Невского": [[59.925655, 30.395755], "моста Александра Невского"],
    "Большеохтинский": [[59.942620, 30.401585], "Большеохтинского моста"],
    "Литейный": [[59.951776, 30.349582], "Литейного моста"],
    "Троицкий": [[59.948767, 30.327582], "Троицкого моста"],
    "Дворцовый": [[59.941213, 30.308170], "Дворцового моста"],
    "Благовещенский": [[59.934691, 30.289538], "Благовещенского моста"],
    "Биржевой": [[59.946270, 30.303489], "Биржевого моста"],
    "Тучков": [[59.949038, 30.285449], "Тучкова моста"],
    "Сампсониевский": [[59.957958, 30.337383], "Сампсониевского моста"],
    "Гренадерский": [[59.967917, 30.334661], "Гренадерского моста"],
    "Кантемировский": [[59.978489, 30.321815], "Кантемировского моста"]
}


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
        a.location = bridge.location
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
        cl.location = loc[cl.name][0]
        cl.fullname = loc[cl.name][1]
        res.append(cl)

    cl = Bridge()
    cl.name = "Сампсониевский"
    cl.link = "/bridges/sampsonievskij"
    cl.river = "Большая Невка"
    cl.stop_land_trans = "NULL"
    cl.start_water_trans = "NULL"
    cl.stop_water_trans = "NULL"
    cl.start_land_trans = "NULL"
    cl.id = get_random_id()
    cl.location = loc[cl.name][0]
    cl.fullname = loc[cl.name][1]
    res.append(cl)

    cl = Bridge()
    cl.name = "Гренадерский"
    cl.link = "/bridges/kantemirovskij"
    cl.river = "Большая Невка"
    cl.stop_land_trans = "NULL"
    cl.start_water_trans = "NULL"
    cl.stop_water_trans = "NULL"
    cl.start_land_trans = "NULL"
    cl.id = get_random_id()
    cl.location = loc[cl.name][0]
    cl.fullname = loc[cl.name][1]
    res.append(cl)

    cl = Bridge()
    cl.name = "Гренадерский"
    cl.link = "/bridges/grenaderskij"
    cl.river = "Большая Невка"
    cl.stop_land_trans = "NULL"
    cl.start_water_trans = "NULL"
    cl.stop_water_trans = "NULL"
    cl.start_land_trans = "NULL"
    cl.id = get_random_id()
    cl.location = loc[cl.name][0]
    cl.fullname = loc[cl.name][1]
    res.append(cl)

    return res


arr = parse_bridges()


# Функция конвертации класса в словарь
def f(k):
    return k.__dict__


def cat_list(arr):
    l = len(arr)
    for i in range(1, l - 1):
        arr[0] = arr[0] + arr[i]
    return arr[0]


# Конвертация массива классов в массив словарей
# arr = list(map(razbiv_bridge, arr))
# arr = cat_list(arr)
arr = list(map(f, arr))

# Создание Json и запись его в файл

j = json.dumps(arr, indent=4, ensure_ascii=False).encode("utf-8")
file = open("data/bridge.json", "w", encoding="utf-8")
file.write(j.decode())
file.close()

df = pd.read_json(r'data/bridge.json')
df.to_csv(r'data/bridge.csv', index=None)

read_file = pd.read_csv(r'data/bridge.csv')
read_file.to_excel(r'data/bridge.xlsx', index=None, header=True)
file.close()
