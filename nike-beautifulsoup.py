import requests
from bs4 import BeautifulSoup
from unidecode import unidecode


# scraping data Boys Running Shoes
html_doc = requests.get('https://www.nike.com/id/w/boys-running-shoes-37v7jz4413nzy7ok')
soup = BeautifulSoup(html_doc.text, 'html.parser')
boysjordan = soup.find('div', 'product-grid__items css-hvew4t')
titles = boysjordan.find_all('div', 'product-card__titles')
kindcolours = boysjordan.find_all('button', 'product-card__colorway-btn')
fixprices = boysjordan.find_all('div', 'product-card__price')
links = boysjordan.find_all('div', 'product-card__body')
link_images = boysjordan.find_all('div', 'wall-image-loader')


for title, kindcolour, fixprice, link, link_image in zip(titles, kindcolours, fixprices, links, link_images):
    title = title.find('div').text
    print('\n' + title)
    try:
        kindcolour = kindcolour.find('div').text
        print(kindcolour)
    except:
        kindcolour = ''
    try:
        fixprice = fixprice.find('div').find('div').text    # pencarian fixprices di dalamnya div dan dalamnya ada div lagi
        # Menggunakan unidecode untuk menghilangkan karakter non-ASCII yang ada di file CSV seperti Â dan lainnya
        fixprice = unidecode(fixprice)
        print(fixprice)
    except:
        fixprice = ''
    try:
        link = link.find('a')['href']
        print(link)
    except:
        link = ''
    try:
        link_image = link_image.find('img')['src']
        print(link_image)
    except:
        link_image = ''



