import scrapy

class XPathQuotesSpider(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls=[
        'https://quotes.toscrape.com/page/1'
    ]
    
    def parse(self, response):
        for quote in response.xpath():
            yield{
                'text': quote.xpath('//span/text::text').get(),
                'author': quote.xpath('//small/author::text').get(),
                'tags': quote.xpath('//div a/tag::text').getall()
            }
            
        next_page = response.xpath('//li/next[a]').attrib[href]
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)