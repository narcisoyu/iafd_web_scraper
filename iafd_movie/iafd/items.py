# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IafdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # info actors perfile
    names = scrapy.Field()
    ethnicity = scrapy.Field()
    nationality = scrapy.Field()
    hair_colors = scrapy.Field()
    height = scrapy.Field()
    weight = scrapy.Field()
    measurements = scrapy.Field()
    tattoos = scrapy.Field()
    piercings = scrapy.Field()
    performer_aka = scrapy.Field()
    birthday = scrapy.Field()
    astrology = scrapy.Field()
    birthplace = scrapy.Field()
    years_active = scrapy.Field()

    #info actor's movie
    movie_title = scrapy.Field()
    movie_year = scrapy.Field()
    distributor = scrapy.Field()
    notes = scrapy.Field()
    Formats = scrapy.Field()
