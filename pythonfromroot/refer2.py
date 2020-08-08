import sys
import os
from zipfile import ZipFile
import shutil


def unzip(file_path):
    myzip = ZipFile(file_path)
    for name in myzip.namelist():
        filename = name.encode('cp437').decode('gbk')
        myzip.extract(name)
        #os.chdir(file_path)
        try:
            os.rename(name, filename)

        except FileExistsError:
            os.remove(filename)
            os.rename(name, filename)


def copy_all(source, destination):
    z1 = destination

    for root, dir1, files1 in os.walk(source):
        for o1 in dir1:
            full_dirs = os.path.join(root, o1)
            relative_paths = full_dirs.replace(source, '')
            current_dirs = z1 + relative_paths
            try:
                os.makedirs(current_dirs)
            except FileExistsError:
                pass

        now_dirs = z1 + root.replace(source, '')
        for t0 in files1:
            shutil.copy(os.path.join(root, t0), now_dirs + '/' + t0)


def write_pythonpath(dir_path):
    dirs = [x for x in sys.path if x.endswith('site-packages')]
    if os.path.exists(dirs[0]+'/a.pth'):
        pass
    else:
        print('正在解压依赖包')
        unzip('site-packages.zip')
        print('正在复制依赖包')
        copy_all('site-packages', dirs[0])
        from testing_remove_line import change_line_py
        jc = dirs[0].replace('\\','\\\\')
        change_line_py(dirs[0]+'/ffmpy3.py', 52, '    def __init__(self, executable=\''+jc + '\\\\ffmpeg.exe\', global_options=None, inputs=None, outputs=None):\n')
        with open(dirs[0]+'/a.pth', 'w', encoding='utf-8') as f:

            f.write(dir_path+'bilibili/\n')
            f.write(dir_path+'bilibili/bilibili/spiders/\n')
