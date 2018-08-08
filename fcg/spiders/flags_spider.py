import scrapy

from fcg.items import CountryFlag


class FlagsSpider(scrapy.Spider):
    name = "flags"

    scheme = 'http://'

    start_urls = ['http://flagpedia.net/index']

    def parse(self, response):
        # for link in response.xpath('//td/a')[:1]:
        for link in response.xpath('//td/a'):
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
        descriptions = main_info_selector.xpath('dd/text()').extract()
        for term, des in zip(terms, descriptions):
            if term.strip() in expected_info:
                main_info.append((term.strip(), des.strip()))
        yield CountryFlag(title=title, image_urls=[image_url], main_info=main_info)
