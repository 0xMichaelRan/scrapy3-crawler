# -*- coding: utf-8 -*-
import scrapy
import json
import re

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from nikonsg.items import NikonsgItem
from scrapy.http import FormRequest


class NikonsgCrawlerSpider(CrawlSpider):
    name = 'nikonsg_crawler'
    allowed_domains = ['www.nikon.com.sg']
    # http://www.nikon.com.sg/en_SG/products/categories/nikkor?
    
    def start_requests(self):
        return [FormRequest(url="http://www.nikon.com.sg/proxies/nikon/solr.proxy?json.wrf=jQuery1601326410169713199_1437873067591&q=*%3A*&indent=off&version=2.2&debug=false&start=0&rows=100&wt=json&fl=*%2Cscore&sort=sort_order_si+desc%2Cpno_ss+asc&hl=off&hl.fl=title_ut&fq=%2Blocale_s%3Aen_SG+%2Bptc_s%3A(LENS)&locale=en_SG&ptc=LENS&facet=true&ProductStatus=ARCHIVE&widgetSite=NikonAsia&_=1437873067894",
                            formdata={},
                            callback=self.parseItemList)]

    def parseItemList(self, response):
        responseStr = response.body_as_unicode();
        responseStr = responseStr[responseStr.index('(') + 1 : -1]

        productListJson = json.loads(responseStr);
        print 'Now got the json dictionary';

        for product in productListJson["response"]["docs"]:
            product_link = ("http://www.nikon.com.sg/" + 
                            product["url_s"])
            print 'product_link is ' + product_link;
            yield scrapy.Request(product_link, callback=self.parse);

    def parse(self, response):
            item = NikonsgItem()

            item['category'] = "lens"
            item['title'] = response.xpath('//h2[@class="nik_product_title"]/text()').extract()[0]
            item['brand'] = "Nikon"

            item['prod_url'] = response.url
            item['small_img'] = ("http://www.nikon.com.sg/" + 
                    response.xpath('//div[@id="nik_product_hero_imgWrapp"]/img/@data-src').extract()[0])

            pricing = response.xpath('//div[@class="price"]/text()')
            if len(pricing) is 0:
                print 'try get price again'
                pricing = response.xpath('//div[@class="price"]/p/text()')
            
            if len(pricing) is not 0:
                pricing = pricing.extract()[0].replace(" ", "").replace(",", "").replace(".", "");

                print 'pricing is ' + pricing + '|'
                if len(pricing) is 0:
                    # price on website is a space or empty, but somehow get crawled
                    return;

                item['price'] = re.findall('\d+', pricing)[0]
                # http://stackoverflow.com/a/10365251
                print 'pricccc is ' + item['price']
            else:
                # no pricing info on the website
                return;

            item['currency'] = "SGD"
            item['country'] = "Singapore"
            item['website'] = "http://www.nikon.com.sg"

            yield item

    def get_num(x):
        return int(''.join(ele for ele in x if ele.isdigit()))
