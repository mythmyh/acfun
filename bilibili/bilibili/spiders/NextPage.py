

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import os
import scrapy
from bilibili.spiders.Directory import AbsDirectory
from scrapy.selector import Selector


class QuotesSpider(scrapy.Spider):

    name = "nextpage"
    start_urls = ['https://www.acfun.cn/']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",
                       'ITEM_PIPELINES': {'bilibili.pipes.FilesPipeline3': 1, }
                       }

    def __init__(self, upid='',pageNo=2, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.upid = upid
        # https://www.acfun.cn/space/next?uid=13215999&type=video&orderBy=2&pageNo=2

        QuotesSpider.start_urls = ['https://www.acfun.cn/space/next?uid='+upid+'&type=vi'
                                                                               'deo&orderBy=2&pageNo='+str(pageNo)]

    def parse(self, response):
        print(response.url)
        data = response.text.replace('true', 'True')
        dict_1 = eval(data)
        dict_2 = dict_1['data']
        dict_3 = eval(str(dict_2))
        source = dict_3['html']
        html_list = Selector(text=source).xpath('//a//@href').extract()
        title_list = Selector(text=source).xpath('//a/figure//@data-title').extract()
        global final_data
        final_data = dict(zip(html_list, title_list))
        print(final_data)
        with open(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/long/up_info.json', 'w', encoding='utf-8') as f:
            import json
            json.dump(final_data, f)

    def closed(spider, reason):
        import socket
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 10001

        client.connect((host, port))
        client.send(str(final_data).encode('utf-8'))


def run_spider(args, pn):

    print(os.getcwd())
    process = CrawlerProcess(get_project_settings())
    process.crawl('nextpage', upid=args, pageNo=pn)
    process.start(stop_after_crawl=True)  # the script will block here until the crawling is finished
    print('hello STOP')
    import sys
    sys.exit(0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        sys.argv.append('13215999', '2')
    print(sys.argv[1], sys.argv[2])
    run_spider(sys.argv[1], sys.argv[2])











