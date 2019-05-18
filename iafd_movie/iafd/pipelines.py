# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy import signals
from scrapy.exporters import CsvItemExporter
import csv

class IafdPipeline(object):
    def __init__(self):
    	self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
    	pipeline = cls()
    	crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    	crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    	return pipeline

    def spider_opened(self, spider):
    	file = open('%s_items.csv' % spider.name, 'w+b')
    	self.files[spider] = file
    	self.exporter = CsvItemExporter(file)
    	self.exporter.fields_to_export = ['names', 'movie_title',
    					'movie_year', 'distributor', 'notes', 'Formats']
    	self.exporter.start_exporting()

    def spider_closed(self, spider):
    	self.exporter.finish_exporting()
    	file = self.files.pop(spider)
    	file.closed()

    def process_item(self, item, spider):
    	self.exporter.export_item(item)
    	return item