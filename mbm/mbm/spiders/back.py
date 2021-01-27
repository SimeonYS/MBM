# import scrapy
# from ..items import MbmItem
#
# class MbmspiderSpider(scrapy.Spider):
#     name = 'mbmspider'
#     start_urls = ['https://mbm-bg.com/blog']
#
#     def parse(self, response):
#         all_cards = response.xpath('//div[contains(@class,"card-content-item padding")]')
#         for card in all_cards:
#             card_url = card.xpath('.//h3/a/@href').get()
#             yield scrapy.Request(card_url, callback=self.parse_card)
#
#     def parse_card(self, response):
#
#         Title = response.xpath('//div[@class="page-header"]/h1/text()').get()
#         Date = response.xpath('//div[contains(@class,"page-header")]/h1/following-sibling::div[1]/text()').get()
#         Content = response.xpath('//div[contains(@class,"static-page")]//descendant-or-self::*[not(self::style or self::script)]/text()').getall()
#         Content = ''.join(x for x in Content if x not in '\r\t\n').strip()
#         Content = Content.replace(' ',' ')
#         Content = Content.replace('\n', ' ')
#         item = MbmItem()
#         item['Title'] = Title,
#         item['Date'] = Date,
#         item['Content'] = Content,
#
#         yield item

# ('//div[contains(@class,"page-content ")]//text()[not(ancestor::style or ancestor::script or ancestor::div[@class="text-center"] or ancestor::form or ancestor-or-self::a)]').getall()