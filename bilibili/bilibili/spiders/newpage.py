from scrapy.selector import Selector
from scrapy.crawler import CrawlerProcess
from bilibili.spiders.Directory import AbsDirectory
from scrapy import Selector
from scrapy.utils.project import get_project_settings
from functools import partial
import os
from bilibili.items import BilibiliItem
import scrapy

global page_no, page_info
page_no = []
page_info = []


class GetUpInfoSpider(scrapy.Spider):

    name = "getupinfo"
    start_urls = ['https://www.acfun.cn/']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",
                       'ITEM_PIPELINES': {'bilibili.pipes.FilesPipeline3': 1, }
                       }

    def __init__(self, up_no=r'', page_no=1, *args, **kwargs):
        super(GetUpInfoSpider, self).__init__(*args, **kwargs)
        self.up_id = up_no
        self.page_no = page_no

    def parse(self, response):
        for x in os.listdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/full/'):
            os.remove(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/full/'+x)
        b = BilibiliItem()
        url_info = 'https://www.acfun.cn/u/{}?quickViewId=ac-space-video-list&reqID=1&a' \
                      'jaxpipe=1&type=video&order=newest&page={}&pageSize=20&t=1587549164677'.\
            format(self.up_id, self.page_no)
        b['file_urls'] = [url_info]
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
               #print(html)
                titles = Selector(text=html).xpath('//a//p[@class="title line"]//@title').extract()
                urls = Selector(text=html).xpath('//a/@href').extract()
                full_urls = ['https://www.acfun.cn'+x for x in urls]
                final_data = dict(zip(titles, full_urls))
                with open(AbsDirectory.file_path + 'bilibili/bilibili/spiders/tomcat/up_info.json', 'w',
                          encoding='utf-8') as r:
                    import json
                    json.dump(final_data, r)
                    r.close()

                print(titles)
                print(full_urls)
        pass


def run_spider(args):

    print(os.getcwd())
    process = CrawlerProcess(get_project_settings())
    run_in = partial(process.crawl, 'getupinfo', args)
    #process.crawl('getupinfo', up_no=args)
    #process.crawl('getupinfo', up_no=args, page_no=3)
    run_in(2)
    run_in(3)
    run_in(4)
    run_in(5)
    print('hello STOP')
    process.start(stop_after_crawl=True)  # the script will block here until the crawling is finished
    import sys
    sys.exit(0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        sys.argv.append('13457270')
    run_spider(sys.argv[1])
