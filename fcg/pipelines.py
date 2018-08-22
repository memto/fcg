# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

from fcg.helpers.translator import country_code_to_langs, is_supported_lang, get_translated, get_lang_name


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
        iso_alpha2_country_code = item['iso_alpha2_country_code']
        country_code, _ = list(iso_alpha2_country_code.items())[0]

        langs = country_code_to_langs(country_code)
        country_lang = 'en'
        for lang in langs:
            if is_supported_lang(lang):
                country_lang = lang
                break
        lang_name = get_lang_name(country_lang)
        translations = get_translated(country_lang)
        translated_texts = [tran.text for tran in translations]

        item['iso_6391_lang_code'] = {country_lang: lang_name}
        item['translated_texts'] = translated_texts
        
        return item


class FcgPipeline(object):
    def process_item(self, item, spider):
        return item
