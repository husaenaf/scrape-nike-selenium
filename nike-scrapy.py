import scrapy

# scraping Men's Basketball Shoes
class nike(scrapy.Spider):
    name = "nike"
    start_urls = ["https://www.nike.com/id/w/mens-basketball-shoes-3glsmznik1zy7ok"]

    def parse(self, response):
        print(response.body)
        for i in range(1, 27):
            for shoes in response.css('#skip-to-products'):

                raw_price = shoes.css('div:nth-child('+str(i)+') > div > figure > div > div.product-card__animation_wrapper > div > div > div > div::text').extract_first()
                if raw_price:
                    # Membersihkan karakter non-breaking space ('\xa0')
                    cleaned_price = raw_price.replace('\xa0', ' ')
                else:
                    cleaned_price = None

                yield {
                    'name': shoes.css('div:nth-child('+str(i)+') > div > figure > div > div:nth-child(1) > div > div.product-card__title::text').extract_first(),
                    'category': shoes.css('div:nth-child('+str(i)+') > div > figure > div > div:nth-child(1) > div > div.product-card__subtitle::text').extract_first(),
                    'kindcolour': shoes.css('div:nth-child('+str(i)+') > div > figure > div > div.product-card__count-wrapper.false.false > div > button > div::text').extract_first(),
                    'price': cleaned_price,
                    'galery': shoes.css('div:nth-child('+str(i)+') > div > figure > a.product-card__img-link-overlay > div > img[src]::attr(src)').extract_first(),

                    # contoh format jika menggunakan css selector
                    # 'price' : shoes.css('div:nth-child('+str(i)+') > div > figure > div > div.product-card__animation_wrapper > div > div > div > div::text').extract_first(),
                    # dontoh format jika menggunakan xpath
                    # 'price': response.xpath('//*[@id="skip-to-products"]/div[1]/div/figure/div/div[3]/div/div/div/div/text()').extract_first()
                }
