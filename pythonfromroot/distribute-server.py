#!/usr/bin/python
#--coding:utf-8--
import time
from refer import write_pythonpath
from server import server
import os
import sys
from referfrom import write_class, write_py_file
out_dir = os.getcwd()
prefix = os.getcwd().split('pythonfromroot')
prefix_0 = prefix[0]
write_pythonpath(prefix_0)
sys.path.append(prefix_0+'bilibili/bilibili/spiders')
sys.path.append(prefix_0+'bilibili')
if not os.path.exists(prefix_0+'bilibili/bilibili/spiders/Directory.py'):
    write_py_file('Directory', 'AbsDirectory', file_path=prefix_0)
    write_class('Directory.py', 'StoreDirectory', file_path=prefix_0+'Acfun/')
try:
    from bilibili.spiders.Directory import AbsDirectory
except ModuleNotFoundError:
    print('==><==')
from threading import Thread
from copycut import *
import threading
from tkinter import filedialog
global anchor_
import socket


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("192.168.1.74", 11001))

    # print(server)
    # ip = socket.getfqdn(socket.gethostname())
    # print(ip)
    # print(socket.gethostbyname(ip))

    t = server.recv(1024)
    print(t.decode('utf-8'))
    server.close()



print(sys.path)

anchor_ = 0

list_in_urls = []
list_in_titles = []
list_in_ups = []


list_urls = ['']
x = 2
b = server()


switcher = True


# 启动服务端
def start_acfun():
    os.chdir(AbsDirectory.file_path+'pythonfromroot/')
    print(os.getcwd())
    os.system('python socket2.py')


# 获取地址列表,随机下载一个
def start_quotes():
    global dameon
    dameon = threading.Thread(target=getlist)
    dameon.start()
    print(dameon)
    os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    print(os.listdir())
    os.system('python test1.py ')
    #import random
    #index = random.randint(0, 9)
    print(list_in_urls)
    #url = list_in_urls[index]
   # single(url, list_in_urls, list_in_titles)


#
def download_list():

    pass

def getlist():
    global list_in_urls, list_in_titles, list_in_ups
    list_in_urls.clear(), list_in_titles.clear(), list_in_ups.clear()

    import socket
    global list_urls
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    port = 9999
    s.bind((host, port))
    s.listen(1)
    s1, address = s.accept()
    print('hello getlist')
    print(dameon)
    data = s1.recv(22000)

    list_urls = eval(data.decode('utf-8'))
    prefix = 'https://www.acfun.cn'
    for url in list_urls:
        if '/v/ac' in url:
            print(url)
            main_url = (prefix + url).replace(' ', '')

            list_in_urls.append(main_url)
        else:
            list_in_titles.append(url)
            split_title = url.split('\r')
            list_in_ups.append(split_title[1][3:])
    s1.close()


def process_spider(args):
    server_socket = threading.Thread(target=start_acfun)
    server_socket.start()
    os.system('cd '+AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    print(args)
    os.system('python cmd_line.py ' + args)


def single(args, list_in_urls_arg, list_in_titles_arg):
    print(os.getcwd())
    if args == '':
        return
    print(args,'this, is args')
    t = Thread(target=process_spider, args=(args,))
    t.start()

    sr = b.getfull()

    try:

        rece_str = next(sr)

        # 已经加倍了x4所以100变成25

        for nx in range(2, 1000):

                next(sr)
    except StopIteration:
            pass
    if args in list_in_urls_arg:
        index = list_in_urls_arg.index(args)
        list_in_urls_arg.remove(args)
        list_in_titles_arg.remove(list_in_titles_arg[index])


d0 = ()
up_list = []


def single2(args):
    print(os.getcwd())
    if args == '':
        return
    print(args,'this, is args')
    t = Thread(target=process_spider, args=(args,))
    t.start()

    sr = b.getfull()

    try:

        rece_str = next(sr)

        # 已经加倍了x4所以100变成25

        for nx in range(2, 1000):

                next(sr)
    except StopIteration:
            pass


# x_0 是被选择的列表, up_info列表
def change(args, list_in_urls_arg):
    print('正在下载' + args)
    if args == '':
        return
    t = Thread(target=process_spider, args=(args,))
    t.start()
    global x
    x += 4
    if x == 6:
        sr = b.getfull()
        try:

            for nx in range(2, 1000):
                next(sr)
        except StopIteration:
            pass

    x = 2
    print('zzzr')
    global anchor_
    if anchor_ < len(list_in_urls_arg):
        print(str(anchor_)+' akjjkk')
        anchor_ += 1
        if anchor_ < len(list_in_urls_arg):
            change(list_in_urls_arg[anchor_], list_in_urls_arg)


start_quotes()
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
print(host)
port = 10997
print(host)
serv.bind(('192.168.1.74', port))
serv.listen(5)
while True:
    cl, addr = serv.accept()
    time.sleep(5)

    if len(list_in_urls) < 0:
        break
    import time
    #while True:
     #   time.sleep(5)
      #  cl.send('hello my sql'.encode('utf-8'))
    print(addr)
    try:
        cl.send(list_in_urls.pop().encode('utf-8'))
    except IndexError:
        serv.close()
        print('end')
        break
