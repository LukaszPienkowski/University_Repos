from urllib import request
from bs4 import BeautifulSoup as BS

painter_links = []

# Look at the page and the code
url = 'https://en.wikipedia.org/wiki/Lists_of_musicians#Genre' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

R = bs.find_all('ul')[19].find_all('li')

links = ['http://en.wikipedia.org' + tag.a['href'] for tag in R]

painter_links.extend(links)

for link in painter_links:
    print(link)
