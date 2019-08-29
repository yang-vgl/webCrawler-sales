# -*- coding: utf-8 -*-
#import requests
import re
from selenium import webdriver
import mysql.connector

"""
get product id
"""



def find_product_id():

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="web_crawler"
    )

    product_ids = []
    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")

    for i in range(1, 10):
        jd_url = 'https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&page='+str(i)
        driver.get(jd_url)
        lis = driver.find_elements_by_class_name('gl-item')
        for li in lis:
            try:
                id = li.get_attribute('data-pid')
                print(id)
                product_ids.append(str(id))
                mycursor = mydb.cursor()
                sql = "INSERT INTO products (product_id) VALUES (%s)"
                mycursor.execute(sql, [id])
                mydb.commit()
            except Exception as e:
                print(e)

    return product_ids


ids = find_product_id()
print(ids)
