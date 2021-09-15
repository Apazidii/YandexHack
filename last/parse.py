from urllib.request import urlopen
html = urlopen("https://mostotrest-spb.ru").read().decode('utf-8')
print(html)
