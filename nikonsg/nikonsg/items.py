# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NikonsgItem(scrapy.Item):
    
    # property of the product
    category = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    prod_url  = scrapy.Field()
    prod_code = scrapy.Field()
    small_img = scrapy.Field()
    large_img = scrapy.Field()
    
    # pricing info
    price = scrapy.Field()
    currency = scrapy.Field()
    country = scrapy.Field()
    website = scrapy.Field()
    
    # realtime and searching info
    update_time = scrapy.Field()
    key = scrapy.Field()
