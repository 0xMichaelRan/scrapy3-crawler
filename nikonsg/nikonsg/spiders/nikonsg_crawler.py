# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from nikonsg.items import NikonsgItem


class NikonsgCrawlerSpider(CrawlSpider):
    name = 'nikonsg_crawler'
    allowed_domains = ['www.nikon.com.sg']

    def start_requests(self):
        return [FormRequest(url="http://www.nikon.com.sg/proxies/nikon/solr.proxy?json.wrf=jQuery1601326410169713199_1437873067591&q=*%3A*&indent=off&version=2.2&debug=false&start=0&rows=100&wt=json&fl=*%2Cscore&sort=sort_order_si+desc%2Cpno_ss+asc&hl=off&hl.fl=title_ut&fq=%2Blocale_s%3Aen_SG+%2Bptc_s%3A(LENS)&locale=en_SG&ptc=LENS&facet=true&ProductStatus=ARCHIVE&widgetSite=NikonAsia&_=1437873067894",
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
        
            print  ('>>>> Category code (' + oneCategory["code"] + '): ' + 
                    oneCategory["name"] + '(' + oneCategory["slug"] + 
                    ') has ' + oneCategory["product_count"] + ' items')
            print  '>>>>>>>>>>>>>>>>>>>>>>>>>>>>'
            total_count += int(oneCategory["product_count"])

            # for each category, request list of all items using their API
            yield FormRequest(url="https://www.coldstorage.com.sg/api/catalog/product/fetch",
                    formdata={'category_slug' : oneCategory["slug"]},
                    callback=self.parseItemList)

        print ('>>>> All categories fetched, there should be in total ' + 
               str(total_count) + ' items. ')
        print '>>>> Let\'s do this. '


    def parse_item(self, response):
        i = NikonsgItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
