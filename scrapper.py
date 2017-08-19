#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:42:55 2017

@author: Ayush Vatsyayan
"""

from product_crawler import ProductCrawler
from product_retriever import ProductRetriever
import time
import pandas as pd

products = ProductCrawler().get_products()
retriever = ProductRetriever()




# get detail of each product
available_prds = []

for product in products:
    prd_id = product['id']
    
    details = retriever.get_product_details(prd_id)
    if details['stockAvailability'].lower() != 'out of stock':
        print('-----')
        print(product)
        print(details)
        available_prds.append(product)
    else:
        print('skipping:',product['name'])
        
    time.sleep(1)
    
df = pd.DataFrame(available_prds)
df = df[['id','name','discounted_price','non_discounted_price']]
df.to_csv('tmp.csv', index=False)

