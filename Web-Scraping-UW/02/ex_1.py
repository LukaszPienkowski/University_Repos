from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

### Downloading whole html file with BS framework
url = 'https://www.pythonscraping.com/pages/page3.html' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')
#print(bs)

### Scraping bolded parts of the text and saving in data frame 
bs_bolded = bs.find_all('span', {'class' : 'excitingNote'})
bolded = [name.get_text() for name in bs_bolded]
d1 = pd.DataFrame(bolded)

### Scraping the last Item Title from the table and saving in data frame 
bs_title = bs.find_all('tr', {'id' : 'gift5'})
title = [name.get_text() for name in bs_title]
title1 = [words for line in title for words in line.split("\n")]
while('' in title1):
    title1.remove('')
d2 = pd.DataFrame(title1[0:1:1])

### Scraping the footer of the webpage and saving in data frame 
bs_footer = bs.find_all('div', {'id' : 'footer'})
footer = [name.get_text() for name in bs_footer]
footer_1 = [s.replace("\n", "") for s in footer]
d3 = pd.DataFrame(footer_1)

### Final result
res = pd.concat([d1, d2, d3])
print(res)