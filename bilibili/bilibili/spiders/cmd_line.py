from scrapy import cmdline
import sys


if __name__ == '__main__':
    script = 'scrapy crawl video -a url=' + sys.argv[1]
    print(sys.path)
    cmdline.execute(script.split())
