import time
import requests
import pandas as pd
import csv
import openpyxl
from selenium import webdriver
from bs4 import BeautifulSoup
from unidecode import unidecode
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# scripe nike Men's Football shoes
url = 'https://www.nike.com/id/w/mens-football-shoes-1gdj0znik1zy7ok'

driver = webdriver.Chrome()
driver.get(url)

# proses membuat csv bag 1
file = open('csvresult.csv', 'w', newline='', encoding='utf-8')
writer = csv.writer(file)
headers = ['title', 'kindcolour', 'price', 'link', 'link image']
writer.writerow(headers)

# menunggu driver selama 10 detik sampai selector zeus-root muncul, kemudian waktu sleep 2 detik (untuk memastikan page terbuka semua)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#experience-wrapper")))
time.sleep(2)

# proses scrolling vertikal dan horizontal
# proses scrolling 20 kali kebawah setiap scrollnya 1 detik dengan jarak vertikal 250 piksel dalam setiap langkah
for i in range(25):
    driver.execute_script("window.scrollBy(0, 250)")
    time.sleep(1)
# digunakan untuk melakukan scroll ke samping sebanyak 50 piksel dalam satu langkah
driver.execute_script("window.scrollBy(50, 0)")
time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")

for item in soup.find_all('div', 'product-card__body'):
    name = item.find('div', 'product-card__title').text
    # kindcolour = item.find('div', 'product-card__product-count').text
    kindcolour = item.find('div', 'product-card__product-count')
    if kindcolour:
        kindcolour = kindcolour.text
    else:
        kindcolour = "N/A"  # Atau nilai default lainnya

    price = item.find('div', 'product-price').text
    price = unidecode(price)
    print(price)

    link = item.find('a')['href']
    image = item.find('div', 'wall-image-loader').find('img')['src']


    print(name)
    print(kindcolour)
    print(price)
    print(link)
    print(image)
    print("============")

    name = name.replace(':', '=').replace('/', '_')
    # proses membuat gambar
    with open('gallery/' + name + '.jpg', 'wb') as f:
        img = requests.get(image)
        f.write(img.content)


    writer.writerow([name, kindcolour, price, link, image])
file.close()

driver.close()