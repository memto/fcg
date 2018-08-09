import scrapy

from fcg.items import CountryFlag


class FlagsSpider(scrapy.Spider):
    name = "flags"

    scheme = 'http://'

    start_urls = ['http://flagpedia.net/index']

    def parse(self, response):
        # for link in response.xpath('//td[@class=\'td-country\']/a')[:4]:
        for link in response.xpath('//td[@class=\'td-country\']/a'):
            yield response.follow(link, self.parse_page)

    def parse_page(self, response):
        title = response.xpath('//article/h1/text()')[0].extract()
        image_url = response.xpath(
            '//article/p[@id=\'flag-detail\']/img/@src').extract_first()
        image_url = self.scheme + image_url.strip('/')

        main_info = []
        expected_info = ['Country', 'Capital city',
                         'Population', 'Total area', 'Code']
        main_info_selector = response.xpath('//dl')[0]
        terms = main_info_selector.xpath('dt/text()').extract()
        descriptions_selector = main_info_selector.xpath('dd')
        for term, des_sel in zip(terms, descriptions_selector):
            if term.strip() in expected_info:
                # some description dont have text() so here need match for
                # text() or first-child's text then extract_first()
                main_info.append((term.strip(), des_sel.xpath(
                    'text()|*[1]/text()').extract_first().strip()))

        main_info = dict(main_info)
        iso_alpha2_country_code = {main_info['Code']: main_info['Country']}
        yield CountryFlag(title=title, image_urls=[image_url], main_info=main_info, iso_alpha2_country_code=iso_alpha2_country_code)
