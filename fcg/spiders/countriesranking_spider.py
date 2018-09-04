# https://www.usnews.com/news/best-countries/education-full-list

import json
import re
import scrapy
import pprint


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
        ranked_countries = {}
        for country in countries:
            country_summary = country['country_summary']
            name = country_summary['name'].lower()
            if 'united' in name or 'republic' in name or name == 'netherlands' or name == 'philippines':
                name = 'the ' + name
        
            # overal_rank = country_summary['overall_rank']
            subranking_rank = country['subranking_rank']
            countries_rankings[name] = subranking_rank
            ranked_countries[subranking_rank] = name

        print('COUNTRIES_RANKINGS_BY_EDU={')
        for rank in sorted(ranked_countries):
            print('"{}": {},'.format(ranked_countries[rank], rank))
        print('}')
