import scrapy
import json

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest

from giant.items import GiantItem

class ColdCrawlerSpider(CrawlSpider):
    name = 'cold_crawler'
    
    # allowed_domains = ['www.coldstorage.com.sg']
    # start_urls = ['https://www.coldstorage.com.sg/shop-online/dairy-chilled-frozen/chilled-frozen']
    # 
    # rules = (
    #     Rule(LinkExtractor(allow='shop-online/.*'), callback='parse_item', follow=True),
    # )
    # 
    # rules = (
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     Rule(LinkExtractor(allow=('ice-cream', ))),

    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     Rule(LinkExtractor(allow=(r'www.coldstorage.com.sg/shop-online/dairy-chilled-frozen/chilled-frozen', )), callback='parse_item'),
    # )

    # start_urls = ['https://www.coldstorage.com.sg/api/catalog/department/listdeptcatalphabetically']
    # # urls from which the spider will start crawling
    
    # rules = [
    #     Rule(LinkExtractor(follow=false, callback='parse_item'), 
    #     # r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
    #     Rule(LinkExtractor(allow=[r'catalog/.+']), callback='parse_item')
    #     # r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs
    # ]

    def start_requests(self):
        return [FormRequest(url="https://www.coldstorage.com.sg/api/catalog/department/listdeptcatalphabetically",
                    formdata={},
                    callback=self.parseCategoryList)]

    def parseCategoryList(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        total_count = 0

        print 'Well, we will do POST to https://www.coldstorage.com.sg/api/catalog/product/fetch with category_slug=(the category name) to request item list as Json.'
        print 'however, we can also leave category_slug blank, and all items from coldstorage.com.sg will be returned!'
        print 'That\'s fantastic but we aren\'t doing this right now. We\'ll query one by one with callback'

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
        for item in productListJson["product_list"]:
            item = ColdstorageItem()
            print 'this ss an item>>>> ' 
            print '???????????????????????????????? ' + str(item)
            yield item






item = GiantItem()

item['brand'] = sel.xpath('div/div/a/text()').extract()
item['title'] = sel.xpath('div/div/h3/a/text()').extract()

item['small_img'] = sel.xpath('div/a/div/img/@src').extract()

item['old_price'] = sel.xpath('div/div/div/div/div/text()').extract()
item['now_price'] = sel.xpath('div/div/div/div/div/strong/text()').extract()

item['prd_code'] = sel.xpath('div/div/div/div/text()[1]').extract()

yield item