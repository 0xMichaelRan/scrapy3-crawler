import pymongo
import datetime
import time

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class GiantPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        # if product title is empty, discard
    	if not item or len(item['title']) == 0 or not item['title'][0]:
    		raise DropItem("Missing title, %s" % item)

        # if is a valid item, then we process the string data
        array = ['title', 'brand', 'small_img', 'large_img', 
                'old_price', 'now_price', 'prd_url', 'prd_code']
        
        # for each property of the item, remove all special chars
        for prop in array:
            if prop not in item or len(item[prop]) == 0:
                item[prop] = ""
            else:
                item[prop] = (item[prop][0].encode("utf-8")
                    .replace("\r", "")
                    .replace("\t", "")
                    .replace("\n", ""))
                
        # replace any S$ or $ sign from the price property
        item['old_price'] = item['old_price'].replace("S$", "").replace("$", "")
        item['now_price'] = item['now_price'].replace("S$", "").replace("$", "")

        # add timestamp to current item
        ts = time.time()
        item['update_time'] = (datetime.datetime.fromtimestamp(ts)
            .strftime('%Y-%m-%d %H:%M:%S'))

        # put the item into mongo db (using 'title' as key)
        self.collection.update(
            {'title': item['title']},
            dict(item), upsert=True
            # The dict() constructs from sequences of key-value pairs
        )
        ## last step, print a msg in console
        log.msg("Grocery item added to MongoDB database!",
                level=log.DEBUG, spider=spider)


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
