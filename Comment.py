# -*- coding: utf-8 -*-
#import requests
import re
import time
import json
import mysql.connector
from selenium import webdriver

"""
get comments
"""


def find_comment_by_id(product_id):
    driver = webdriver.PhantomJS(executable_path="/usr/local/bin/phantomjs")
    comments = []
    jd_url = 'https://item.jd.com/{}.html#comment'.format(str(product_id))

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="web_crawler"
    )

    driver.get(jd_url)
    time.sleep(30)
    for i in range(1, 10):
        try:
            #driver.implicitly_wait(60)
            path = ".//div[@class ='ui-page']/a[@ rel='{}']".format(str(i))
            #path = ".//div[@class ='ui-page']/a[@ rel='2']"
            driver.find_element_by_xpath(path).click()
            time.sleep(10)
            with open('comment.txt', "w+") as f:
                f.write(driver.page_source)
            lis = driver.find_elements_by_class_name('order-info')
            for li in lis:
                spans = li.find_elements_by_tag_name('span')
                comments.append({'color': spans[0].text, 'size': spans[1].text})
                mycursor = mydb.cursor()
                sql = "INSERT INTO comments (size, color, created_at) VALUES (%s, %s, %s)"
                val = (spans[1].text, spans[0].text, spans[2].text)
                mycursor.execute(sql, val)
            mydb.commit()
            print(comments)
            comments = []
        except Exception as e:
            print("An exception occurred {}".format(i))
            print(e)


#data = find_comment_by_id(100003464155)
# f = open('comment.txt',  "w+")
# f.write(str(data))
# f.close()
# print(data)



