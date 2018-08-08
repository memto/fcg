# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryFlag(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    main_info = scrapy.Field()
