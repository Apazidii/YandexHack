import datetime
import pytz
from Kostya.convert_time import time_to_text
from Kostya.get_db import get_data
def get_bridge(name):
    return {
        "name" : "Название",
        "fullname" : "моста Названия",
        "coord" : [42, 21],
        "time" : [["0:20", "1:00"], ["4:20", "5:10"]]
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



def get_phrase(name):
    global br_names
    bridge = get_data(br_names[name])
    tz = pytz.timezone("Europe/Moscow")
    time = datetime.datetime.now(tz = tz)
    time = datetime.timedelta(hours=time.hour, minutes=time.minute)
    return time_to_text(time, bridge["time"][0], 0, bridge["fullname"])


