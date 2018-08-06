# -*- coding:utf-8 -*-
import urllib.request
import csv
import os
from lxml import etree
url="https://xl.16888.com/s/127692/"
html = urllib.request.urlopen(url)
content = html.read().decode()
html.close()
# print(content)

selector = etree.HTML(content,parser=etree.HTMLParser(encoding='utf-8'))
# print(selector)
table_header = selector.xpath('//table//tr/th/text()')


table_header[-1] = table_header[-1].replace('在', '').replace('排名', '')
table_header.insert(-2, '在所占车型中排名')
car_type = table_header[-1]
table_header[-1] = '所属级别'
# print(car_type)
# print(table_header)

num_data = selector.xpath('//div[@class="xl-data-pageing lbBox"]/span/text()')
num = int(num_data[0].replace('共', '').replace('条数据', ''))
# print(num)
content = []
for i in range(num):
    part_content = selector.xpath('//table//tr[{}]/td/text()|//table//tr[{}]/td/a/text()'.format(i + 2, i + 2))
    part_content.append(car_type)
    content.append(part_content)
# print(content)
# os.mkdir(r'car_message')
# 切换至创建的文件夹目录下
# os.chdir(r'car_message')
# for i in range(len(table_header)):
#     table_header[i] = bytes(table_header[i].encode('utf-8'))

print(table_header)
with open('changan_cs55.csv', 'w') as f:
    writer = csv.writer(f, dialect='excel')
    writer.writerow(table_header)
    for i in content:
        writer.writerow(i)