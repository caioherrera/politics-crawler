#!/usr/bin/env python3

import scrapy
from unidecode import unidecode

class FirstSpider(scrapy.Spider):
    name = 'first'

    def start_requests(self):
        urls = ['https://g1.globo.com/politica/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        i = 0
        raw_css = '.bastian-page > div:nth-child(1) > div:nth-child({0}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a::text'
        #news_title = response.css(raw_css.format(i)).extract_first()
        while True:
            i += 1
            news_title = response.css(raw_css.format(i)).extract_first()
            if news_title == None:
                break
            yield { 'title': unidecode(news_title) }
