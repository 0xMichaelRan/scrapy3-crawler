# -*- coding: utf-8 -*-

# Scrapy settings for giant project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'giant'

SPIDER_MODULES = ['giant.spiders']
NEWSPIDER_MODULE = 'giant.spiders'

ITEM_PIPELINES = {
    'giant.pipelines.GiantPipeline': 300,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'giant (+http://www.yourdomain.com)'

DOWNLOAD_DELAY = 5
