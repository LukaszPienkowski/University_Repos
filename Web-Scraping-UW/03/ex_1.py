from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

# Lets download and import to Beautiful Soup already known page:
url = 'https://www.pythonscraping.com/pages/warandpeace.html' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

### a)
regex = 'Anna Pavlovna'
text = bs.find_all(lambda an: an.get_text() ==  'Anna Pavlovna')
i = 0
for tag in text:
    print(tag.get_text())
    i = i + 1

print('Number of occurences:', i)

### b)
one_tag = len(bs.find_all(lambda tag: len(tag.attrs) == 1))
print(one_tag)