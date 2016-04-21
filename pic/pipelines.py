# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PicPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
	yield scrapy.Request(item['pic_url'])
#	for image_url in item['pic_url']:
#		print image_url
#		yield scrapy.Request(image_url)
    #def process_item(self, item, spider):
    #    return item
