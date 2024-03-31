import scrapy
class PropScrapper(scrapy.Spider):
  name = "product_scraper"
  start_url = ['https://www.property24.com/houses-for-sale/gauteng/1/' ]
  indices = [f"'https://www.property24.com/houses-for-sale/gauteng/1/p{pno}" for pno in range(2,4)]

  def parse(self, response):
    # Extract product titles using CSS selectors
    price = response.css('p24_price').extract()
    
    # Print the extracted titles
    print(price)

    yield {"price":price}