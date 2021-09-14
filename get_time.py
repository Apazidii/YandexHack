from parse_time import parse_bridges

# k = int(input("Введите число: "))
k = input("Название моста: ")

def get_bridge_from_name(k):
    arr = parse_bridges()
    for str in arr:
        if str.find("div", "name").text == k:
            return str
    return None

def f(k):
    return (k.text)

def get_time_from_name(name):
    str = get_bridge_from_name(name)
    time = str.find_all("span")
    time = list(map(f, time))
    time.sort()
    return time

def print_time(time):
    l = len(time)
    print("Мост разведен ", end="")
    for i in range(0, l, 2):
        if (i != 0):
            print(" и ", end="")
        print("c " + time[i] + " по " + time[i + 1], end="")

time = get_time_from_name(k)

print_time(time)

# for a in arr[0].find_all("span"):
#     print(a.text)
# print(arr[0].find_all("span"))