import scrapy

from tutorial.items import MyItem

class MySpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["redmart.com"]
    start_urls = [

        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13501&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13502&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13503&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13504&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13505&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13506&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13507&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13508&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13509&pageView=grid&catalogId=10051",
        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13510&pageView=grid&catalogId=10051",
    ]
    #rules = [Rule(LinkExtractor(allow=['/product/\w+']), 'parse')]

    def parse(self, response):

        # for sel in response.xpath('//fieldset/div/div'):
        #     item = MyItem()
        #     item['link'] = sel.xpath('a[2]/@href').extract()
        #     item['large_img'] = sel.xpath('a/p/img/@src').extract()
        #     item['promo'] = sel.xpath('div/p/text()').extract()
        #     item['price'] = sel.xpath('span[2]/text()').extract()
        #     item['title'] = sel.xpath('a/h3/text()').extract()
        #     yield item

        for sel in response.xpath('//div[@class="prod_des_wrp_n"]'):
            item = MyItem()

            item['link'] = response.url
            item['large_img'] = sel.xpath('div/div/div/img/@data-large-img-url').extract()
            item['small_img'] = sel.xpath('div/div/div/img/@src').extract()
            item['promo'] = sel.xpath('div/div/div/div/div/h3/text()').extract()
            item['price'] = sel.xpath('div/div/div/div/div/p/text()').extract()
            item['title'] = sel.xpath('div/div/div/h1/text()').extract()

            yield item

        for prod in response.xpath('//fieldset/div/div'):
            prod_link = prod.xpath('a[2]/@href').extract()
            if len(prod_link) > 0:
                yield scrapy.Request(prod_link[0], callback=self.parse)

        # for sel in response.xpath('//ul/li'):
        #     item = DmozItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item
