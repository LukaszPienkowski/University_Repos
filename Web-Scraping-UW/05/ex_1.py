from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Lists_of_musicians' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

### 1 ###
tags = bs.find_all('ul')[3].find_all('a', {'href':re.compile('\/wiki\/List_of_[aA].*')})
links = ['http://en.wikipedia.org' + tag['href'] for tag in tags]

for link in links:
    print(link)

### 2 ###
link_to_artists = list()
for link in links:
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    headline = bs.find('span', {'class': 'mw-headline'}).text
    if headline.startswith('0') or headline.startswith('A'):
        link_to_artists.append("http://en.wikipedia.org" + bs.find('span', {'class': 'mw-headline'}).find_next('ul').find('li').a['href'])
    else:
        link_to_artists.append('http://en.wikipedia.org' + bs.find('table', {'class': 'wikitable'}).find('td').a['href'])
print(*link_to_artists, sep = '\n')

### 3 ###
names_artists = list()
years_artists = list()

for link in link_to_artists:
    html = request.urlopen(link)
    bs = BS(html.read(), 'html.parser')
    name = bs.find('table', {'class': 'infobox vcard plainlist'})
    if name:
        names_artists.append(name.find('tr').text)
        years_artists.append(bs.find('th',string = 'Years active').next_sibling.text)
    else:
        names_artists.append(bs.find('table', {'class': 'infobox biography vcard'}).find('tr').text)
        years_artists.append(bs.find('th', string = 'Years active').next_sibling.text)
df = pd.DataFrame({'name': names_artists, 'years_active': years_artists})

print(df)
