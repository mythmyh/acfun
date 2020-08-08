from scrapy import cmdline
import sys
import os
video_url = sys.argv[1]
print(os.getcwd())
os.chdir('/home/mayinghao/bilibili/bilibili/spiders')
print(os.getcwd())
script = 'scrapy crawl acfun -a list_url='+video_url
print(script)
cmdline.execute(script.split())
