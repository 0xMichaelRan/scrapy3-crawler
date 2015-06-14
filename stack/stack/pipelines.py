import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.update({'url': item['url']}, dict(item), upsert=True)
            log.msg("Question added to MongoDB database!",
                    level=log.DEBUG, spider=spider)
        return item

# https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/
# https://realpython.com/blog/python/web-scraping-and-crawling-with-scrapy-and-mongodb/
