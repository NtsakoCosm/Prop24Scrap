import scrapy
import re
import time
import random

def extract_number(text):
    cleaned = text.replace("\\r\\n",'').strip()
    if cleaned != '' :
        return cleaned
    

def remove_tags(text):
 
  return re.sub(r"<.*?>", "", text)
class PropScrapper(scrapy.Spider):

  name = "propscrap"
  allowed_domains = ["www.property24.com/"]
  start_urls = ['https://www.property24.com/houses-for-sale/gauteng/1?sp=eszf%3d100%26bd%3d1%26bth%3d1%26ps%3d1' ]
  indices = [f"https://www.property24.com/houses-for-sale/gauteng/1/p{pno}?sp=eszf%3d100%26bd%3d1%26bth%3d1%26ps%3d1" for pno in range(2,10)]

  for i in indices :
    start_urls.append(i)
 
  prices_dump =[]
  def parse(self, response):
    
    #CSS SELECTORS
    bedrooms = response.css(".p24_featureDetails:nth-child(1)").extract()
    bathroom = response.css(".p24_featureDetails:nth-child(2)").extract()
    parking = response.css(".p24_featureDetails~ .p24_featureDetails+ .p24_featureDetails").extract()
    location = response.css(".p24_location").extract()
    size = response.css(".p24_size span").extract()
    price = response.css(".js_listingResultsContainer .p24_price::text").extract()
    price = [extract_number(p) for p in price if extract_number(p) != None]
   
    #Cleaned Data
    bedrooms  = [extract_number(remove_tags(b)) for b in bedrooms]
    bathrooms = [extract_number(remove_tags(b)) for b in bathroom]
    parkings =[extract_number(remove_tags(b)) for b in parking]
    sizes = [extract_number(remove_tags(b)) for b in size]
    locations = [remove_tags(loc) for loc in location]

    time.sleep(random.randint(5, 10)) 

    yield {"price":price,"Content count": len(price),"bedrooms":bedrooms,
    "bed":len(bedrooms),"loc":locations,"loclen":len(locations),"bathrooms":bathrooms,
    "bathroomlen":len(bathrooms),"size":sizes,"sizelen":len(sizes),"parking":parkings,"plen":len(parkings)
    }