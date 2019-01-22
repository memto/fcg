# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import subprocess
import tempfile
import shutil
import random

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

from fcg.helpers.translator import country_code_to_langs, is_supported_lang, get_translated, get_lang_name
from fcg.templates import templates
from fcg.helpers.constants import COUNTRIES_RANKINGS_BY_EDU

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
        translated_texts = get_translated(country_lang)

        item['iso_6391_lang_code'] = {country_lang: lang_name}
        item['translated_texts'] = translated_texts

        return item


class FcgPipeline(object):
    __page_count = 0
    __page = None
    __next_rank = 1
    __queued_by_rank = {}

    __random_str = str(random.randrange(1000))
    __fcg_tmp_dir = os.path.join(tempfile.gettempdir(), 'fcg')
    __unziped_templace_dir = os.path.join(
        __fcg_tmp_dir, 'template' + __random_str)
    __unziped_templace_pictures_dir = os.path.join(
        __unziped_templace_dir, 'Pictures')
    __unziped_template_content_file = os.path.join(
        __unziped_templace_dir, "content.xml")
    __unziped_template_content = None

    def open_spider(self, spider):
        self.project_root = os.path.realpath(
            spider.settings.get('PROJECT_ROOT'))
        self.images_store = os.path.realpath(
            spider.settings.get('IMAGES_STORE'))

        os.makedirs(self.__unziped_templace_dir, exist_ok=True)
        template_file = os.path.join(
            self.project_root, "fcg", "templates", "template.odt")
        subprocess.run(["unzip", template_file, "-d",
                        self.__unziped_templace_dir], stdout=subprocess.DEVNULL)
        with open(self.__unziped_template_content_file) as content_file:
            self.__unziped_template_content = content_file.read()

    def process_item(self, item, spider):
        country_rank = item['main_info']['Edu rank']
        if country_rank != self.__next_rank:
            self.__queued_by_rank[country_rank] = item
        else:
            self.__handle_item(item)
            self.__next_rank += 1
            if self.__queued_by_rank:
                queued_min_rank = sorted(self.__queued_by_rank)[0]
                if queued_min_rank == self.__next_rank:
                    queued_item = self.__queued_by_rank[queued_min_rank]
                    del self.__queued_by_rank[queued_min_rank]
                    self.process_item(queued_item, spider)
        return item

    def __handle_item(self, item):
        image_path = item['image_paths'][0]
        front_cel = self.__gen_front_cel(image_path)

        iso_alpha2_country_code = item['iso_alpha2_country_code']
        country_code, country_name = list(
            iso_alpha2_country_code.items())[0]
        iso_6391_lang_code = item['iso_6391_lang_code']
        country_lang, country_lang_name = list(
            iso_6391_lang_code.items())[0]
        translated_texts = item['translated_texts']
        main_info = item['main_info']
        country_rank = main_info['Edu rank']
        back_cel_table_name = 'Table{}'.format(country_code)
        header = '{} - {}({})'.format(country_name, country_lang_name.capitalize(), country_rank)
        meta_data = self.__gen_meta_data(country_code, country_lang, main_info)
        back_cel = self.__gen_back_cel(
            back_cel_table_name, header, translated_texts, meta_data)

        if not self.__page:
            page_front_table_name = 'FontTable{}'.format(self.__page_count)
            page_back_table_name = 'BackTable{}'.format(self.__page_count)
            self.__page = templates.PAGE_TMP_PLACEHOLDER.format(
                frontTableName=page_front_table_name, backTableName=page_back_table_name)
            self.__page_count += 1

        if self.__page:
            card_placeholder_count = self.__page.count(
                templates.CARD_CEL_PLACEHOLDER_MARKER)
            if card_placeholder_count:
                card_placeholder = templates.CARD_CEL_PLACEHOLDER_FMT.format(
                    cardIndex=card_placeholder_count//2)
                self.__page = self.__page.replace(
                    card_placeholder, front_cel, 1)
                self.__page = self.__page.replace(
                    card_placeholder, back_cel, 1)
                card_placeholder_count -= 2

            if card_placeholder_count == 0:
                self.__unziped_template_content = self.__unziped_template_content.replace(
                    templates.PAGE_PLACEHOLDER, self.__page + templates.PAGE_PLACEHOLDER)
                with open(self.__unziped_template_content_file, 'w') as content_file:
                    content_file.write(self.__unziped_template_content)
                self.__page = None

    def __gen_front_cel(self, image_path):
        image_realpath = os.path.join(self.images_store, image_path)
        shutil.copy(image_realpath, self.__unziped_templace_pictures_dir)
        image_name = os.path.basename(image_path)
        return templates.FRONT_CEL_TMP.format(imageName=image_name)

    def __gen_meta_data(self, country_code, country_lang, main_info):
        return '{} / {} / {} / {} ({}-{}, {}, {})'.format(
            main_info['Capital city'], main_info['Population'], main_info['Total area'], main_info['GDP'],
            country_code, country_lang, main_info['Calling code'], main_info['Internet TLD']
        )

    def __gen_back_cel(self, table_name, header, translated_texts, footer):
        return templates.BACK_CEL_TMP.format(backCelTableName=table_name,
                                             header=header,
                                             text0=translated_texts[0],
                                             text1=translated_texts[1],
                                             text2=translated_texts[2],
                                             text3=translated_texts[3],
                                             text4=translated_texts[4],
                                             text5=translated_texts[5],
                                             text6=translated_texts[6],
                                             text7=translated_texts[7],
                                             text8=translated_texts[8],
                                             text9=translated_texts[9],
                                             text10=translated_texts[10],
                                             text11=translated_texts[11],
                                             footer=footer
                                             )

    def close_spider(self, spider):
        if self.__page:
            self.__unziped_template_content = self.__unziped_template_content.replace(
                templates.PAGE_PLACEHOLDER, self.__page + templates.PAGE_PLACEHOLDER)
            with open(self.__unziped_template_content_file, 'w') as content_file:
                content_file.write(self.__unziped_template_content)

        cwd = os.getcwd()
        os.chdir(self.__unziped_templace_dir)
        output_file = os.path.join(
            self.project_root, "output", "output{}.odt".format(self.__random_str))
        subprocess.run('zip -r {} *'.format(output_file),
                       shell=True, stdout=subprocess.DEVNULL)
        os.chdir(cwd)

        shutil.rmtree(self.__unziped_templace_dir, ignore_errors=True)
