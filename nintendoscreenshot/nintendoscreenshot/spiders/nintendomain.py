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
        self.driver.get(BASE_URL)
        self.driver.get_screenshot_as_file('screenshot.png')

    def parse(self, response):
        driver = webdriver.Remote("http://localhost:4444/wd/hub", DesiredCapabilities.CHROME)
        driver.get('http://prod.jitsejan.com:8080')
        driver.save_screenshot('vue_frontpage.png')
        for elem in response.css('section.new-releases li a'):
            yield {
               'name': elem.css('div[itemprop="name"]::text').extract_first(),
               'releasedate': elem.css('.date::text').extract_first().strip(),
               'link': BASE_URL + elem.xpath('@href').extract_first(),
               'image': elem.css('img::attr(src)').extract_first()
            }

    def closed(self, reason):
        self.driver.quit()