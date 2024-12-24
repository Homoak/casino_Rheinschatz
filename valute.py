import requests
from bs4 import BeautifulSoup

def eur ():
    url = "https://privatbank.ua/rates-archive"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('div', class_='purchase').find('span')
    usd = soup.find('div', class_='sale').find('span')
    usd = usd.text
    title = title.text
    print(title)
    print(usd)

eur()
