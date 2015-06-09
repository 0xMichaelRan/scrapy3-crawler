# -*- coding: utf-8 -*-

# Scrapy settings for fairprice project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fairprice'

SPIDER_MODULES = ['fairprice.spiders']
NEWSPIDER_MODULE = 'fairprice.spiders'

ITEM_PIPELINES = {
    'fairprice.pipelines.FairpricePipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fairprice (+http://www.yourdomain.com)'
