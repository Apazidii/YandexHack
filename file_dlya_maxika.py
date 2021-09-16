import json

def read_json():
    file = open("bridge.json", "r", encoding="utf-8")
    j = json.load(file)

    def d(k):
        k.pop("river")
        k.pop("link")
        k.pop("stop_water_trans")
        k.pop("start_water_trans")
        return k

    j = list(map(d, j))

    return j