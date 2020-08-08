from scrapy import cmdline
import sys
import os

#video_url = sys.argv[1]
##print(os.getcwd())
#os.system('cd /home/mayinghao/bilibili/bilibili/spiders/ && scrapy crawl acfun -a list_url ='+video_url)


import scrapy



class SeleniumRequest(scrapy.Request):
    """
    selenium专用Request类
    """
    pass
