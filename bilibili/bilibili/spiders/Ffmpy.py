from ffmpy3 import FFmpeg
import os
from bilibili.spiders.Directory import StoreDirectory


def get_full(filename):
    if os.path.exists(StoreDirectory.file_path+filename):
        print('已经存在')
        return
    os.chdir('./tomcat/full/')
    s = 'concat:'

    for list1 in sorted(os.listdir('./')):
        s += list1+'|'
    ff = FFmpeg(inputs={s: None}, outputs={StoreDirectory.file_path+filename: '-vcodec copy -acodec copy'})
    print(filename)
    try:
        ff.run()
    finally:
        for list1 in os.listdir('./'):
            os.remove(list1)


def change_mark_point(t):
    b = r'\\n#EXTINF:5.0,\\n'   

    mark = b.replace('5.0', t)
    return mark
