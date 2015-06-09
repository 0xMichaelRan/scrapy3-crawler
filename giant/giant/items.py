# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GiantItem(scrapy.Item):
    small_img = scrapy.Field()
    product_code = scrapy.Field()
    old_price = scrapy.Field()
    now_price = scrapy.Field()
    title = scrapy.Field()

