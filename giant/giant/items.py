# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GiantItem(scrapy.Item):
	
    title = scrapy.Field()
    brand = scrapy.Field()
    quantity = scrapy.Field()
    unit = scrapy.Field()
    
    small_img = scrapy.Field()
    large_img = scrapy.Field()
    
    old_price = scrapy.Field()
    now_price = scrapy.Field()
    promo = scrapy.Field()
    
    prd_url  = scrapy.Field()
    prd_code = scrapy.Field()
    
    merchant = scrapy.Field()
    website = scrapy.Field()
    update_time = scrapy.Field()
