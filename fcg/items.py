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
    iso_alpha2_country_code = scrapy.Field()
    iso_6391_lang_code = scrapy.Field()
    translated_texts = scrapy.Field()    
    main_info = scrapy.Field()

class CarBrand(scrapy.Item):
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()

    country = scrapy.Field()
    name = scrapy.Field()
    info = scrapy.Field()