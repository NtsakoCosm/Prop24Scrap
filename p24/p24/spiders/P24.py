import scrapy
class MySpider(scrapy.Spider):
  name = "product_scraper"
  start_urls = ['https://www.property24.com/houses-for-sale/gauteng/1/' ]
  indices = [f"'https://www.property24.com/houses-for-sale/gauteng/1/p{pno}" for pno in range(2,4)]
  def parse(self, response):
    # Extract product titles using CSS selectors
    product_titles = response.css('.product-title::text').extract()
    
    # Print the extracted titles
    for title in product_titles:
      print(title.strip())