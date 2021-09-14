from urllib.request import urlopen
f = open("urls.txt", "r", encoding="utf-8")
s = f.read()
s = eval(s)
k = int(input())
html = urlopen("https://mostotrest-spb.ru" + s[k]).read().decode('utf-8')
k = html.find('content="')
print(html[k:])