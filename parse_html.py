from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


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


# Обрабатывает время
# разбиваея строку на массив подстрок по 4 символа
def strf(s):
    l = len(s)
    arr = []
    for i in range(0, l, 4):
        arr.append(s[i:i+4])
    return arr

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
        res.append(cl)

    return res



arr = parse_bridges()

# Функция конвертации класса в словарь
def f(k):
    return k.__dict__
# Конвертация массива классов в массив словарей
arr = list(map(f, arr))

# Создание Json и запись его в файл
j = json.dumps(arr, indent=4, ensure_ascii=False).encode("utf-8")
file = open("bridge.json", "w", encoding= "utf-8")
file.write(j.decode())