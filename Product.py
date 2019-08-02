# -*- coding: utf-8 -*-
#import requests
import re
from selenium import webdriver


"""
get product id
"""



def find_product_id():
    product_ids = []
    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")

    for i in range(1, 3):
        jd_url = 'https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&page='+str(i)
        driver.get(jd_url)
        #print(driver.page_source)
        # with open('source.txt',  "w+") as f:
        #     f.write(driver.page_source)
        # return
        lis = driver.find_elements_by_class_name('gl-item')
        for li in lis:
            try:
                id = li.get_attribute('data-pid')
                print(id)
                product_ids.append(str(id))
            except:
                print("An exception occurred")

    return product_ids


ids = find_product_id()
print(ids)
