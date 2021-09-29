import requests
import json
import math

apikey_geocode = "c2b0fa0a-360d-4bc4-95d5-29c8273f2bfb"
apikey_organizations = "c1d3c70e-4972-4140-9b6d-d0adfe75f2b4"
lower_corner = "29.391159," + "59.667464"
upper_corner = "30.940276," + "60.149092"

bridges = [
    {
        "name": "Володарский",
        "pos": [30.452669, 59.877590]
    },
    {
        "name": "Александра Невского",
        "pos": [30.39536476135254, 59.92558288574219]
    },
    {
        "name": "Литейный",
        "pos": [30.349868774414062, 59.95296096801758]
    },
    {
        "name": "Троицкий",
        "pos": [30.327347, 59.948891]
    },
    {
        "name": "Дворцовый",
        "pos": [30.308170, 59.941250]
    },
    {
        "name": "Благовещенский",
        "pos": [30.2895547, 59.9347886]
    },
    {
        "name": "Биржевой",
        "pos": [30.3033726, 59.9462816]
    },
    {
        "name": "Тучков",
        "pos": [30.285506, 59.9489495]
    },
    {
        "name": "Сампсониевский",
        "pos": [30.3373158, 59.9579616]
    },
    {
        "name": "Гренадерский",
        "pos": [30.3346052, 59.9679575]
    },
    {
        "name": "Большеохтинский",
        "pos": [30.404556274414062, 59.9426155090332]
    },
    {
        "name": "Кантемировский",
        "pos": [30.32177, 59.9784766]
    }
]


class GeoData:
    def __init__(self, request, name, address, pos):
        self.request = request
        self.name = name
        self.address = address
        self.pos = pos


# Request places from Yandex API
def __request_geocode(request):
    response = requests.get(
        "https://geocode-maps.yandex.ru/1.x/" +
        "?apikey=" + apikey_geocode +
        "&geocode=" + "+".join(request.split()) +
        "&bbox=" + lower_corner + "~" + upper_corner +
        "&format=json" +
        "&result=100" +
        "&lang=ru_RU"
    )
    return response


# Convert responded places from Yandex API to object
def get_geocode(request):
    result = []
    response = __request_geocode(request)
    data = json.loads(response.content)
    for obj in data["response"]["GeoObjectCollection"]["featureMember"]:
        name = obj["GeoObject"]["name"]
        address = obj["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["text"]
        pos = list(map(float, obj["GeoObject"]["Point"]["pos"].split()))
        result.append(GeoData(request, name, address, pos))
    return result


# Request organizations from Yandex API
def __request_organizations(request):
    response = requests.get(
        "https://search-maps.yandex.ru/v1/" +
        "?apikey=" + apikey_organizations +
        "&text=" + request +
        "&lang=ru_RU" +
        "&bbox=" + lower_corner + "~" + upper_corner +
        "&results=500"
    )
    return response


# Convert responded organizations from Yandex API to object
def get_organizations(request):
    result = []
    response = __request_organizations(request)
    data = json.loads(response.content)
    for obj in data["features"]:
        name = obj["properties"]["name"]
        address = obj["properties"]["CompanyMetaData"]["address"]
        pos = list(map(float, obj["geometry"]["coordinates"]))
        result.append(GeoData(request, name, address, pos))
    return result


def get_nearest(point, point_list):
    def get_distance(a, b):
        return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    nearest = point_list[0]
    min_dist = get_distance(point.pos, point_list[0].pos)
    for location in point_list:
        dist = get_distance(point.pos, location.pos)
        if dist < min_dist:
            nearest = location
            min_dist = dist
    return nearest


def translate_bridge_to_obj(bridge):
    res = GeoData("DB_BRIDGE", bridge["name"], bridge["name"], bridge["pos"])
    return res


def get_nearest_bridge(point):
    bridges_obj = list(map(translate_bridge_to_obj, bridges))
    nearest = get_nearest(point, bridges_obj)
    return nearest
