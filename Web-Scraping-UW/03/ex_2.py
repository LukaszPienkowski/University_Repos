from urllib import request
from bs4 import BeautifulSoup as BS
import re

# Lets download and import to Beautiful Soup already known page:
url = 'https://en.wikipedia.org/wiki/United_Nations_Development_Programme' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

flags = bs.find_all('img', {'src':re.compile('\/\/upload.wikimedia.org\/wikipedia\/(.*)\/thumb\/(.*)\/Flag_(.*)')})
i = 0
for flag in flags:
    print(flag['src'])
    i = i + 1

print("Number of paths:", i)