import scrapy

from tutorial.items import OnlineItem

class OnlineSpider(scrapy.Spider):
    name = "onlinecr"
    # allowed_domains = ["redmart.com"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13503&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?urlRequestType=Base&catalogId=10051&categoryId=13506&pageView=grid&urlLangId=-1&beginIndex=0&langId=-1&top_category=13506&storeId=10001"
    ]
    #rules = [Rule(LinkExtractor(allow=['/product/\w+']), 'parse')]

    def parse(self, response):

        for sel in response.xpath('//fieldset/div/div'):
            item = OnlineItem()
            item['link'] = sel.xpath('a[2]/@href').extract()
            item['img_src'] = sel.xpath('a/p/img/@src').extract()
            item['promo'] = sel.xpath('div/p/text()').extract()
            item['price'] = sel.xpath('span[2]/text()').extract()
            item['title'] = sel.xpath('a/h3/text()').extract()

            # item['link'] = sel.xpath('a/@href').extract()
            # item['desc'] = sel.xpath('text()').extract()
            yield item

        # for sel in response.xpath('//ul/li'):
        #     item = DmozItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item
