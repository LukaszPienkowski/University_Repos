from urllib import request
from bs4 import BeautifulSoup as BS

painter_links = []

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/List_of_hard_rock_musicians_(N%E2%80%93Z) ' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

tags = bs.find_all('ul')[4].find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in tags]

painter_links.extend(links)

for link in painter_links:
    print(link)
 