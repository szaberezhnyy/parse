
# coding: utf-8

# In[3]:

from bs4 import BeautifulSoup
import requests


# In[28]:

basic_url = 'https://krisha.kz/prodazha/kvartiry/'
n = '&'


# In[23]:

town='almaty/'


# In[24]:

# метки
room_num = 'das[live.rooms]='
# from 1 to 5.100


# In[25]:

# цена от и до
from_price = 'das[price][from]='
to_price = 'das[price][to]='


# In[26]:

# тип здания
building_type = 'das[flat.building][]='
b_type=[]
from collections import namedtuple
building = namedtuple('building',['type','n_type'])
b_type.append(building('кирпичный', 1))
b_type.append(building('панельный',2))
b_type.append(building('монолитный',3))
b_type.append(building('каркасно-камышитовый',4))
b_type.append(building('иное',5))
print(b_type[0].n_type)


# In[27]:

# text
txt = '_txt_='


# In[29]:

url=basic_url+'?'+n+room_num+'1'
print(url)


# In[ ]:

def parse_fst_page(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'lxml')


# In[54]:

r=requests.get(url)
soup=BeautifulSoup(r.content, 'lxml')


# In[55]:

pages = []
for page in soup.find_all('a'):
    a = page.get('data-page')
    if a:
        pages.append(a)
max_page=int(pages[-2])
print(max_page)


# In[58]:

all_flats = soup.find_all('div', {'class':'a-description'})
print(all_flats[0].prettify())


# In[70]:

class flat:
    def __init__ (self):
        self.title = None
        self.link = None
        self.price = None
        self.address = None
        self.descr = None
        


# In[97]:

parsed_flats = []


# In[98]:

for flats in all_flats:
    f=flat()
    f.link = flats.find_all("a", {'class':'link'})[0].get('href')
    f.title = flats.find_all("a", {'class':'link'})[0].get('title')
    f.price = flats.find_all('span', {'class':'a-price-value'})[0].text
    f.address = flats.find_all('div', {'class':'a-subtitle'})[0].text
    f.descr = flats.find_all('div', {'class':'a-text'})[0].text
    parsed_flats.append(f)
    print(f.title,f.price)
   # print(s.get('title'))


# In[ ]:




# In[108]:

dir(f)


# In[109]:

print(f.title,f.price)


# In[107]:

print(f)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



