# -*- coding: utf-8 -*-
<<<<<<< HEAD

=======
#修改调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
#开启去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# REDIS_URL = 'redis://@localhost:6379'
SCHEDULER_PERSIST = True
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
# Scrapy settings for dongqiudi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'dongqiudi'

SPIDER_MODULES = ['dongqiudi.spiders']
NEWSPIDER_MODULE = 'dongqiudi.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
<<<<<<< HEAD
#USER_AGENT = 'dongqiudi (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32
=======
# 抓取目标网站时使用的USER_AGENT
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'


# Obey robots.txt rules
# 是否遵循robots.txt规则
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 并发请求数量
CONCURRENT_REQUESTS = 4
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
<<<<<<< HEAD
#DOWNLOAD_DELAY = 3
=======
# 请求延迟的时间（秒）,0为没有延迟
DOWNLOAD_DELAY = 0




>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
<<<<<<< HEAD
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
=======
#是否使用Cookies
COOKIES_ENABLED = False




# Disable Telnet Console (enabled by default)
# 是否使用telnet控制台  默认启用
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'accept': "image/webp,image/apng,image/*,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.8",
    'connection': "keep-alive",
    'host': "collector.githubapp.com",
    'referer': "https://github.com/Bestlzh/spider",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
    'cache-control': "no-cache",
}
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
<<<<<<< HEAD
#    'dongqiudi.middlewares.DongqiudiSpiderMiddleware': 543,
=======
#    'qianmu.middlewares.QianmuSpiderMiddleware': 543,
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
<<<<<<< HEAD
#    'dongqiudi.middlewares.MyCustomDownloaderMiddleware': 543,
=======
#    'qianmu.middlewares.MyCustomDownloaderMiddleware': 543,
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
<<<<<<< HEAD
#ITEM_PIPELINES = {
#    'dongqiudi.pipelines.DongqiudiPipeline': 300,
#}
=======
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline':300,
   # 'dongqiudi.pipelines.CheckPipeline': 301,
   'dongqiudi.pipelines.DongqiudiPipeline': 301,
   # 'dongqiudi.pipelines.MysqlPipleine': 302,
}
>>>>>>> defaf6a73cc03eeb17362791485a9c754889df31

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
