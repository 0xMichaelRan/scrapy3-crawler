# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from luxurycity.items import LuxurycityItem


class LcityCrawlerSpider(CrawlSpider):
    name = 'lcity_crawler'
    allowed_domains = ['www.luxurycity.com.sg']
    start_urls = ['http://www.www.luxurycity.com.sg/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = LuxurycityItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
