import sys
from scrapy import cmdline
from bilibili.spiders.Directory import AbsDirectory
import os

os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
script = 'scrapy crawl video -a url=' + sys.argv[1]
print(sys.path)
cmdline.execute(script.split())
