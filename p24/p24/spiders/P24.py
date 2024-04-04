import scrapy
import re
import time
import random
import asyncio
from scrapy.http import TextResponse
import requests

from avproxyrotate import start_avast
import dns.resolver
import pyuac


def rotateips():
  dns_resolver = dns.resolver.Resolver()
  if not pyuac.isUserAdmin():
          pyuac.runAsAdmin()
          start_avast(

                  sleeptime_reconnect=3,

                  hotkey_change="ctrl+alt+m",  # Changes the proxy server via hotkey

                  hotkey_stop="ctrl+alt+n",  # Kills the script

                  dns=f"{dns_resolver.nameservers[0]}",

                  rotate_server_each_n_seconds=5,  # changes IP each n seconds

                  clear_used_ips_after_n_seconds=3600,  # clears already used IPs during proxy rotation

                  path_app=r"C:\Program Files\Avast Software\SecureLine VPN",  # install folder

                  path_data=r"C:\ProgramData\Avast Software\SecureLine VPN",  # App data - IPs and tlsdomain are extracted from log files, that means, before you use this function, you have to connect to some avast servers using their app

              )


def extract_number(text):
    cleaned = text.replace("\\r\\n",'').strip()
    if cleaned != '' :
        return cleaned
    

def remove_tags(text):
 
  return re.sub(r"<.*?>", "", text)

def keep_link(string):
  pattern = r'src="(.*?)"'

  # Find the link using regex
  match = re.search(pattern, string)

  if match:
      link = match.group(1)
      return link

rotateips()
class PropScrapper(scrapy.Spider):

  name = "propscrap"
  allowed_domains = ["www.property24.com/"]
  start_urls = ['https://www.property24.com/houses-for-sale/gauteng/1?sp=eszf%3d100%26bd%3d1%26bth%3d1%26ps%3d1' ]
  #indices = [f"https://www.property24.com/houses-for-sale/gauteng/1/p{pno}?sp=eszf%3d100%26bd%3d1%26bth%3d1%26ps%3d1" for pno in range(2,10)]

  #for i in indices :
   # start_urls.append(i)
 
  prices_dump =[]
  async def parsecontent(self,link):
    time.sleep(random.randint(1, 30)) 
    resp = requests.get(link)
    resp = TextResponse(body=resp.content, url=link)

    # Using XPath to target the specific div containing the text data
    text_div = resp.xpath('//div[@class="js_readMoreText p24_readMoreText"]')

    # Extracting text from all child p tags within the targeted div
    text_data = text_div.xpath('.//p/text()').getall()

    # Joining the extracted text data into a single string
    full_text = ' '.join(text_data)
    time.sleep(random.randint(1, 3)) 

    return f"---------------{full_text}****-------------------------------------"

  def parse(self, response):
    #Rotating IPs from VPN
    
    
    #CSS SELECTORS
    anchor_selector1 = response.xpath('//a[@class="p24_tileAnchorWrapper"]')
    hrefs1 = [f"https://www.property24.com{ref.xpath('@href').get()}" for ref in anchor_selector1]

    anchor_selector2 = response.xpath('//a[@class="p24_regularTile js_resultTileClickable js_rollover_container "]')
    hrefs2 = [f"https://www.property24.com{ref.xpath('@href').get()}" for ref in anchor_selector2]


    bedrooms = response.css(".p24_featureDetails:nth-child(1)").extract()
    bathroom = response.css(".p24_featureDetails:nth-child(2)").extract()
    parking = response.css(".p24_featureDetails~ .p24_featureDetails+ .p24_featureDetails").extract()
    location = response.css(".p24_location").extract()
    size = response.css(".p24_size span").extract()
    price = response.css(".js_listingResultsContainer .p24_price::text").extract()
    price = [extract_number(p) for p in price if extract_number(p) != None]
   
    #Cleaned Data
    links = hrefs1 + hrefs2
    bedrooms  = [extract_number(remove_tags(b)) for b in bedrooms]
    bathrooms = [extract_number(remove_tags(b)) for b in bathroom]
    parkings =[extract_number(remove_tags(b)) for b in parking]
    sizes = [extract_number(remove_tags(b)) for b in size]
    locations = [remove_tags(loc) for loc in location]
    descriptions = []

    for link in links:
      loop = asyncio.get_event_loop()
      description = loop.run_until_complete(self.parsecontent(link))
       
      descriptions.append(description)
      
    time.sleep(random.randint(3, 10)) 


  
    

    yield {"price":price,"Content count": len(price),"bedrooms":bedrooms,
    "bed":len(bedrooms),"loc":locations,"loclen":len(locations),"bathrooms":bathrooms,
    "bathroomlen":len(bathrooms),"size":sizes,"sizelen":len(sizes),"parking":parkings,"plen":len(parkings),
    "links":  links, "linkslen": len(links),"descriptions": descriptions,"descriptionslen":len(descriptions)


    }