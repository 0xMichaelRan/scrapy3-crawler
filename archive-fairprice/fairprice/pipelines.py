# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem 

class FairpricePipeline(object):
    def process_item(self, item, spider):
    	if len(item['title']) == 0 or not item['title'][0]:
    		raise DropItem("Missing title, %s" % item)
    	# item['price'] = item['price'].replace("\r", "").replace("\t", "").replace("\n", "")
    	item['link'] = item['link'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
        item['large_img'] = item['large_img'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
        item['small_img'] = item['small_img'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
    	
    	if len(item['promo']) == 1:
    		item['promo'] = item['promo'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
    	else:
    		item['promo'] = ""

    	item['price'] = item['price'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
    	item['title'] = item['title'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        return item
