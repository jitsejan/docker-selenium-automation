# -*- coding: utf-8 -*-
import scrapy


class NintendomainSpider(scrapy.Spider):
    name = 'nintendomain'
    allowed_domains = ['www.nintendo.com']
    start_urls = ['http://www.nintendo.com/']

    def parse(self, response):
        pass
