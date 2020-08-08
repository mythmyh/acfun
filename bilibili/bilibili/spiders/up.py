
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import json
import scrapy
from bilibili.spiders.Directory import AbsDirectory
from scrapy.selector import  Selector
from bilibili.items import BilibiliItem

class UpInfoSpider(scrapy.Spider):

    name = "upinfo"
    start_urls = ['https://www.acfun.cn/']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",
                       'ITEM_PIPELINES': {'bilibili.pipes.FilesPipeline3': 1, }
                       }

    def __init__(self, url2='https://www.acfun.cn/v/ac14110187', *args, **kwargs):
        super(UpInfoSpider, self).__init__(*args, **kwargs)

        self.start_urls = [url2]

    def parse(self, response):
        up_url = response.xpath('//div[@class="up-details"]//a//@href').extract()[0]
        print(up_url)
        import re
        global up_id
        pattern = re.compile(r'\d+')
        m = pattern.findall(up_url)
        if len(m) != 0:
            up_id = m[0]

        yield scrapy.Request(url='https://www.acfun.cn'+up_url, callback=self.parse_up_url)

    def parse_up_url(self, response):
        global totalPage
        totalPage = response.xpath('//div[@class="ac-space-contribute-list"]//ul//li[@class="active"]//@data-count').extract()[0]
        totalPage = int(int(totalPage)/20) + 1
        s = 'https://www.acfun.cn/u/{}?quickViewId=ac-space-video-list&reqID=4&ajaxpipe=' \
            '1&type=video&order=newest&page={}&pageSize=20&t=1587619209806'.format(up_id, 1)
        b = BilibiliItem()
        b['file_urls'] = [s]
        print(totalPage)
        yield b

    def closed(spider, reason):
        for x in os.listdir('./tomcat/full/'):
            with open('./tomcat/full/' + x, encoding='utf-8') as f:
                t = f.read()
                f.close()
                os.remove('./tomcat/full/' + x)
                if len(t) == 198:
                    return
                html = eval(t.split('/*')[0])['html']
                # print(html)
                titles = Selector(text=html).xpath('//a//p[@class="title line"]//@title').extract()
                urls = Selector(text=html).xpath('//a/@href').extract()
                #full_urls = ['https://www.acfun.cn' + x for x in urls]
                final_data = dict(zip(titles, urls))
                with open(AbsDirectory.file_path + 'bilibili/bilibili/spiders/tomcat/long/up_info.json', 'w',
                          encoding='utf-8') as r:
                    import json
                    json.dump(final_data, r)
                    r.close()

                print(titles)
        import socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 10000
        tux = (totalPage, up_id)
        client.connect((host, port))
        client.send(str(tux).encode('utf-8'))


def run_spider(args):

    print(os.getcwd())
    process = CrawlerProcess(get_project_settings())

    # process第二个参数为要在__init__里传入的参数名
    process.crawl('upinfo', url2=args)
    process.start(stop_after_crawl=True)  # the script will block here until the crawling is finished
    import sys
    sys.exit(0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.argv.append('https://www.acfun.cn/v/ac14134110')
    run_spider(sys.argv[1])
