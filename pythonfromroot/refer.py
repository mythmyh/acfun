import sys
import os


def write_pythonpath(dir_path):
    dir = [x for x in sys.path if x.endswith('site-packages')]
    if os.path.exists(dir[0]+'/a.pth'):
        pass
    else:
        with open(dir[0]+'/a.pth', 'w', encoding='utf-8') as f:
            f.write(dir_path+'bilibili/\n')
            f.write(dir_path+'bilibili/bilibili/spiders/\n')
