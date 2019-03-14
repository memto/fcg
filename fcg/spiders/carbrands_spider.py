import scrapy

class FlagsSpider(scrapy.Spider):
  name = "carbrands"
  start_urls = ['http://www.carlogos.org/']

  def parse(self, response):
    # for link in response.xpath('//dl[@class=\'counav\']/dd/a'):
    for link in response.xpath('//dl[@class=\'counav\']/dd/a')[:1]:
      yield response.follow(link, self.parse_country_page)

  def parse_country_page(self, response):
    # first logo1 dl in main-l div, first a in dd 
    # for link in response.xpath('//div[@class=\'main-l\']/dl[@class=\'logo1\'][1]/dd/a[1]'):
    for link in response.xpath('//div[@class=\'main-l\']/dl[@class=\'logo1\'][1]/dd/a[1]')[:1]:
      yield response.follow(link, self.parse_brand_page)

  def parse_brand_page(self, response):
    image_url = response.xpath('//div[@class=\'content\']/p[1]/a/@href').extract_first()
    info_fields = ["Founded", "Founder", "Headquarters", "Slogan", "Subsidiaries", "Official Site", "Overview"]
    info_sel = response.xpath('//div[@class=\'content\']/table/tbody')
    header = info_sel.xpath('tr[1]/th/text()').extract_first()
    field_sels = response.xpath('//div[@class=\'content\']/table/tbody/tr')[1:]

    brand_info = {}
    for field_sel in field_sels:
      field = field_sel.xpath('td[1]/text()').extract_first()
      value = field_sel.xpath('td[2]/text()').extract_first()

      brand_info[field] = value

    # print(image_url)
    # print(header)
    # print(brand_info)

    pass
    # yield CountryFlag(title=title, image_urls=[image_url], main_info=main_info, iso_alpha2_country_code=iso_alpha2_country_code)