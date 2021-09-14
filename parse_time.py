from bs4 import BeautifulSoup
from urllib.request import urlopen

def parse_bridges():
    html = urlopen("https://mostotrest-spb.ru").read().decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')

    bridges = []
    bridge = soup.find('div', 'bridge')
    bridges.append(bridge)

    while bridge:
        bridges.append(bridge.find_next_sibling('div', 'bridge'))
        bridge = bridge.find_next_sibling('div', 'bridge')

    return bridges

#print(bridge.find_next_sibling('div', 'bridge'))