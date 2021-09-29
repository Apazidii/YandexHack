import datetime
import pytz
from Kostya.convert_time import time_to_text
from Kostya.get_db import get_data
def get_bridge(name):
    return {
        "name" : "Название",
        "fullname" : "моста Названия",
        "coord" : [42, 21],
        "time" : [["0:20", "1:00"], ["4:20", "5:10"], ["6:13", "8:21"]]
    }
br_names = {
    'blagbridge': 'Благовещенский',
    'troibridge': 'Троицкий',
    'birbridge': 'Биржевой',
    'castlebridge': 'Дворцовый',
    'grenbridge': 'Гренадерский',
    'cloudbridge': 'Тучков',
    'volbridge': 'Володарский',
    'sampbridge': 'Сампсониевский',
    'kantbridge': 'Кантемировский',
    'nevskiibridge': 'Александра Невского',
    'bigbridge': 'Большеохтинский',
    'litbridge': 'Литейный',
    'Благовещенский' : 'Благовещенский',
    'Троицкий' : 'Троицкий',
    'Биржевой' : 'Биржевой',
    'Дворцовый' : 'Дворцовый',
    'Гренадерский' : 'Гренадерский',
    'Тучков' : 'Тучков',
    'Володарский' : 'Володарский',
    'Сампсониевский' : 'Сампсониевский',
    'Кантемировский' : 'Кантемировский',
    'Александра Невского' : 'Александра Невского',
    'Большеохтинский' : 'Большеохтинский',
    'Литейный' : 'Литейный'
}

def catarr(arr):
    l = len(arr)
    for i in range(1, l):
        arr[0] = arr[0] + arr[i]
    return arr[0]

def near_time(tall, now):
    time = catarr(tall)
    l = len(time)
    min = 86400
    minind = -1
    for i in range(0, l):
        t = datetime.timedelta(hours=int(time[i][:time[i].find(":")]), minutes=int(time[i][time[i].find(":") + 1:]))
        ts = (t - now).total_seconds()
        if ts < min and ts > 0:
            min = ts
            minind = i
    if minind == -1:
        return (tall[0], 0)
    return (tall[int(minind / 2)], minind % 2)


def get_phrase(name):
    global br_names
    bridge = get_data(br_names[name])
    tz = pytz.timezone("Europe/Moscow")
    time = datetime.datetime.now(tz = tz)
    time = datetime.timedelta(hours=time.hour, minutes=time.minute)
    # time = datetime.timedelta(hours=3, minutes=50)
    t, ra = near_time(bridge["time"], time)
    return (time_to_text(time, t, ra, bridge["fullname"]), ra)


