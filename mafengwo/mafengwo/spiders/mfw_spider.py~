#!/usr/bin/python
#-*-coding:utf-8-*-
import time
from pprint import pprint
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from redisList import urlList
from urlparse import urlparse, urljoin
import json as json_mod
from mafengwo.items import MafengwoItem

class CrawlSpider(BaseSpider):

    urlList         = 'mfw_url'
    base_url        = "http://www.mafengwo.cn"
    name            = "crawl_spider"
    allowed_domain  = ["mafengwo.cn"]
    start_urls      = ["http://www.mafengwo.cn/gonglve/"]

    def __init__(self) :
        self.urlListObject   = urlList()

    # parse next_link
    def parse(self, response):

        if self.urlListObject.lenList > 0 :
            next_link = self.urlListObject.rpopLink(self.urlList)
            yield Request(url = next_link , callback = self.detail_parse)

    # get sub url
    def detail_parse(self,response):
        responseSelector = HtmlXPathSelector(response)
        Mafengwo_item = MafengwoItem()
        #init_url = responseSelector.select(u'//div[@class="gl_list"]/a/@href').extract()
        yield Mafengwo_item


