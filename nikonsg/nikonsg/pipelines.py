import pymongo
import datetime
import time
import re

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class NikonsgPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        
        # set current timestamp 
        ts = time.time()
        item['update_time'] = (datetime.datetime.fromtimestamp(ts)
            .strftime('%Y-%m-%d %H:%M:%S'))
        
        item['key'] = (item['brand'].lower() + ' ' + item['title'].lower()).strip()

        # put the item into mongo db (using 'title' as key)
        self.collection.update(
            {'key': item['key'], 'currency': item['currency']},
            dict(item), upsert=True
        )
        # The dict() constructs from sequences of key-value pairs
        # MongoDB upsert: update if it is already exist, or insert otherwise.

        # last step, print a msg in console
        print "Current item added to MongoDB database!"

        return item
