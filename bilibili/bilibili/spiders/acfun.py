# -*- coding: utf-8 -*-
import scrapy
import json
from bilibili.spiders.Directory import AbsDirectory
from bilibili.items import BilibiliItem
import os
from bilibili.spiders.Ffmpy import get_full
import hashlib
import sys
#sys.path.append(r'/home/mayinghao/bilibili')


class Store:
    file_length = 0
    first_run = 0


class AcfunSpider(scrapy.Spider):
    name = 'acfun'
    allowed_domains = ['www.acfun.cn']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",

                       }

    def __init__(self, list_url=None, *args, **kwargs):
        super(AcfunSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.acfun.cn/v/ac12850247']

        self.start = list_url.split(',')
        global urls
        urls = self.start
        Store.file_length = len(self.start)

    def parse(self, response):
        global title
        print(self.start)
        if len(self.start) > 1:
            print('from socket')
            items = BilibiliItem()

            items['file_urls'] = self.start[0:len(self.start)-1]

            title = self.start[len(self.start)-1]
            print(title, 'parse')
            yield items
        else:
            print('from json')

            with open(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/long/long.json', 'r', encoding='utf-8') as f:
                json_list = json.load(f)
                print(json_list)
                print(json_list[len(json_list)-1])
                items = BilibiliItem()
                json_list.append('end')
                items['file_urls'] = json_list[0:len(json_list)-1]
                f.close()
                os.remove(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/long/long.json')
                Store.file_length = len(json_list)
                title = self.start[0]
                global urls

                urls = json_list

                yield items

    def closed(spider, reason):
        print(os.getcwd())

        for listname in os.listdir('./tomcat/full/'):
            if listname == 'tomcat':
                os.remove('./tomcat/full/'+listname)
            newname = listname[len(listname) - 8:len(listname)]
            os.rename('./tomcat/full/' + listname, './tomcat/full/' + newname+'.ts')
        num = 1000
        print(urls)
        for raw in urls[0:len(urls)-1]:
            x = hashlib.md5(raw.encode('utf-8')).hexdigest()
            a = x[len(x)-8:len(x)]
            os.rename('./tomcat/full/'+a+'.ts', './tomcat/full/'+str(num)+'.ts')
            num += 1
        get_full(title+'.mp4')





