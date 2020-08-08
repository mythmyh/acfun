from scrapy import cmdline
import scrapy
import sys
from twisted.internet import reactor


if __name__ == '__main__':
    script = 'scrapy crawl house'
    print(sys.path)
    cmdline.execute(script.split())


