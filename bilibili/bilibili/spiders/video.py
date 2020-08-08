# -*- coding: utf-8 -*-
import logging
from scrapy import FormRequest
from bilibili.items import BilibiliItem
from bilibili.spiders.Directory import AbsDirectory
import os
import re
import re
from bilibili.spiders.mp4 import Info
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import sys
sys.path.append(AbsDirectory.file_path+'bilibili')
import threading


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['www.acfun.cn']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",
                       'ITEM_PIPELINES': {'bilibili.pipes.FilesPipeline3': 1,}


                       }

    def start_requests(self):
        return [FormRequest('https://id.app.acfun.cn/rest/web/login/signin',
                            formdata={'username': '13306131532', 'password': '7758196159'})]

    def __init__(self, url='https://www.acfun.cn/v/ac12717962', *args, **kwargs):
        super(VideoSpider, self).__init__(*args, **kwargs)
        self.start_urls = [url]

    def parse(self, response):
        path = AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/full/'
        for x in os.listdir(path):
            os.remove(path + x)
        cookie1 = response.headers.getlist('Set-Cookie')
        cookies = {}
        for i in cookie1:
            i = str(i)
            l1 = i.split(';')
            l2 = l1[0].split('=')
            cookies[l2[0]] = l2[1]
        a = BilibiliItem()
        #url ='https://ali-video.acfun.cn/mediacloud/acfun/acfun_video/segment/'+self.start_urls[0]
        a['file_urls'] = [self.start_urls[0]]
       # if self.start_urls[0] is not None:
           # yield scrapy.Request(self.start_urls[0], cookies=cookies, callback=self.parse_2)
        yield scrapy.Request(self.start_urls[0], cookies=cookies, callback=self.parse_2)

    def parse_2(self, response):
        global title

        title_l = response.xpath("//h1//text()").extract()
        if len(title_l) > 1:
            title = response.xpath("//h1//text()").extract()[len(title_l)-1]
        else:
            title = title_l[0]
        urls = response.text.split('\\\"1080P60\\\"')
        if len(urls) == 1:
            urls = response.text.split('\\\"1080P\\\"')
            if len(urls) == 1:
                urls = response.text.split('\\\"超清\\\"')
                if len(urls) == 1:
                    urls = response.text.split('\\\"高清\\\"')
                    if len(urls) == 1:
                        urls = response.text.split('\\\"标清\\\"')

        t = urls[1]
        raw_url = self.get_str(t, '[', ']')
        logging.warning(raw_url)
        a = BilibiliItem()
        # url ='https://ali-video.acfun.cn/mediacloud/acfun/acfun_video/segment/'+self.start_urls[0]
        a['file_urls'] = [raw_url]
        yield a

    def get_str(self, args, start, end):
        a1 = args.split(start)
        b1 = a1[1]
        c1 = b1.split(end)

        wanted = c1[0].replace('\\"', '')
        url = re.findall(r'http[s]?://.*?\/segment', wanted)
        if len(url) != 0:
            Info.url = url[0]
        else:
            url = re.findall(r'http[s]?://.*?\/hls', wanted)
            Info.url = url[0]

        return wanted

    def closed(spider, reason):
        print(os.getcwd())
        for listname in os.listdir('./tomcat/full/'):
            newname = listname[len(listname) - 8:len(listname)]
            os.rename('./tomcat/full/' + listname, './tomcat/full/' + newname+'.txt')

        num = 1000

        with open('./tomcat/full/'+newname+'.txt') as f:
            lines = f.readlines()
            for line in lines:
                if not line.startswith('#EXT'):

                    slice_url = line.replace('\n', '')
                    slice_url2 = Info.url+'/'+slice_url
                    Info.lista.append(slice_url2)

        b = ''
        if Info.url+'/mediacloud/acfun/acfun_video/hls/' in Info.lista:
            Info.lista.remove(Info.url+'/mediacloud/acfun/acfun_video/hls/')
        for x in Info.lista:
            b += x
            b += ','
        # 去掉 / 去掉空格,冒号 竖线等
        title_1 = title.replace(' ', '').replace('/', '').replace('|', '').replace(':', '').replace(',', '')
        print(title_1)

        bytes_len = sys.getsizeof(b)
        if bytes_len % 2 == 1:
            bytes_len += 1
        print(sys.getsizeof(b))

        path = AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/full/'
        for x in os.listdir(path):
            os.remove(path + x)
        import json
        if bytes_len > 50*1024:
            print('from json')
            with open(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/long/long.json', 'w') as f:

                json.dump(Info.lista, f)
            import socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            port = 9997
            s.connect((host, port))
            s.send(title_1.encode('utf-8'))
            s.close()

        else:
            b += title_1
            import socket
            print('from socket')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            port = 9997
            print(b)
            s.connect((host, port))
            s.sendall(b.encode('utf-8'))
            s.close()











