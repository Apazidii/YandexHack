from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://mostotrest-spb.ru").read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

bridges = []
bridge = soup.find('div', 'bridge')
bridges.append(bridge)

while bridge:
    bridges.append(bridge.find_next_sibling('div', 'bridge'))
    bridge = bridge.find_next_sibling('div', 'bridge')

#print(bridges[0])

#print(bridge.find_next_sibling('div', 'bridge'))