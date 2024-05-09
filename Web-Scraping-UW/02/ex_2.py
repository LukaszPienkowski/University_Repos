from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

### Downloading whole html file with BS framework
url = 'https://en.wikipedia.org/wiki/Pawe%C5%82_Domaga%C5%82a' 
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')
#print(bs)

### Scraping Pawel’s date of birth and saving in data frame 
bs_birth = bs.find_all('span', {'class' : 'bday'})
birth = [name.get_text() for name in bs_birth]
d1 = pd.DataFrame(birth)

### Scraping Pawel’s three occupations and saving in data frame 
bs_occu = bs.find_all('div', {'class' : 'hlist hlist-separated'})
occu = [name.get_text(', ') for name in bs_occu]
d2 = pd.DataFrame(occu)

### Scraping the list of references and saving in data frame 
bs_ref = bs.find('div', {'class' : 'mw-references-wrap mw-references-columns'})
bs_ref1 = bs_ref.find_all('li')
ref = [name.get_text() for name in bs_ref1]
res2 = pd.DataFrame(ref)

### Final result
res = pd.concat([d1, d2])
print(res)
print(res2)