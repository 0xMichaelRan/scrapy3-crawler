# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GiantPipeline(object):
    def process_item(self, item, spider):
    	if len(item['title']) == 0 or not item['title'][0]:
    		raise DropItem("Missing title, %s" % item)
        item['product_code'] = item['product_code'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
        item['small_img'] = 'giantonline.com.sg' + item['small_img'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
    	
    	if len(item['old_price']) == 1:
    		item['old_price'] = item['old_price'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
    	else:
    		item['old_price'] = ""

    	item['now_price'] = item['now_price'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")
    	item['title'] = item['title'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        return item
