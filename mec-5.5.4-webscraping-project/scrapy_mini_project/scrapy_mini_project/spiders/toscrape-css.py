import scrapy

class CSSQuotesSpider(scrapy.Spider):
    name = 'toscrape-css'
    start_urls=[
        'https://quotes.toscrape.com/page/1'
    ]
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield{
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            
        next_page=response.css("li.next a").attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
                    