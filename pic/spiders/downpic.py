# -*- coding: utf-8 -*-
import scrapy
from pic.items import PicItem


class DownpicSpider(scrapy.Spider):
    name = "downpic"
    allowed_domains = ["sample.com"]
    start_urls = (
        'http://www.sample.com/PIC01/index.html',
    )

    def parse(self, response):
	url_list = response.xpath("//ul/li/a[contains(@href,'PIC01')]/@href").extract()
	for per_url in url_list:
		all_url = "http://www.sample.com%s"%per_url	
		yield scrapy.Request(all_url,callback=self.parse_url)

    def parse_url(self,response):
	items = PicItem()
	pic_list = response.xpath("//img/@src").extract()
	for pic in pic_list:
		items['pic_url'] = pic
		yield items
		#print pic

#response.xpath("//ul/li/a[contains(@href,'PIC01')]/@href").extract()
#response.xpath("//img/@src").extract()
