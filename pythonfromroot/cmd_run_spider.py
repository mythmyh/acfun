import threading
from threading import Thread
from bilibili.spiders.Directory import AbsDirectory
import os
import socket


def start_spiders(port, size, url):
    dameon = GetPageNo(getlist, (port, size))
    dameon.start()
    print(dameon)
    os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    cmd_line = 'python up.py ' + url
    os.system(cmd_line)
    return dameon.get_result()


def start_spiders_from(port, size, url, pyfile):
    dameon = GetPageNo(getlist, (port, size))
    dameon.start()
    print(dameon)
    os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    cmd_line = 'python '+pyfile+'.py ' + url
    os.system(cmd_line)
    return dameon.get_result()


def start_next_page(port, size, up_id, page_no):
    dameon = GetPageNo(getlist, (port, size))
    dameon.start()
    print(dameon)
    os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    cmd_line = 'python NextPage.py ' + up_id+' '+page_no
    os.system(cmd_line)
    return dameon.get_result()


def getlist(port, size):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(1)
    server, address = s.accept()
    data = server.recv(size)
    return data.decode('utf-8')


class GetPageNo(Thread):

    def __init__(self, func, args):
        super(GetPageNo, self).__init__()
        self.func = func
        self.args = args
        self.result = ''
        print('hello world')

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)
        try:
            return self.result
        except Exception:
            return None
