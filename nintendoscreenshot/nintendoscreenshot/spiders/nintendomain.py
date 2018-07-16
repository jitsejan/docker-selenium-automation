# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

BASE_URL = 'http://www.nintendo.com/'

class NintendomainSpider(scrapy.Spider):
    name = 'nintendomain'
    allowed_domains = ['www.nintendo.com']
    start_urls = [BASE_URL]

    def __init__(self, *args, **kwargs):
        super(NintendomainSpider, self).__init__(*args, **kwargs)
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)

    def parse(self, response):
        for elem in response.css('section.new-releases li a'):
            item = {
               'name': elem.css('div[itemprop="name"]::text').extract_first(),
               'releasedate': elem.css('.date::text').extract_first().strip(),
               'link': BASE_URL + elem.xpath('@href').extract_first(),
               'image': elem.css('img::attr(src)').extract_first()
            }
            self.driver.get(item['link'])
            self.driver.save_screenshot(item['name']+'.PNG')
            yield item

    def closed(self, reason):
        self.driver.quit()
