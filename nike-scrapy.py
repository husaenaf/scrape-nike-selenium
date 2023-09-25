import scrapy

# scraping Men's Basketball Shoes
class nike(scrapy.Spider):
    name = "nike"
    start_urls = ["https://www.nike.com/id/w/mens-basketball-shoes-3glsmznik1zy7ok"]

    def parse(self, response):
        # print(response.body)
        name = response.css("#Tatum\\ 1\\ \\'Home\\ Team\\'\\ PF::text").extract_first()
        category = response.css("#skip-to-products > div:nth-child(1) > div > figure > div > div:nth-child(1) > div > div.product-card__subtitle::text").extract_first()
        kindcolour = response.css("#skip-to-products > div:nth-child(1) > div > figure > div > div.product-card__count-wrapper.false.false > div > button > div::text").extract_first()
        price = response.css("#skip-to-products > div:nth-child(1) > div > figure > div > div.product-card__animation_wrapper > div > div > div > div::text").extract_first()

        print(name)
        print(category)
        print(kindcolour)
        print(price)