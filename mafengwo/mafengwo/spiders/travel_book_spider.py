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

class TravelSpider(BaseSpider):

    urlList         = 'mfw_url'
    base_url        = "http://www.mafengwo.cn"
    name            = "MFWTravelBook"
    allowed_domain  = ["mafengwo.cn"]
    start_urls      = ["http://www.mafengwo.cn/gonglve/"]
    top_url         = "http://www.mafengwo.cn/mdd/ajax_book_search.php?act=get_more&keyword=mdd-0-0-0-"

    def __init__(self) :
        self.urlListObject   = urlList()
        self.urlListObject.delList(self.urlList)

    # parse next_link
    def parse(self, response):
        responseSelector = HtmlXPathSelector(response)
        init_url = responseSelector.select(u'//div[@class="gl_list"]/a/@href').extract()
        for i in init_url: self.urlListObject.pushLink(self.urlList ,self.base_url + i)
        for i in range(2,20):
            next_link = self.top_url + str(i)
            yield Request(url = next_link , callback = self.detail_parse)

    # get sub url
    def detail_parse(self,response):
        print "crawled last page : " + response.url
        json = json_mod.loads(response.body.decode('iso-8859-1'))
        if json['ret'] == "1":
            for i in json['data']:
                for j in i : self.urlListObject.lpushLink(self.urlList ,self.base_url + j["url"])
        else: print "response.url not be used !"
        a = self.urlListObject.lenList(self.urlList)
        print a


