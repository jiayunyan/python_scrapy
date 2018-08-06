# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        dangdang = pymysql.connect(host="localhost", user="root", passwd="yanjiayun0629",db="dangdang",charset='utf8')
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            link=item["link"][i]
            comment=item["comment"][i]
            sql="insert into goods(title,link,comment) values ('"+title+"','"+link+"','"+comment+"')"
            print(sql)
            dangdang.query(sql)
        dangdang.commit()
        dangdang.close()
        return item
