# -*- coding: utf-8 -*-
import scrapy
import re

class UfcStatsSpider(scrapy.Spider):
    name = 'ufc-stats'
    allowed_domains = ['http://www.ufcstats.com/statistics/events/completed']
    start_urls = ['http://www.ufcstats.com/statistics/events/completed']
	
    def parse(self, response):
        titles = response.xpath('//a[@class="b-link b-link_style_black"]/text()').extract()
        for title in titles:
            yield {'Title': title.strip()}

