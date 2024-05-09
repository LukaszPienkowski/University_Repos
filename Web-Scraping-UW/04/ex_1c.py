import string
from urllib import request
from bs4 import BeautifulSoup as BS
import re
import pandas as pd

d = pd.DataFrame({'name':[], 'genre':[], 'number of years active':[]})

url = 'https://en.wikipedia.org/wiki/Queen_(band)' 
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

try:
    name = bs.find('h1').text
except:
    name = ''

try:
    genre = bs.find('th',string = 'Genres').next_sibling.text
except:
    genre = ''

try:
    num = bs.find('th',string = 'Years active').next_sibling.text
except:
    num = ''

name = name.split()
name = name[0]

num = num.split('–')
num = num[0]
num = 2022 - int(num)

painter = {'name':name, 'genre':genre, 'number of years active':num}

d = d.append(painter, ignore_index = True)

print(d)
