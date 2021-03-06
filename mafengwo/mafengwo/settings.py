# Scrapy settings for mafengwo project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mafengwo'

SPIDER_MODULES = ['mafengwo.spiders']
NEWSPIDER_MODULE = 'mafengwo.spiders'

#control the speed of  download 
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3.0
AUTOTHROTTLE_MAX_DELAY = 10.0

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mafengwo (+http://www.yourdomain.com)'
