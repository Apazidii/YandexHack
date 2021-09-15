from urllib.request import urlopen
html = urlopen("https://mostotrest-spb.ru/bridges").read().decode('utf-8')
s = '<div class="col-xs-12 col-ss-6 col-sm-3">'
arr = []
while (s in html):
    k = html.find(s)
    html = html[k + 71:]
    k = html.find('"')
    arr.append(html[:k])
    html = html[k:]

f = open("urls.txt", "w", encoding="utf-8")
f.write(str(arr))
print(arr)
print(len(arr))
