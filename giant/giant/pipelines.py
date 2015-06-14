# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GiantPipeline(object):
    def process_item(self, item, spider):
        # if product title is empty, discard
    	if len(item['title']) == 0 or not item['title'][0]:
    		raise DropItem("Missing title, %s" % item)

        array = ['title', 'small_img', 'large_img', 'old_price', 'now_price', 'prd_url', 'prd_code']
        for prop in array:
            print prop
            if prop not in item or len(item[prop]) == 0:
                item[prop] = ""
            else:
                item[prop] = item[prop][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")


        # if len(item['title']) == 0:
        #     item['title'] = ""
        # else:
        #     item['title'] = item['title'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['title']) == 0:
        #     item['title'] = ""
        # else:
        #     item['title'] = item['title'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['small_img']) == 0:
        #     item['small_img'] = ""
        # else:
        #     item['small_img'] = item['small_img'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['large_img']) == 0:
        #     item['large_img'] = ""
        # else:
        #     item['large_img'] = item['large_img'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['old_price']) == 0:
        #     item['old_price'] = ""
        # else:
        #     item['old_price'] = item['old_price'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['now_price']) == 0:
        #     item['now_price'] = ""
        # else:
        #     item['now_price'] = item['now_price'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['prd_url']) == 0:
        #     item['prd_url'] = ""
        # else:
        #     item['prd_url'] = item['prd_url'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        # if len(item['prd_code']) == 0:
        #     item['prd_code'] = ""
        # else:
        #     item['prd_code'] = item['prd_code'][0].encode("utf-8").replace("\r", "").replace("\t", "").replace("\n", "")

        return item
