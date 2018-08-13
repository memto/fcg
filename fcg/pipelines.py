# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

from fcg.helpers.translator import get_translated_by_country_code, get_translated_by_lang


class MyImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item


class TranslatePipeline(object):
    def process_item(self, item, spider):
        print('='*3)
        try:
            main_info = item['main_info']
            country_code = main_info['Code']
            translations = get_translated_by_country_code(country_code)
            for translation in translations:
                print(translation.origin, ' -> ', translation.text)
        except Exception:
            translations = get_translated_by_lang('en')
            for translation in translations:
                print(translation.origin, ' -> ', translation.text)


class FcgPipeline(object):
    def process_item(self, item, spider):
        return item
