# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FairItem(scrapy.Item):
    link = scrapy.Field()
    large_img = scrapy.Field()
    small_img = scrapy.Field()
    promo = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
