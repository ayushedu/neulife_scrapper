#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:40:19 2017

@author: Ayush Vatsyayan
"""

from selenium import webdriver
from lxml import html

class ProductCrawler:
    """Get list of all products and then get individual details"""
    
    def __init__(self):
        self.browser = webdriver.PhantomJS()
        
        # XPath definitions
        self.xpath_product_div = '//div[@class="product-item"]'
        self.xpath_product_id = "@data-productid"
        self.xpath_product_name = 'div[@class="product-info"]/div/a/text()'
        
        xpath_prices = 'div[@class="details"]/div/div[@class="prices"]/'
        self.xpath_discounted_price = xpath_prices + 'div[@class="product-price discounted-price"]/span/text()'
        self.xpath_non_discounted_price = xpath_prices + 'div[@class="non-discounted-price"]/span/text()'
        
    def get_products(self):
        """get products"""
        self.browser.get("http://www.neulife.com/neucom/whey-proteins?orderby=5")    
        tree = html.fromstring(self.browser.page_source)
        product_div = tree.xpath(self.xpath_product_div)
        
        result = []
        
        for elem in product_div:
            details = {}
            
            try:
                
                details['id'] = elem.xpath(self.xpath_product_id)[0]
                details['name'] = elem.xpath(self.xpath_product_name)[0]
                
                price_dis = elem.xpath(self.xpath_discounted_price)
                price_non_dis = elem.xpath(self.xpath_non_discounted_price)
                
                if price_dis and len(price_dis) > 0:                    
                    details['discounted_price'] = price_dis[0]                

                if price_non_dis and len(price_non_dis) > 0:
                    details['non_discounted_price'] = price_non_dis[0]
                    
                result.append(details)                
            except IndexError as ie:
                print('IndexError while getting details.', ie.reason)
            
        return result