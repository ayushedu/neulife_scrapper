#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:19:33 2017

@author: Ayush Vatsyayan
"""
import requests
import json

class ProductRetriever:
    """ Retrieve product detail from site"""
    
    def __init__(self):
        self.url = "http://www.neulife.com/neucom/ShoppingCart/ProductDetails_AttributeChange"
        self.headers = {'User-Agent':'Mozilla/5.0'}

    def get_product_details(self, product_id, validate_attr=False):
        """ Get product details such as price and availability """
        
        req_params = {"productId":product_id, "validateAttributeConditions":validate_attr}
        session = requests.Session()
        resp = session.post(self.url, headers=self.headers, data=req_params)
        session.close()
        
        # read json here
        result = json.loads(resp.text)
        return result
    
 
#print(ProductRetriever().get_product_details(4096))
