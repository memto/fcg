# https://www.usnews.com/news/best-countries/education-full-list

import json
import re
import scrapy


class CountriesRankingSpider(scrapy.Spider):
    name = "countriesranking"
    start_urls = [
        'https://www.usnews.com/news/best-countries/education-full-list']

    def parse(self, response):
        script_tag_with_data = response.xpath(
            '//script[contains(text(), \'__APOLLO_STATE__\')]').extract_first()
        data = re.findall(r'\s*window.__APOLLO_STATE__\s*=\s*(.+?)\n', script_tag_with_data)
        json_object = json.loads(data[0])
        rankings = json_object['$ROOT_QUERY.context']['rankings']
        countries = rankings['json']
        countries_rankings = {}
        for country in countries:
            country_summary = country['country_summary']
            name = country_summary['name'].lower()
            if 'united' in name or 'republic' in name or name == 'netherlands' or name == 'philippines':
                name = 'the ' + name
        
            overal_rank = country_summary['overall_rank']
            countries_rankings[name] = overal_rank

        print(countries_rankings)
