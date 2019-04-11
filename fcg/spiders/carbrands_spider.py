import scrapy
import html2text

from fcg.items import CarBrand

class FlagsSpider(scrapy.Spider):
  name = "carbrands"
  start_urls = ['http://www.carlogos.org/']


  def parse(self, response):
    for link in response.xpath('//dl[@class=\'counav\']/dd/a'):
    # for link in response.xpath('//dl[@class=\'counav\']/dd/a')[:1]:
      yield response.follow(link, self.parse_country_page)

  def parse_country_page(self, response):
    country = response.xpath('//div[@class=\'main-l\']/div[@class=\'title1\']/h1/text()').extract_first()
    country = country.replace(' Car Brands', '')
    if 'Other' in country:
      country_sels = response.xpath('//div[@class=\'main-l\']/div[@class=\'subtitle\']')
      brands_sels = response.xpath('//div[@class=\'main-l\']/dl[@class=\'logo1\']')
      for country_sel, brands_sel in zip(country_sels, brands_sels):
        country = country_sel.xpath('strong/text()').extract_first()
        for idx, link in enumerate(brands_sel.xpath('dd/a[1]')):
          yield response.follow(link, self.parse_brand_page, meta={'country': country, 'idx': idx})  
    else:
      # first logo1 dl in main-l div, first a in dd 
      for idx, link in enumerate(response.xpath('//div[@class=\'main-l\']/dl[@class=\'logo1\'][1]/dd/a[1]')):
      # for link in response.xpath('//div[@class=\'main-l\']/dl[@class=\'logo1\'][1]/dd/a[1]')[:3]:
        yield response.follow(link, self.parse_brand_page, meta={'country': country, 'idx': idx})

  def parse_brand_page(self, response):
    image_url = response.xpath('//div[@class=\'content\']/p[1]/a/@href').extract_first()
    if image_url == None or image_url[0] == None:
      image_url = response.xpath('//div[@class=\'content\']/p[1]/img/@src').extract_first()
    info_fields = ["Founded", "Founder", "Headquarters", "Slogan", "Subsidiaries", "Official Site", "Overview"]
    info_sel = response.xpath('//div[@class=\'content\']/table/tbody')
    brand = info_sel.xpath('tr[1]/th/text()').extract_first().replace(' Information', '')
    field_sels = response.xpath('//div[@class=\'content\']/table/tbody/tr')[1:]

    brand_info = {}
    for field_sel in field_sels:
      field = field_sel.xpath('td[1]/text()').extract_first()
      for info_field in info_fields:
        if info_field in field:
          field = info_field

      import html2text
      converter = html2text.HTML2Text()
      converter.ignore_links = True

      value = field_sel.xpath('td[2]').extract_first()
      value = converter.handle(value).strip('\n')

      brand_info[field] = value

    yield CarBrand(country=response.meta['country'], name=brand, idx=response.meta['idx'], image_urls=[image_url], info=brand_info)