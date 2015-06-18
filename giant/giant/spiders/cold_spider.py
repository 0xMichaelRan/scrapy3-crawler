import scrapy
import json

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest

from giant.items import GiantItem


class ColdCrawlerSpider(CrawlSpider):
    name = 'cold_spider'
    
    def start_requests(self):
        return [FormRequest(url="https://www.coldstorage.com.sg/api/catalog/department/listdeptcatalphabetically",
                            formdata={},
                            callback=self.parseCategoryList)]

    def parseCategoryList(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        total_count = 0

        print 'Well, we will do POST to '
        print 'https://www.coldstorage.com.sg/api/catalog/product/fetch'
        print 'with category_slug=(the category name) to request item list as Json.'
        print 'however, we can also leave category_slug blank, '
        print 'and all items from coldstorage.com.sg will be returned!'
        print 'That\'s fantastic but we aren\'t doing this right now. '
        print 'We\'ll query one by one with callback'

        for oneCategory in jsonresponse:
        
            print  '>>>> Category code (' + oneCategory["code"] + '): ' + oneCategory["name"] + '(' + oneCategory["slug"] + ') has ' + oneCategory["product_count"] + ' items'
            total_count += int(oneCategory["product_count"])
            print  '>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

            yield FormRequest(url="https://www.coldstorage.com.sg/api/catalog/product/fetch",
                    formdata={'category_slug' : oneCategory["slug"]},
                    callback=self.parseItemList)

        print '>>>> So, there should be in total ' + str(total_count) + ' items. '
        print '>>>> Let\'s do this. '

    def parseItemList(self, response):
        productListJson = json.loads(response.body_as_unicode())
        for product in productListJson["product_list"]:
            item = GiantItem()

            item['title'] = [ product["name"] ]
            item['brand'] = [ product["brand"] ]

            # if product["average_weight"] is not None
            if product["average_weight"]:
                item['quantity'] = [ product["average_weight"] ]
            item['unit'] = [ product["size"] ]

            item['small_img'] = [ "http://www.coldstorage.com.sg" + product["image"].replace("\\", "") ]

            item['old_price'] = [ product["highest_price"] ]
            item['now_price'] = [ product["lowest_price"] ]

            item['prd_code'] = [ product["product_id"] ]

            item['merchant'] = "Cold Storage"
            item['website'] = "http://www.coldstorage.com.sg"

            yield item
