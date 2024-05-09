# -*- coding: utf-8 -*-
import scrapy

class Musican(scrapy.Item):
    name        = scrapy.Field()
    years_active       = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'musicans'
    allowed_domains = ['https://en.wikipedia.org/']
    try:
        with open("links.csv", "rt") as f:
            start_urls = [url.strip() for url in f.readlines()][1:]
    except:
        start_urls = []

    def parse(self, response):
        p = Musican()

        name_xpath = '//h1/text()'
        years_active_xpath = '//span[text()="Years active"]/following::td[1]//text()'
       
        p['name'] = response.xpath(name_xpath).getall()
        p['years_active'] = response.xpath(years_active_xpath).getall()

        yield p

