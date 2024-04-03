# Scrapy settings for p24 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = ' '

SPIDER_MODULES = ['p24.spiders']
NEWSPIDER_MODULE = 'p24.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 50
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 1

ROTATING_PROXY_LIST = [
"162.240.75.37:80",
"72.10.160.170:32953",
"72.10.164.178:1075",
"185.217.136.67:1337",
"50.173.182.90:80",
"50.174.216.110:80",
"50.174.214.216:80",
"50.173.140.138:80",
"50.174.145.10:80",
"50.173.140.149:80",
"50.174.7.157:80",
"50.174.214.220:80",
"50.168.210.235:80",
"154.208.10.126:80",
"50.207.199.82:80",
"24.205.201.186:80",
"50.204.219.224:80",
"50.172.75.123:80",
"50.172.75.126:80",
"50.217.226.43:80",
"50.173.140.145:80",
"50.172.23.10:80",
"50.207.199.87:80",
"50.223.38.6:80",
"50.218.57.69:80",
"50.204.190.234:80",
"50.175.212.66:80",
"50.231.172.74:80",
"50.170.90.34:80",
"35.185.196.38:3128",
"50.218.57.68:80",
"50.174.214.222:80",
"50.168.72.114:80",
"50.220.168.134:80",
"50.168.72.115:80",
"50.168.163.166:80",
"50.175.212.72:80",
"51.89.14.70:80",
"50.217.226.45:80",
"50.122.86.118:80",
"50.168.72.113:80",
"50.218.57.71:80",
"50.172.75.125:80",
"50.174.145.14:80",
"50.168.210.234:80",
"50.145.6.38:80",
"82.64.77.30:80",
"50.175.212.79:80",
"50.172.75.127:80",
"50.173.140.150:80",
"50.172.39.98:80",
"50.223.239.166:80",
"50.217.226.47:80",
"50.174.214.206:80",
"50.174.7.153:80",
"50.168.163.183:80",
"50.174.145.11:80",
"50.222.245.50:80",
"50.221.230.186:80",
"50.207.199.81:80",
"50.174.7.158:80",
"50.207.199.80:80",
"50.223.239.183:80",
"216.137.184.253:80",
"50.202.75.26:80",
"50.168.72.119:80",
"50.175.212.74:80",
"50.174.145.13:80",
"50.207.199.86:80",
"50.170.90.24:80",
"50.172.75.120:80",
"41.207.187.178:80",
"50.174.7.154:80",
"50.231.104.58:80",
"68.188.59.198:80",
"50.169.135.10:80",
"50.168.210.239:80",
"50.239.72.18:80",
"50.217.226.42:80",
"50.170.90.30:80",
"50.223.239.190:80",
"50.174.214.217:80",
"50.174.145.8:80",
"50.217.226.40:80",
"50.222.245.41:80",
"50.218.57.66:80",
"50.239.72.17:80",
"50.174.7.159:80",
"50.171.68.130:80",
"20.205.61.143:80",
"50.168.210.232:80",
"50.207.199.83:80",
"50.172.218.160:80",
"50.173.140.151:80",
"50.174.216.104:80",
"50.222.245.42:80",
"50.170.90.26:80",
"50.174.145.12:80",
"50.170.90.28:80",
"50.222.245.47:80",
"37.130.26.102:8081",
"51.195.115.18:8080",
"121.101.131.67:1111",
"47.254.90.125:3128",
"93.171.220.229:8888",
"103.148.130.3:7777",
"5.135.83.214:80",
"122.160.30.99:80",
"159.69.230.19:80",
"67.43.227.227:17629",
"116.203.28.43:80",
"47.56.110.204:8989",
"213.91.232.94:8080",
"138.197.102.119:80",
"176.65.240.15:80",
"185.247.18.200:8888",
"133.18.234.13:80",
"87.237.239.57:3128",
"51.254.78.223:80",
"64.76.43.115:999",
"82.65.220.152:80",
"202.51.68.205:80",
"79.137.194.110:80",
"123.30.154.171:7777",
"183.100.14.134:8000",
"178.128.113.118:23128",
"173.213.71.7:80",
"41.89.16.6:80",
"167.71.5.83:3128",
"41.204.63.118:80",
"162.223.94.166:80",
"116.125.141.115:80",
"72.10.160.94:5771",
"72.10.160.90:20931",
"41.111.198.108:80",
"198.44.255.5:80",

]

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
   'Accept-Language': 'en-US,en;q=0.5',
   "Referer":"http://www.google.com/"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'p24.middlewares.P24SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'p24.middlewares.P24DownloaderMiddleware': 543,
  
}
USER_AGENTS = [
   
    ('Mozilla/5.0 (X11; Linux x86_64)'
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/57.0.2987.110 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Linux x86_64) '
     'AppleWebKit/537.36 (KHTML, like Gecko) '
     'Chrome/61.0.3163.79 '
     'Safari/537.36'),  # chrome
    ('Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:55.0) '
     'Gecko/20100101 Firefox/55.0'),  # firefox
     ('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; MDDCJS)'),
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'p24.pipelines.P24Pipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
