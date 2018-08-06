# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request

class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

    def start_requests(self):
        return [Request('https://accounts.douban.com/login',callback=self.parse,meta={"cookiejar":1})]

    def parse(self, response):
        captchar=response.xpath("//img[@id='captcha_image']/@src").extract()
        url="https://accounts.douban.com/login"
        if len(captchar)>0:
            print("此时有验证码")
            localpath="F:/result/captchar.png"
            urllib.request.urlretrieve(captchar[0],filename=localpath)
            print("查看本地验证码并输入")
            captchar_value=input()
            data = {
                "form_email": "542120155@qq.com",
                "form_password": "yanjiayun0629",
                "captcha-solution": captchar_value,
                "redir": "https://www.douban.com/people/169110190/"
            }


        else:
            print("此时没有验证码")
            data = {
                "form_email": "542120155@qq.com",
                "form_password": "yanjiayun0629",
                "redir": "https://www.douban.com/people/169110190/"
            }
        print("登录中....")
        return [FormRequest.from_response(response,
                                            meta={"cookiejar": response.meta["cookiejar"]},
                                            headers=self.header,
                                            formdata=data,
                                            callback=self.next)]

    def next(self,response):
        print("此时已经登录完成并转到个人中心")
        title=response.xpath("/html/head/title/text()").extract()
        note=response.xpath("//div[@class='note']/text()").extract()
        print(title)
        print(note)