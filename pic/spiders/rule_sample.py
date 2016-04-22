# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

#class UrlSpider(scrapy.Spider):
class UrlSpider(CrawlSpider):
    name = "url"
    #allowed_domains = ["dbmeinv.com","sinaimg.cn"]
    start_urls = (
        'http://news.163.com/',
    )
    #    'http://www.dbmeinv.com/',
    #rules = (Rule(LinkExtractor(allow='http://news.163.com/16/0421/10/BL5T67RI00014Q4P.html'),callback='parse_item'),)
    rules = (Rule(LinkExtractor(allow='http://news.163.com/16/\d{4}/\d{2}/.*.html',restrict_xpaths=("//h3/a[@class='ac01']")),callback='parse_item'),)
                                        #这里根据allow里面的规矩来查找ur，restrict_xpaths是辅助作用，来过滤必须符合这个要求的url
    #rules = (Rule(LinkExtractor(allow='http://money.*.html'),callback='parse_item'),)
    #rules = (Rule(LinkExtractor(allow="http://view.163.com/\d+.*.html",deny="http://view.163.com/16/0310/11/BHPS4MFS000156M4.html"),callback='parse_item'),)
    #rules = (Rule(LinkExtractor(allow=('http://ww1.sinaimg.cn/bmiddle/0060lm7Tgw1f33k9if9msj30dw0dw75k.jpg')),callback='parse_item'),)
    #rules = (Rule(LinkExtractor(allow="http://www.dbmeinv.com/dbgroup/\d{6}",restrict_xpaths=("//div[@class='bottombar']")),callback='parse_item'),)
    #rules = (Rule(LinkExtractor(allow="http://www.dbmeinv.com/dbgroup/\d{6}"),callback='parse_item'),)
   

    def parse_item(self,response):
	print response.url
#    def parse(self, response):
#        #pass
#	print response.url
