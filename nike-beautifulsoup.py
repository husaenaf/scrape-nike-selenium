import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
import base64

# Scraping data Boys Running Shoes
url = 'https://www.nike.com/id/w/boys-running-shoes-37v7jz4413nzy7ok'
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')
boysjordan = soup.find('div', 'product-grid__items css-hvew4t')

for product in boysjordan.find_all('div', 'product-card'):
    title = product.find('div', 'product-card__title').text.strip()
    kindcolour = product.find('button', 'product-card__colorway-btn').find('div').text.strip()
    fixprice = unidecode(product.find('div', 'product-card__price').find('div').find('div').text.strip())
    link = product.find('div', 'product-card__body').find('a')['href']
    link_image = product.find('div', 'wall-image-loader').find('img')['src']

    print('\n' + title)
    print(kindcolour)
    print(fixprice)
    print(link)
    print(link_image)
