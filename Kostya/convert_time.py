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
# now - datetime объект с текущим временем
# most - массив из 2 строк, в которых содержатся времена сводки и разводки моста в формате HH:MM
# ra - число, обозначающее действие моста: 0 - разведение, 1 - сведение
# fullname - строка содержащая название моста вместе со словом "мост" в родительном падеже

# Возвращает строку со словами для Алисы, без редакции интонации и пауз
def time_to_text(now, most, ra, fullname):
    res = ""

    move = ["разведения", "сведения"]
    move2 = ["сведен", "разведен"]
    t = [datetime.timedelta(hours=int(most[0][:most[0].find(":")]), minutes=int(most[0][most[0].find(":") + 1:])),
         datetime.timedelta(hours=int(most[1][:most[1].find(":")]), minutes=int(most[1][most[1].find(":") + 1:]))]
    rt = [(':'.join(str(t[0]).split(':')[:2])), (':'.join(str(t[1]).split(':')[:2])) ]
    c = t[ra] - now
    tm = int(c.seconds / 60)
    if tm == 30:
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось ровно полчаса, в {rt[ra]}"
    elif tm < 30 and tm >= 28:
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось чуть меньше чем через полчаса, в {rt[ra]}"
    elif tm > 30 and tm <= 32:
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось чуть больше чем через полчаса, в {rt[ra]}"
    elif tm == 60:
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} остался ровно час, в {rt[ra]}"
    elif tm > 60 and tm <= 65:
        # res = f"До {move[ra]} {fullname} осталось чуть больше чем через час, в {rt[ra]}"
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} остался час, в {rt[ra]}"
    elif tm < 60 and tm >= 55:
        # res = f"До {move[ra]} {fullname} осталось чуть меньше чем через час, в {rt[ra]}"
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} остался час, в r{t[ra]}"
    elif tm == 90:
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось ровно полторачаса, в {rt[ra]}"
    elif tm < 90 and tm >= 80:
        # res = f"До {move[ra]} {fullname} осталось чуть меньше чем через полторачаса, в {rt[ra]}"
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось полторачаса, в {rt[ra]}"
    elif tm > 90 and tm <= 100:
        # res = f"До {move[ra]} {fullname} осталось чуть больше чем через полторачаса, в {rt[ra]}"
        res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось полторачаса, в {rt[ra]}"
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
            res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} остался "
        else:
            res = f"Сейчас мост {move2[ra]}, до {move[ra]} {fullname} осталось "
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
        res = res + f", в {rt[ra]}"
    return (res)

