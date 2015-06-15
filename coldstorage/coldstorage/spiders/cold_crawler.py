import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from coldstorage.items import ColdstorageItem


class ColdCrawlerSpider(CrawlSpider):
    name = 'cold_crawler'
    
    # allowed_domains = ['www.coldstorage.com.sg']
    # start_urls = ['https://www.coldstorage.com.sg/shop-online/dairy-chilled-frozen/chilled-frozen']
    # 
    # rules = (
    #     Rule(LinkExtractor(allow='shop-online/.*'), callback='parse_item', follow=True),
    # )
    # 
    # rules = (
    #     # Extract links matching 'category.php' (but not matching 'subsection.php')
    #     # and follow links from them (since no callback means follow=True by default).
    #     Rule(LinkExtractor(allow=('ice-cream', ))),

    #     # Extract links matching 'item.php' and parse them with the spider's method parse_item
    #     Rule(LinkExtractor(allow=(r'www.coldstorage.com.sg/shop-online/dairy-chilled-frozen/chilled-frozen', )), callback='parse_item'),
    # )

    start_urls = ['https://giantonline.com.sg/']
    # urls from which the spider will start crawling
    
    rules = [
        Rule(LinkExtractor(allow=[r'catalog/.+']), follow=True, callback='parse_item'), 
        # r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
        Rule(LinkExtractor(allow=[r'catalog/.+']), callback='parse_item')
        # r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs
    ]

    def parse_item(self, response):
        i = ColdstorageItem()

        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print 'follow the url ' + str(response.url)
        print response.url

        #     for sel in response.xpath('//div[@class="prod_des_wrp_n"]'):
        # item = FairItem()

        # item['link'] = response.url
        # item['large_img'] = sel.xpath('div/div/div/img/@data-large-img-url').extract()
        # item['small_img'] = sel.xpath('div/div/div/img/@src').extract()
        # item['promo'] = sel.xpath('div/div/div/div/div/h3/text()').extract()
        # item['price'] = sel.xpath('div/div/div/div/div/p/text()').extract()
        # item['title'] = sel.xpath('div/div/div/h1/text()').extract()

        # yield item


        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
