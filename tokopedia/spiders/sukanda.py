# -*- coding: utf-8 -*-
import scrapy


class SukandaSpider(scrapy.Spider):
    name = 'sukanda'
    allowed_domains = ['tokopedia.com']
    start_urls = ['https://www.tokopedia.com/sukandahome/product']
    
    async def parse(self, response):
        for products in response.css('div.prd_container-card'):
            yield {
                'name': products.css('div.prd_link-product-name::text').get(),
                'price': products.css('div.prd_link-product-price::text').get(),
                'discount': products.css('div.prd_badge-product-discount::text').get(),
                'slashPrice': products.css('div.prd_label-product-slash-price::text').get()
            }
