import os
import sys
import scrapy.crawler as crawler
from twisted.internet import reactor
from multiprocessing import Process, Queue
from scrapy.crawler import CrawlerProcess
from bilibili.spiders.Directory import AbsDirectory
from scrapy import Selector
import re
from scrapy.utils.project import get_project_settings
import os
from bilibili.items import BilibiliItem
import scrapy
import inspect
import ctypes


class column1:
    str = ''


class QuotesSpider(scrapy.Spider):

    name = "quote1"
    start_urls = ['https://www.acfun.cn/']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",
                       'ITEM_PIPELINES': {'bilibili.pipes.FilesPipeline3': 1, }
                       }

    def __init__(self, column=r'pagelet_dance', *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.column = column
        column1.str = column
        print(column1.str)

    def parse(self, response):
        for x in os.listdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/full/'):
            os.remove(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/full/'+x)
        b = BilibiliItem()
        b['file_urls'] = ['https://www.acfun.cn/?pagelets=pagelet_game,pagelet_douga,pagelet_bangumi_list,pagelet_life,'
                         'pagelet_tech,pagelet_dance,pagelet_music,pagelet_film,pagelet_fishpond,pagelet_s'
                         'port&reqID=0&ajaxpipe=1&t=1582458727656']
        yield b

    def closed(spider, reason):
        for x in os.listdir('./tomcat/full/'):
            with open('./tomcat/full/'+x, encoding='utf-8') as f:
                t = f.read()
                b = t.split('/*<!-- fetch-stream -->*/')
                f.close()
                os.remove('./tomcat/full/' + x)
                for x in b:
                    b = re.search(column1.str, x)
                    if b is not None:
                        v = eval(x)
                        e = Selector(text=v['html']).xpath('//div[@class="normal-video log-item"]//a[@'
                                                           'class="normal-video-cover"]//@href').extract()
                        alt = Selector(text=v['html']).xpath('//div[@class="normal-video log-item"]//a[@class="normal-video-title"]//@title').extract()
                        e += alt
                        print(e)
                        import socket
                        import sys
                        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        host = socket.gethostname()
                        port = 9999
                        print(sys.getsizeof(str(e)))
                        client.connect((host, port))
                        client.send(str(e).encode('utf-8'))


def run_spider(args):

    print(os.getcwd())
    process = CrawlerProcess(get_project_settings())
    process.crawl('quote1', column=args)
    process.start(stop_after_crawl=True)  # the script will block here until the crawling is finished
    print('hello STOP')
    import sys
    sys.exit(0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.argv.append('pagelet_dance')
    run_spider(sys.argv[1])
