most = ["0:05", "0:30"]
now = "0:00"
import datetime


def myround(x, base):
    return base * round(x / base)

def get_ending(num: int) -> str:
    if num % 100 in {11, 12, 13, 14}:
        return "ов"
    elif num % 10 in {0, 5, 6, 7, 8, 9}:
        return "ов"
    elif num % 10 in {2, 3, 4}:
        return "а"
    elif num % 10 in {1}:
        return ""



# Функция генерации ответа Алисы
# На вход получает 4 параметра
# now - строка с текущим временем в формате HH:MM
# most - массив из 2 строк, в которых содержатся времена сводки и разводки моста в формате HH:MM
# ra - число, обозначающее действие моста: 0 - разведение, 1 - сведение
# fullname - строка содержащая название моста вместе со словом "мост" в родительном падеже

# Возвращает строку со словами для Алисы, без редакции интонации и пауз
def time_to_text(now, most, ra, fullname):
    res = ""

    move = ["разведения", "сведения"]
    t = [datetime.timedelta(hours=int(most[0][:1]), minutes=int(most[0][2:])),
         datetime.timedelta(hours=int(most[1][:1]), minutes=int(most[1][2:]))]
    now = datetime.timedelta(hours=int(now[:1]), minutes=int(now[2:]))
    c = t[ra] - now
    tm = int(c.seconds / 60)
    if tm == 30:
        res = f"До {move[ra]} {fullname} осталось ровно полчаса, в {t[ra]}"
    elif tm < 30 and tm >= 28:
        res = f"До {move[ra]} {fullname} осталось чуть меньше чем через полчаса, в {t[ra]}"
    elif tm > 30 and tm <= 32:
        res = f"До {move[ra]} {fullname} осталось чуть больше чем через полчаса, в {t[ra]}"
    elif tm == 60:
        res = f"До {move[ra]} {fullname} остался ровно час, в {t[ra]}"
    elif tm > 60 and tm <= 65:
        # res = f"До {move[ra]} {fullname} осталось чуть больше чем через час, в {t[ra]}"
        res = f"До {move[ra]} {fullname} остался час, в {t[ra]}"
    elif tm < 60 and tm >= 55:
        # res = f"До {move[ra]} {fullname} осталось чуть меньше чем через час, в {t[ra]}"
        res = f"До {move[ra]} {fullname} остался час, в {t[ra]}"
    elif tm == 90:
        res = f"До {move[ra]} {fullname} осталось ровно полторачаса, в {t[ra]}"
    elif tm < 90 and tm >= 80:
        # res = f"До {move[ra]} {fullname} осталось чуть меньше чем через полторачаса, в {t[ra]}"
        res = f"До {move[ra]} {fullname} осталось полторачаса, в {t[ra]}"
    elif tm > 90 and tm <= 100:
        # res = f"До {move[ra]} {fullname} осталось чуть больше чем через полторачаса, в {t[ra]}"
        res = f"До {move[ra]} {fullname} осталось полторачаса, в {t[ra]}"
    else:
        if tm > 60 and tm < 120:
            ok = 5
        elif tm >= 120:
            ok = 10
        else:
            ok = 1

        ntm = myround(tm, ok)




        m = int(ntm % 60)
        h = int(ntm / 60)
        if get_ending(h) == "":
            res = f"До {move[ra]} {fullname} остался "
        else:
            res = f"До {move[ra]} {fullname} осталось "
        if (h != 0):
            res = res + f"{str(h)} час{get_ending(h)}"
        if (m != 0):
            res = res +f" {str(m)} "
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


# print(time_to_text(now, most, 1, "моста Александра Невского"))

def prints(n, name):
    global now
    global most
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:06"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:12"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:28"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:30"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:31"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:47"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "0:55"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:00"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:02"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:15"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:16"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:20"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:30"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "1:38"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "2:00"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "2:02"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

    most[0] = "4:00"
    now     = "0:00"
    print("Время:",now,"Время разводки моста:",most[0])
    print("Фраза Aлисы:", time_to_text(now, most, n, name))
    print("----------------------------------")

prints(0, "моста Александра Невского")