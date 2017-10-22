import requests
from bs4 import BeautifulSoup
import sys
class flat:
    def __init__ (self):
        self.title = None
        self.link = None
        self.price = None
        self.address = None
        self.descr = None
        self.update_date = None

def parse_fst_page(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'lxml')
    pages = []
    for page in soup.find_all('a'):
        a = page.get('data-page')
        if a:
            pages.append(a)
    max_page=int(pages[-2])
    all_flats = soup.find_all('div', {'class':'a-description'})
    parsed_flats = []
    for flats in all_flats:
        f=flat()
        f.link = flats.find_all("a", {'class':'link'})[0].get('href')
        f.title = flats.find_all("a", {'class':'link'})[0].get('title')
        f.price = flats.find_all('span', {'class':'a-price-value'})[0].text
        f.address = flats.find_all('div', {'class':'a-subtitle'})[0].text
        f.descr = flats.find_all('div', {'class':'a-text'})[0].text
        f.update_date = flats.find_all("span", {'class':'a-date status-item'})[0].text
        parsed_flats.append(f)
    return parsed_flats, max_page


def parse_page(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content, 'lxml')
    all_flats = soup.find_all('div', {'class':'a-description'})
    parsed_flats = []
    for flats in all_flats:
        f=flat()
        f.link = flats.find_all("a", {'class':'link'})[0].get('href')
        f.title = flats.find_all("a", {'class':'link'})[0].get('title')
        f.price = flats.find_all('span', {'class':'a-price-value'})[0].text
        f.address = flats.find_all('div', {'class':'a-subtitle'})[0].text
        f.descr = flats.find_all('div', {'class':'a-text'})[0].text
        parsed_flats.append(f)
    return parsed_flats




def parse_krysha(*args, **kwargs):
    """
    This function will receive a form params
    and send requests to krysha.kz and parse site results
    """
    basic_url = 'https://krisha.kz/prodazha/kvartiry/'
    grand_url=basic_url
    pf, max_page = parse_fst_page(grand_url)
    proceed = ''
    while proceed != 'y' and proceed != 'n':
        print (max_page)
        proceed = input('парсить все эти страницы? y/n ')
    if proceed == 'n':
        sys.exit()


    return max_page



