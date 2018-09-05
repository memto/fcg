import scrapy

from fcg.items import CountryFlag

from fcg.helpers.constants import COUNTRIES_RANKINGS_BY_EDU

class FlagsSpider(scrapy.Spider):
    name = "flags"

    scheme = 'http://'

    start_urls = ['http://flagpedia.net/index']

    def parse(self, response):
        # yield scrapy.Request(url='http://flagpedia.net/south-korea', callback=self.parse_page)
        # for link in response.xpath('//td[@class=\'td-country\']/a')[:6]:

        ranked_countries = {}
        for link in response.xpath('//td[@class=\'td-country\']/a'):
            pass
            country = link.xpath('text()').extract_first()
            country = country.lower()
            if 'china' in country:
                country = 'china'

            if country in COUNTRIES_RANKINGS_BY_EDU:
                country_rank = COUNTRIES_RANKINGS_BY_EDU[country]
                ranked_countries[country_rank] = link

        sorted_ranks = sorted(ranked_countries)
        for rank in sorted_ranks[:4]:
            link = ranked_countries[rank]
            yield response.follow(link, self.parse_page, meta={'Edu rank': rank})

    def parse_page(self, response):
        title = response.xpath('//article/h1/text()')[0].extract()
        image_url = response.xpath(
            '//article/p[@id=\'flag-detail\']/img/@src').extract_first()
        image_url = self.scheme + image_url.strip('/')

        main_info = []
        expected_info = ['Country', 'Capital city',
                         'Population', 'Total area', 'GDP', 'Code', 'Calling code', 'Internet TLD']
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
        main_info['Edu rank'] = response.meta['Edu rank']
        yield CountryFlag(title=title, image_urls=[image_url], main_info=main_info, iso_alpha2_country_code=iso_alpha2_country_code)
