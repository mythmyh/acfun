# -*- coding: utf-8 -*-
from scrapy import FormRequest
from bilibili.spiders.Directory import AbsDirectory
import os
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess
import sys
from bilibili.spiders.package_socket_client_and_server import send_socket
sys.path.append(AbsDirectory.file_path+'bilibili')


class CookieSpider(scrapy.Spider):
    name = 'cookies'
    #allowed_domains = ['www.acfun.cn']
    # 与setting里的不同=换成冒号
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",
                       'ITEM_PIPELINES': {'bilibili.pipes.FilesPipeline3': 1, },
                       'DEFAULT_REQUEST_HEADERS': {'referer': 'https://www.acfun.cn/v/ac13890788'}


                       }
    ''' 
    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], cookies=self.cookies2)
    '''
    def start_requests(self):
        return [FormRequest('https://id.app.acfun.cn/rest/web/login/signin',
                            formdata={'username': self.username, 'password': self.password})]

    def __init__(self,username=None, password=None, target=None, *args, **kwargs):
        super(CookieSpider, self).__init__(*args, **kwargs)
        self.username = username
        self.password = password
        self.target = target

    def parse(self, response):
        print(response.text,'abc')
        info_user = eval(response.text)
        print(type(info_user))
        global message, dict_cookie
        dict_cookie = {}
        message = 0

        t = dict(response.headers)
        if self.target == 'content':
            yield scrapy.Request('https://www.acfun.cn/rest/pc-direct/feed/followFeed?isGroup=0&gid'
                                 '=-1&count=10&pcursor=1',
                                 cookies=dict_cookie, callback=self.parse_2)
            pass
        else:
            if b'Set-Cookie' in t:
                message = info_user['username']
                cookies = t[b'Set-Cookie']
                for x in cookies:
                    n1 = x.decode('utf-8').split('=')
                    dict_cookie[n1[0]] = n1[1]

                yield scrapy.Request('https://www.acfun.cn/rest/pc-direct/feed/followFeed?isGroup=0&gid'
                                     '=-1&count=10&pcursor=1',
                                     cookies=dict_cookie, callback=self.parse_2)
                send_socket(12010, message)
            else:

                send_socket(12010, message)

    def parse_2(self, response):
        dict_1 = response.text.replace('true', 'True').replace('false', 'False').replace('null', '\'null\'')
        dict_2 = eval(dict_1)
        feed_list = dict_2['feedList']
        global push_content_info
        push_content_info = {}
        print(feed_list)
        for x in feed_list:
            print(x['title'], x['url'])
            push_content_info[x['title']] = 'https://www.acfun.cn'+x['url']
        yield scrapy.Request('https://www.acfun.cn/rest/pc-direct/feed/followFeed?isGroup=0&gid=0&count=10&pcursor=2', cookies=dict_cookie, callback=self.parse_3)

    def parse_3(self, response):
        pass

    def closed(spider, reason):
        if message == 0:

            send_socket(12010, str(push_content_info))


def run_spider(*args):
    process = CrawlerProcess(get_project_settings())
    process.crawl('cookies', username=args[0], password=args[1], target=args[2])
    print(args)
    process.start(stop_after_crawl=True)

    import sys
    sys.exit(0)


if __name__ == '__main__':
    import sys

    print(len(sys.argv))
    if len(sys.argv) <= 2:
        print('hello world')
    run_spider(sys.argv[1], sys.argv[2], sys.argv[3])







