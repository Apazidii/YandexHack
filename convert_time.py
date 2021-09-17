most = ["4:20", "5:30"]
now = "3.20"
import datetime
def time_to_text(now, most):
    res = ""

    t_start = datetime.timedelta(hours = int(most[0][:1]), minutes = int(most[0][2:]))
    t_stop  = datetime.timedelta(hours = int(most[1][:1]), minutes = int(most[1][2:]))
    now     = datetime.timedelta(hours = int(now[:1])    , minutes = int(now[2:]))
    c = t_start - now
    s = c.seconds / 60
    if s < 15:
        res = "Мост будет разведен через " + str(int(s)) + " минут, поторопитесь"
    elif (s >= 15 and s <= 25) or (s >= 35 and s <= 55):
        res = "Мост будет разведен через " + str(int(s)) + " минут, в " + most[0]
    elif s > 25 and s < 25:
        res = "Мост будет разведен через полчаса, в " +most[0]
    elif s > 55 and s < 65:
        res = "Мост будет разведен через час, в " + most[0]
    elif s > 75 and s < 105:
        res = "Мост будет разведен через полтора часа, в " + most[0]
    else:
        res = "Мост будет разведен через " + str(int(s/60)) + " часов " +str(int(s % 60)) + " минут, в " + most[0]
    return (res)

print("Время")
print(time_to_text(now, most))