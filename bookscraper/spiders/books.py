import scrapy
from bookscraper.items import BookscraperItem
from urllib.parse import urljoin
import re

class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.xpath('//ol[@class="row"]/li'):
            item = BookscraperItem()
            item['title'] = book.xpath('.//h3/a/@title').get()
            item['price'] = book.xpath('.//div[@class="product_price"]/p[@class="price_color"]/text()').get().replace('£', '')
            item['rating'] = book.xpath('.//p[contains(@class, "star-rating")]/@class').get().split()[-1]
            book_url = book.xpath('.//h3/a/@href').get()
            book_url = urljoin(response.url, book_url)
            yield response.follow(book_url, self.parse_book, meta={'item': item})

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield response.follow(next_page_url, self.parse)

    def parse_book(self, response):
        item = response.meta['item']
        item['category'] = response.xpath('//ul[@class="breadcrumb"]/li[3]/a/text()').get()
        stock_text = response.xpath('//table[@class="table table-striped"]/tr[th/text()="Availability"]/td/text()').getall()
        stock_text = ''.join(stock_text).strip()
        item['stock'] = int(re.search(r'\d+', stock_text).group()) if stock_text else 0
        yield item
