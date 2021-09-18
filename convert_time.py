most = ["0:05", "5:30"]
now = "0:00"
import datetime

def myround(x, base):
    return base * round(x/base)

def get_ending(num: int) -> str:
    if num % 100 in {11, 12, 13, 14}:
        return "ов"
    elif num % 10 in {0, 5, 6, 7, 8, 9}:
        return "ов"
    elif num % 10 in {2, 3, 4}:
        return "а"
    elif num % 10 in {1}:
        return ""

def time_to_text(now, most):
    res = ""

    t_start = datetime.timedelta(hours = int(most[0][:1]), minutes = int(most[0][2:]))
    t_stop  = datetime.timedelta(hours = int(most[1][:1]), minutes = int(most[1][2:]))
    now     = datetime.timedelta(hours = int(now[:1])    , minutes = int(now[2:]))
    c = t_start - now
    tm = int(c.seconds / 60)
    print("Минут:",tm)
    if tm == 30:
        res = "Мост будет разведен ровно через полчаса, в " + most[0]
    elif tm < 30 and tm >=28:
        res = "Мост будет разведен чуть меньше чем через полчаса, в " + most[0]
    elif tm > 30 and tm <=32:
        res = "Мост будет разведен чуть больше чем через полчаса, в " + most[0]
    elif tm == 60:
        res = "Мост будет разведен ровно через час, в " + most[0]
    elif tm > 60 and tm <= 65:
        res = "Мост будет разведен чуть больше чем через час, в " + most[0]
    elif tm < 60 and tm >= 55:
        res = "Мост будет разведен чуть меньше чем через час, в " + most[0]
    elif tm == 90:
        res = "Мост будет разведен ровно через полторачаса, в " + most[0]
    elif tm < 90 and tm >= 80:
        res = "Мост будет разведен чуть меньше чем через полторачаса, в " + most[0]
    elif tm > 90 and tm <= 100:
        res = "Мост будет разведен чуть больше чем через полторачаса, в " + most[0]
    else:
        if tm > 60 and tm < 120:
            ok = 5
        elif tm >= 120:
            ok = 10
        else:
            ok = 1

        ntm = myround(tm, ok)
        k = ntm == tm
        tm = ntm
        m = int(tm % 60)
        h = int(tm / 60)
        if k:
            res = "Мост будет разведен через "
        else:
            res = "Мост будет разведен примерно через "
        if (h != 0):
            res = res + str(h) + " час" + get_ending(h)
        if (m != 0):
            res = res + " " + str(m) + " "
            if (m % 100 in {11, 12, 13, 14, 15, 16, 17, 18, 19}):
                min = "минут"
            elif (m % 10 == 1):
                min = "минута"
            elif (m % 10 in {2, 3, 4, 5}):
                min = "минут"
            else:
                min = "минут"
            res = res + min
        res = res + ", в " + most[0]
    return (res)


def prints():
    global now
    global most
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:06"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:12"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:28"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:30"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:31"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:47"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "0:55"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:00"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:02"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:15"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:16"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:20"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:30"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "1:38"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "2:00"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "2:02"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

    most[0] = "4:00"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most))
    print("----------------------------------")

