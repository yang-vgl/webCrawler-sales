# -*- coding: utf-8 -*-
#import requests
import re
import time
import json
from selenium import webdriver


"""
get product id
"""



def find_comment_by_id(product_id):
    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
    color = []
    size = []
    jd_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv48&productId=27344400591&score=0&sortType=5&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1'
    driver.get(jd_url)
    time.sleep(60)
    with open('comment_json.txt', "w+") as f:
        f.write(driver.page_source)
    return
    for i in range(2, 20):
        try:
            #path = ".//div[@class ='ui-page']/a[@ rel='{}']".format(str(i))
            path = ".//div[@class ='ui-page']/a[@ rel='2']"
            driver.find_element_by_xpath(".//div[@class ='ui-page']/a[@ rel='2']").click()
            time.sleep(60)
            with open('comment.txt', "w+") as f:
                f.write(driver.page_source)
            return
            lis = driver.find_elements_by_class_name('order-info')
            for li in lis:
                spans = li.find_elements_by_tag_name('span')
                color.append(spans[0].text)
                size.append(spans[1].text)
        except:
            print("An exception occurred {}".format(i))
    return {'color': color, 'size': size}


data = find_comment_by_id(27344400591)
# f = open('comment.txt',  "w+")
# f.write(str(data))
# f.close()
print(data)



