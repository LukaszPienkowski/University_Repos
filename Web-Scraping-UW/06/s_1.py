import scrapy

class Link(scrapy.Item):
    link = scrapy.Field()

class LinksSpider(scrapy.Spider):
    name = 'link_lists'
    allowed_domains = ['https://en.wikipedia.org/']
    start_urls = ['https://en.wikipedia.org/wiki/Lists_of_musicians']

    def parse(self, response):
        xpath = '//a[re:test(@title, "List of [aA]\w.*")]//@href'
        selection = response.xpath(xpath)[0:9]
        for s in selection:
            l = Link()
            l['link'] = 'https://en.wikipedia.org' + s.get()
            yield l
    
