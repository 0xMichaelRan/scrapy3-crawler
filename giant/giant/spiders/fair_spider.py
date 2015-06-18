import scrapy

from giant.items import GiantItem

class Fair_spider(scrapy.Spider):
    name = "fair_spider"
    # allowed_domains = ["redmart.com"]
    start_urls = [

        "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&urlRequestType=Base&pageView=grid&catalogId=10051&categoryId=13501&beginIndex=0",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13502&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13503&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13504&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13505&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13506&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13507&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13508&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13509&pageView=grid&catalogId=10051",
        # "http://www.fairprice.com.sg/webapp/wcs/stores/servlet/CategoryDisplay?storeId=10001&beginIndex=0&urlRequestType=Base&categoryId=13510&pageView=grid&catalogId=10051",
    ]
    #rules = [Rule(LinkExtractor(allow=['/product/\w+']), 'parse')]

    def parse(self, response):

        # if current page is a product details page, crawl the product info
        for sel in response.xpath('//div[@class="prod_des_wrp_n"]'):
            item = GiantItem()

            item['title'] = sel.xpath('div/div/div/h1/text()').extract()

            item['small_img'] = sel.xpath('div/div/div/img/@src').extract()
            item['large_img'] = sel.xpath('div/div/div/img/@data-large-img-url').extract()

            item['now_price'] = sel.xpath('div/div/div/div/div/p/text()').extract()
            item['promo'] = sel.xpath('div/div/div/div/div/h3/text()').extract()
            
            item['prd_url'] = response.url
            
            item['merchant'] = "Fairprice"
            item['website'] = "http://www.fairprice.com.sg"

            yield item

        # if current page is a product overview list, go into each product link
        for prod in response.xpath('//fieldset/div/div'): # last div: class=pro_list
            prod_link = prod.xpath('a[2]/@href').extract()
            if len(prod_link) > 0:
                yield scrapy.Request(prod_link[0], callback=self.parse)

        # if current page is a product overview list
        if ('CategoryDisplay' in response.url):
            # eg. www.fairprice.com.sg/.../categoryId=13501&beginIndex=0
            list1 = response.url.split('categoryId=')
            list2 = list1[1].split('&beginIndex=')
            catId = int(list2[0])
            beginInd = int(list2[1])

            # if there are items in current page, then go to next page
            # then go to next page by changing the beginIndex
            if (len(response.xpath('//fieldset/div/div'))):
                splitList = response.url.split('beginIndex=')
                new_url = splitList[0] + 'beginIndex=' + str(beginInd + 24)
                print '>>> next page url is ' + new_url
                yield scrapy.Request(new_url, callback=self.parse)
            # if current page has 0 items, but it's not first page
            # then go to next category by change categoryId and reset beginIndex
            elif (beginInd != 0):
                splitList = response.url.split('categoryId=')
                new_url = splitList[0] + 'categoryId=' + str(catId + 1) + '&beginIndex=0'
                print '>>> next category url is ' + new_url
                yield scrapy.Request(new_url, callback=self.parse)
            # if current page has 0 item, and is the first page of the category
            # stop the crawl, cuz we reach the end
            else:
                print '>>> do nothing'
