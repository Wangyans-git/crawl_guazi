# -*- coding: utf-8 -*-

# Scrapy settings for guazi_scrapy_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# scrapybot
BOT_NAME = 'guazi_scrapy_project'

# 解析器模块
SPIDER_MODULES = ['guazi_scrapy_project.spiders']
NEWSPIDER_MODULE = 'guazi_scrapy_project.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 默认请求头，也可以在中间件里设置
# USER_AGENT = 'guazi_scrapy_project (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 设置robots.txt为True不可被抓取
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 由于当前代理每秒只能发送5个请求，所以设置为5
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 每个请求的等待时间，限制爬行速度
DOWNLOAD_DELAY = 0.2
# 代理请求数据，默认为180秒
DOWNLOAD_TIMEOUT = 10
# 是否进行重试
RETRY_ENABLED = True
# 重试的次数
RETRY_TIMES = 3

# The download delay setting will honor only one of:
# 对单个网站并发请求的默认值为8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 对单个ip并发请求最大值，如果非0，这忽略上面的设定
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 提交到下载器中间件之前的spider中间件
# SPIDER_MIDDLEWARES = {
#    'guazi_scrapy_project.middlewares.GuaziScrapyProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# ---------------------中间件------------------------
DOWNLOADER_MIDDLEWARES = {
   # 'guazi_scrapy_project.middlewares.GuaziScrapyProjectDownloaderMiddleware': 543,
   'guazi_scrapy_project.middlewares.guazi_downloader_middleware': 500,
   'guazi_scrapy_project.middlewares.my_useragent': 501,
   # 'guazi_scrapy_project.middlewares.my_proxy': 502,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# 基于信号的中间件
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ---------------------pipelines------------------------
ITEM_PIPELINES = {
   'guazi_scrapy_project.pipelines.GuaziScrapyProjectPipeline': 300,
}

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
