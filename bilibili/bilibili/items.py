# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_urls = Field()
    files = Field()
    title = Field()
    pass


class PhotoItem(scrapy.Item):
    url = 'files'
    album = ''
    links = set()
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_urls = Field()
    image = Field()
    file_urls = Field()
    files = Field()
    image_main_url = Field()
    title = Field()
    tag = Field()
    pass


class Thumbnail(scrapy.Item):
    image_urls = Field()
    image = Field()
    thumb = Field()
    master = Field()
    pass

