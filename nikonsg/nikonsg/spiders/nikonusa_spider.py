import scrapy
import json

from nikonsg.items import NikonItem

class NikonUsaSpider(scrapy.Spider):
    name = "nikonusa_crawler"
    allowed_domains = ["http://www.nikonusa.com/"]
    
    start_urls = [
        "http://www.nikonusa.com/en/Nikon-Products/Camera-Lenses/All-Lenses/index.page",
    ]

    def parse(self, response):
        responseStr = response.body_as_unicode();
        responseStr = responseStr[responseStr.index('{"response"') : responseStr.index('}}}') + 3]

        productListJson = json.loads(responseStr);
        print 'Now got the json dictionary';

        for product in productListJson["response"]["docs"]:
            item = NikonItem()

            item['category'] = "lens"
            item['title'] = product["title_ut"]
            item['brand'] = "Nikon"

            item['prod_url'] = ("http://www.nikonusa.com/en/Nikon-Products/Product/" + 
                                product["default_url_s"])
            item['small_img'] = ("http://www.nikonusa.com/" + 
                                product["img_s"])

            item['price'] = '333'
            
            item['currency'] = "USD"
            item['country'] = "USA"
            item['website'] = "http://www.nikonusa.com/"

            yield item
            