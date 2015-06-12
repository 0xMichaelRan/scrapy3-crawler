import scrapy

from giant.items import GiantItem

class Giant_spider(scrapy.Spider):
    name = "giant_spider"
    # allowed_domains = ["redmart.com"]
    start_urls = [

        "https://giantonline.com.sg/catalog/clothing?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/clothing?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/clothing?order=0&view=grid&perpage=36&Product_page=3",

        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=7",
        "https://giantonline.com.sg/catalog/household?order=0&view=grid&perpage=36&Product_page=8",

        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=7",
        "https://giantonline.com.sg/catalog/home-furnishing?order=0&view=grid&perpage=36&Product_page=8",

        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/furniture?order=0&view=grid&perpage=36&Product_page=7",

        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=7",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=8",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=9",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=10",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=11",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=12",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=13",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=14",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=15",
        "https://giantonline.com.sg/catalog/leisure?order=0&view=grid&perpage=36&Product_page=16",

        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/toys-stationery?order=0&view=grid&perpage=36&Product_page=7",

        "https://giantonline.com.sg/catalog/electrical?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/electrical?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/electrical?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/electrical?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/electrical?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/electrical?order=0&view=grid&perpage=36&Product_page=6",

        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=7",
        "https://giantonline.com.sg/catalog/fresh?order=0&view=grid&perpage=36&Product_page=8",

        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=7",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=8",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=9",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=10",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=11",
        "https://giantonline.com.sg/catalog/groceries?order=0&view=grid&perpage=36&Product_page=12",

        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=1",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=2",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=3",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=4",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=5",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=6",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=7",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=8",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=9",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=10",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=11",
        "https://giantonline.com.sg/catalog/dairy-frozen?order=0&view=grid&perpage=36&Product_page=12",
    ]
    #rules = [Rule(LinkExtractor(allow=['/product/\w+']), 'parse')]

    def parse(self, response):

        # for sel in response.xpath('//fieldset/div/div'):
        #     item = GiantItem()
        #     item['link'] = sel.xpath('a[2]/@href').extract()
        #     item['large_img'] = sel.xpath('a/p/img/@src').extract()
        #     item['promo'] = sel.xpath('div/p/text()').extract()
        #     item['price'] = sel.xpath('span[2]/text()').extract()
        #     item['title'] = sel.xpath('a/h3/text()').extract()
        #     yield item


        for sel in response.xpath('//div[@class="items"]/div'):
            item = GiantItem()

            item['small_img'] = sel.xpath('div/a/div/img/@src').extract()
            item['product_code'] = sel.xpath('div/div/div/div/text()[1]').extract()
            item['old_price'] = sel.xpath('div/div/div/div/div/text()').extract()
            item['now_price'] = sel.xpath('div/div/div/div/div/strong/text()').extract()
            item['title'] = sel.xpath('div/div/h3/a/text()').extract()

            yield item
