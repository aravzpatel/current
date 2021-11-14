import scrapy


class PageScraper(scrapy.Spider):
  name = "pages"

  def start_requests(self):
    urls=['https://medium.com/transferwise-engineering']

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)

  def parse(self, response):
    for article in response.xpath('//a/h3/parent::*'):
      self.log('New Article')
      title = article.css('h3 div::text').get()
      self.log(title)
      link = article.css('a::attr(href)').get()
      self.log(link)
      sub_text = article.css('div div::text').get()
      self.log(sub_text)
