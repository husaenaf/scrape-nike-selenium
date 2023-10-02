import time
import requests
import pandas as pd
import csv
import openpyxl
import mysql.connector
from selenium import webdriver
from bs4 import BeautifulSoup
from unidecode import unidecode
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def initialize_webdriver(url):
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def create_csv(file_name, headers):
    file = open(file_name, 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(headers)
    return file, writer

def scroll_page(driver, vertical_steps):
    for i in range(vertical_steps):
        driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(1)

def scrape_data(driver):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    data_list = []

    for item in soup.find_all('div', 'product-card__body'):
        name = item.find('div', 'product-card__title').text
        kindcolour = item.find('div', 'product-card__product-count')
        if kindcolour:
            kindcolour = kindcolour.text
        else:
            kindcolour = "N/A"

        price = item.find('div', 'product-price').text
        price = unidecode(price)

        link = item.find('a')['href']
        image = item.find('div', 'wall-image-loader').find('img')['src']

        item_data = {
            'name': name,
            'kindcolour': kindcolour,
            'price': price,
            'link': link,
            'image': image
        }

        print("Product:", name)
        print("Kind Colour:", kindcolour)
        print("Price:", price)
        print("Link:", link)
        print("Link Image:", image)
        print("============")

        data_list.append(item_data)

    return data_list

def save_data_to_csv(file, writer, data_list):
    for data in data_list:
        writer.writerow([data['name'], data['kindcolour'], data['price'], data['link'], data['image']])

def close_resources(driver, file):
    driver.close()
    file.close()

def main():
    # URL to scrape
    url = 'https://www.nike.com/id/w/mens-football-shoes-1gdj0znik1zy7ok'

    # Initialize WebDriver
    driver = initialize_webdriver(url)

    # Create CSV file
    headers = ['title', 'kindcolour', 'price', 'link', 'link image']
    file, writer = create_csv('csvresult.csv', headers)

    # Scroll the page
    scroll_page(driver, 25)

    # Scrape data
    data_list = scrape_data(driver)

    # Save data to CSV
    save_data_to_csv(file, writer, data_list)

    # Close resources
    close_resources(driver, file)

if __name__ == "__main__":
    main()
