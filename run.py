import requests
import time
from bs4 import BeautifulSoup
from flask import Flask, render_template
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

app = Flask(__name__)   # pembuatan objek Flask untuk membuat aplikasi web

@app.route('/')     # Ini adalah decorator yang menentukan rute untuk fungsi home().
def home():         # Ketika mengakses rute utama (/), maka fungsi home()  dijalankan & merender template 'base.html'.
    return render_template('base.html')

@app.route('/scraping-nike-selenium')
def scraping_nike_selenium():
    url = 'https://www.nike.com/id/w/mens-football-shoes-1gdj0znik1zy7ok'
    driver = webdriver.Chrome()
    driver.get(url)

    # proses scrolling 20 kali kebawah setiap scrollnya 1 detik dengan jarak vertikal 250 piksel dalam setiap langkah
    for i in range(25):
        driver.execute_script("window.scrollBy(0, 250)")
        time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    return render_template('scraping-nike-selenium.html', soup=soup)


if __name__ == '__main__':
    app.run(debug=True, port=7777)