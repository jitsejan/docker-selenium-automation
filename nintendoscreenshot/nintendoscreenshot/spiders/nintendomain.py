# -*- coding: utf-8 -*-
import scrapy

BASE_URL = 'http://www.nintendo.com/'

class NintendomainSpider(scrapy.Spider):
    name = 'nintendomain'
    allowed_domains = ['www.nintendo.com']
    start_urls = [BASE_URL]

    def parse(self, response):
        for elem in response.css('section.new-releases li a'):
            yield {
               'name': elem.css('div[itemprop="name"]::text').extract_first(),
               'releasedate': elem.css('.date::text').extract_first().strip(),
               'link': BASE_URL + elem.xpath('@href').extract_first(),
               'image': elem.css('img::attr(src)').extract_first()
            }