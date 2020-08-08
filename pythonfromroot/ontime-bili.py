#!/usr/bin/python
#--coding:utf-8--
import tkinter
from refer2 import write_pythonpath
from tkinter import ttk
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
from bilibili.spiders.Directory import AbsDirectory
from threading import Thread
from copycut import *
import threading
from tkinter import filedialog
global anchor_

print(sys.path)

anchor_ = 0

list_in_urls = []
list_in_titles = []
list_in_ups = []
win = tkinter.Tk()
win.title('Acfun Wonderful Dancer')


menubar = Menu(win)
emnu = Menu(menubar)


def change_path():
    path = filedialog.askdirectory()
    with open('../bilibili/bilibili/spiders/Directory.py', 'r+', encoding='utf-8') as f:
        a = f.readlines()
        h = [a.index(x) for x in a if x.startswith('class Store')]
        a[h[0] + 1] = '    file_path = \'' + path + '/\''
        print(h)
        print(a)
        os.remove('../bilibili/bilibili/spiders/Directory.py')
        with open('../bilibili/bilibili/spiders/Directory.py', 'w', encoding='utf-8') as t:
            t.writelines(a)


emnu.add_command(label='存储路径', command=change_path)

menubar.add_cascade(label='文件', menu=emnu, )
menubar.add_command(label='关于')
win['menu'] = menubar

list_urls = ['']
dance_urls = StringVar(value=list_urls)
at = StringVar()
global title_s
title_s = StringVar()
up = StringVar()
title = StringVar()
url2 = StringVar()
x = 2
b = server()


switcher = True


# 启动服务端
def start_acfun():
    os.chdir(AbsDirectory.file_path+'pythonfromroot/')
    print(os.getcwd())
    os.system('python socket2.py')


# 获取地址列表
def start_quotes():
    global column, dameon
    dameon = threading.Thread(target=getlist)
    dameon.start()
    print(dameon)
    os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    print(column.get())
    print(os.listdir())
    os.system('python test1.py '+column.get())


def getlist():
    print('hello world 95')

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
    print(list_in_urls)
    global dance_urls
    dance_urls.set(value=list_in_titles)
    print('hello world 126')
    s1.close()


def single2(args):
    print(os.getcwd())
    if args == '':
        return
    print(args, 'this, is args')
    p.grid(column=2, row=0, columnspan=3)
    p.update()
    t = Thread(target=process_spider, args=(args,))
    t.start()

    sr = b.getfull()

    try:

        rece_str = next(sr)

        # 已经加倍了x4所以100变成25

        p['maximum'] = eval(rece_str) * 25 * eval(rece_str)
        print(str(p['maximum']), '=====')
        p.update()
        for nx in range(2, 1000):
            p['value'] = next(sr)
            p.update()
    except StopIteration:
        p['value'] = 0

    at.set('')
    entry.update()
    p.grid_forget()




def cut(editor, event=None):
    editor.event_generate("<<Cut>>")


def copy(editor, event=None):
    editor.event_generate("<<Copy>>")


def paste(editor, event=None):
    editor.event_generate('<<Paste>>')


def clear(editor, event=None):
    editor.event_generate('<<Clear>>')


def undo(editor, event=None):
    editor.event_generate("<<Undo>>")


def select_all(editor, event=None):
    editor.event_generate("<<SelectAll>>")


def display(event):
    if menubar.winfo_ismapped():
        menubar.unpost()
        win.unbind("<<Button-1>>")


def rightKey(editor, event):
    if menubar.winfo_ismapped():
        menubar.unpost()
        return
    menubar.delete(0, END)
    menubar.add_command(label='剪切', command=lambda: cut(editor))
    menubar.add_command(label='复制', command=lambda: copy(editor))
    menubar.add_command(label='粘贴', command=lambda: paste(editor))
    menubar.add_command(label='清空', command=lambda: clear(editor))
    menubar.add_command(label='撤销', command=lambda: undo(editor))
    menubar.add_command(label='全选', command=lambda: select_all(editor))
    menubar.post(event.x_root, event.y_root)
    win.bind('<Button-1>', display)


def process_spider(args):
    server_socket = threading.Thread(target=start_acfun)
    server_socket.start()
    os.system('cd '+AbsDirectory.file_path+'bilibili/bilibili/spiders/')
    print(args)
    os.system('python cmd_line.py ' + args)


def single(args, list_in_urls_arg, list_in_titles_arg, dance_urls_arg):
    print(os.getcwd())
    if args == '':
        return
    print(args,'this, is args')
    t = Thread(target=process_spider, args=(args,))
    t.start()
    p.grid(column=2, row=0, columnspan=3)
    p.update()
    sr = b.getfull()

    try:

        rece_str = next(sr)

        # 已经加倍了x4所以100变成25

        p['maximum'] = eval(rece_str)*25*eval(rece_str)
        print(str(p['maximum']), '=====')
        p.update()
        for nx in range(2, 1000):

                p['value'] = next(sr)
                p.update()
    except StopIteration:
        p['value'] = 0

    at.set('')
    entry.update()
    if args in list_in_urls_arg:
        index = list_in_urls_arg.index(args)
        list_in_urls_arg.remove(args)
        list_in_ups.remove(list_in_ups[index])
        list_in_titles_arg.remove(list_in_titles_arg[index])
        dance_urls_arg.set(list_in_titles_arg)
    p.grid_forget()


d0 = ()
up_list = []


def change(args, list_in_urls_arg, dance_urls_arg, urls_full, titles_full,l2, x_0=[],):
    print(x_0)
    print('正在下载' + args)
    if args == '':
        return
    t = Thread(target=process_spider, args=(args,))
    t.start()
    p.grid(column=2, row=0, columnspan=3)
    p.update()
    global x
    x += 4
    if x == 6:
        sr = b.getfull()
        try:
            rece_str = next(sr)
            p['maximum'] = eval(rece_str) * 25 * eval(rece_str)
            p.update()
            for nx in range(2, 1000):
                p['value'] = next(sr)
                p.update()
        except StopIteration:
            p['value'] = 0

    else:
        at.set(x)
        label2.update()

    x = 2
    print('zzzr')
    at.set('')
    entry.update()
    p.grid_forget()
    global anchor_
    if anchor_ < len(list_in_urls_arg):
        print(str(anchor_)+' akjjkk')
        anchor_ += 1
        if anchor_ < len(list_in_urls_arg):
            print(list_in_urls_arg[anchor_])
            change(list_in_urls_arg[anchor_], list_in_urls_arg, dance_urls_arg, urls_full, titles_full,l2, x_0)
        else:
            if len(x_0) == 0:
                list_in_urls_arg.clear()
                dance_urls_arg.set(value=list_in_urls_arg)
            else:
                print(list_in_urls_arg)
                global kl, kt
                kl = [x1 for x1 in kl if kl.index(x1) not in x_0]
                kt = [x1 for x1 in titles_full if titles_full.index(x1) not in x_0]
                dance_urls_arg.set(value=kt)
                l2.selection_clear(0, len(kl))
                l2.update()

            pass


def showStatus(lx, list_in_titles, list_in_urls):
    idxs = lx.curselection()
    if len(idxs) == 1:
        idx = int(idxs[0])
        up.set(list_in_ups[idx])
        title.set(list_in_titles[idx])
        print(list_in_urls[idx])
        url2.set(list_in_urls[idx])


def showUpInfo():
    def get_position(tk):
        synax = tk.winfo_geometry()
        list_1 = synax.split('+')
        w_1, h_1 = list_1[1], list_1[2]
        return w_1, h_1
    info_w, info_h = get_position(win)
    from cmd_run_spider import start_spiders, start_next_page
    total_page = start_spiders(10000, 220, url2.get())
    t = eval(total_page)
    print(url2, 'showupinfo')
    global kt, dance_title, kl
    kt = ['']

    print(t[1])
    value_range = [j for j in range(1, int(t[0]) + 1)]

    w1, h1 = 700, 700
    sub_window = Toplevel()
    status_s = StringVar()
    dance_title = StringVar(value=kt)
    with open(AbsDirectory.file_path+'bilibili/bilibili/spiders/tomcat/long/up_info.json', encoding='utf-8') as f:
        import json
        data = json.load(f)
        # global k
        kt = list(data.keys())
        kl = list(data.values())
        dance_title.set(value=kt)
        print(kt)
        print('==============')

    def get_clicked(dx, idx):
        v = set(dx) - set(idx)
        print()
        print(set(idx))
        h2 = set(idx) - set(dx)
        sr = list(v.union(h2))
        return sr[0]

    def showstatus_2(lx, kt, kl):
        global d0
        idxs = lx.curselection()
        h_index = get_clicked(d0, idxs)
        d0 = idxs
        url_s.set(kt[h_index])
        print(title_s.get(), 'before')
        title_s.set('https://www.acfun.cn'+kl[h_index])
        global titlej, up_list
        up_list = ['https://www.acfun.cn'+e for e in kl if kl.index(e) in idxs]
        print(up_list)
        titlej = title_s.get()
        status_s.set('已经选中{}个视频'.format(len(idxs)))
        print(lx.curselection(), 'after')
        if len(lx.curselection()) > 1:
            button_select_download.grid(column=0, row=12, sticky=W)
            button_select_download.update()

        print(len(lx.curselection()))

    def got_next_page(event):
        global kt, kl, data_dict, title
        kt = []
        kl = []
        data_1 = start_next_page(10001, 5000, t[1], str(no_var.get()))
        data_dict = eval(data_1)
        print(data_dict)
        kt.clear(), kl.clear()
        kl = list(data_dict.keys())
        print(list(kl))
        kt = list(data_dict.values())
        dance_title.set(value=list(data_dict.values()))

    def wrapp(arg):
        print(arg)
        single(arg, kl, kt, dance_title)

    frame_in = ttk.Frame(sub_window, padding=(10, 10))
    frame_in.grid(column=0, row=0)
    no_var = StringVar()
    page_no = ttk.Combobox(frame_in, textvariable=no_var, exportselection=True, values=value_range)
    page_no.current(0)
    page_no.grid(column=0, row=0, sticky=W)
    url_s = StringVar()
    label_tag = ttk.Label(frame_in, text='标题: ', padding=(10, 0, 0, 0))
    label_tag.grid(column=2, row=1)
    label_tag_2 = ttk.Label(frame_in, text='网址：', padding=(10, 0, 0, 0))
    label_tag_2.grid(column=2, row=2)

    label_url1 = ttk.Label(frame_in, textvariable=url_s, justify=LEFT)
    label_url1.grid(column=3, row=1, sticky=W)
    label_title = ttk.Label(frame_in, textvariable=title_s, justify=LEFT)
    label_title.grid(column=3, row=2, sticky=W)
    l2 = Listbox(frame_in, listvariable=dance_title, height=20, width=40, selectmode='multiple')
    l2.bind('<<ListboxSelect>>', lambda event: showstatus_2(l2, kt, kl))
    l2.grid(column=0, row=1, sticky=(W, S, E), rowspan=10, columnspan=2)
    button_select_download = ttk.Button(frame_in, text='下载选中', command=lambda: change(up_list[0], up_list, dance_title, kl, kt,l2,
                                                                              l2.curselection()))

    label_select_staus = ttk.Label(frame_in, textvariable=status_s, justify=LEFT)
    label_select_staus.grid(column=0, row=11, sticky=W)
    button_info = ttk.Button(frame_in, text='下载', command=lambda: wrapp(title_s.get()))
    button_info.grid(column=3, row=3, sticky=W)
    page_no.bind("<<ComboboxSelected>>", got_next_page)
    x_sub = int(info_w) + 700
    y_sub = int(info_h) - 60
    sub_window.geometry("{}x{}+{}+{}".format(str(w1), str(h1), str(x_sub), str(y_sub)))
    sub_window.mainloop()


frame1 = ttk.Frame(win, padding=(10, 10))

p = ttk.Progressbar(frame1, orient=HORIZONTAL, length=200, mode='determinate')
p['maximum'] = 100
label2 = ttk.Label(win, padding=(10,12))
entry = ttk.Entry(frame1, textvariable=at, width=30)
entry.grid(column=0, row=0)
button = ttk.Button(frame1, text='单页下载',command=lambda: single2(at.get()), width=7)

column = StringVar()

music = ttk.Radiobutton(frame1, text='音乐 ', variable=column, value='pagelet_music')
music.grid(column=1, row=2)
life = ttk.Radiobutton(frame1, text=' 生活', variable=column, value='pagelet_life')
life.grid(column=3, row=2, sticky=W)
anima = ttk.Radiobutton(frame1, text='动画', variable=column, value='pagelet_douga')
anima.grid(column=4, row=2,)

tech = ttk.Radiobutton(frame1, text='科技', variable=column, value='pagelet_tech')
tech.grid(column=4, row=3,)

banana = ttk.Radiobutton(frame1, text='电影', variable=column, value='pagelet_film')
game = ttk.Radiobutton(frame1, text='游戏', variable=column, value='pagelet_game')
banana.grid(column=1, row=3)
game.grid(column=2, row=3, sticky=W)
dance = ttk.Radiobutton(frame1, text='鱼塘', variable=column, value='pagelet_fishpond')
dance.grid(column=3, row=3, sticky=W)
cars = ttk.Radiobutton(frame1, text='体育', variable=column, value='pagelet_sport')
cars.grid(column=2, row=2, sticky=W)
label_up = ttk.Label(frame1, text='up主: ')
label_up.grid(column=1, row=6)

label_up = ttk.Label(frame1,textvariable=up, justify=LEFT)
label_up.grid(column=2, row=6, columnspan=2, sticky=W)
button_up = ttk.Button(frame1, text='up信息', command=showUpInfo)
button_up.grid(column=4, row=6, )

label_url = ttk.Label(frame1, text='网址: ')
label_url.grid(column=1, row=8)
button_url = ttk.Button(frame1, text='下载', command=lambda: single(url2.get(), list_in_urls, list_in_titles, dance_urls))
button_url.grid(column=4, row=8,)

label_select_url = ttk.Label(frame1, textvariable=url2, justify=LEFT, wraplength='3c')
label_select_url.grid(column=2, row=8, columnspan=2, sticky=W)


l = Listbox(frame1, listvariable=dance_urls, height=20,)
l.grid(column=0, row=1, sticky=(W, S, E), rowspan=10)
l.bind('<<ListboxSelect>>', lambda event: showStatus(l, list_in_titles, list_in_urls))
button_l = ttk.Button(frame1, text='获取列表', command=start_quotes)
button_l.grid(column=1, row=10, sticky=(W, S, E),padx=10)
button_Download = ttk.Button(frame1, text='下载列表', command=lambda: change(list_in_urls[0], list_in_urls, dance_urls, list_in_urls, list_in_titles,l))
button_Download.grid(column=2, row=10, sticky=(W, S, E))
button.grid(column=1, row=0)
frame1.grid(column=0, row=0)
menubar = Menu(win, tearoff=False)
entry.bind("<Button-3>", lambda x1: rightKey(entry, x1))
win.bind('<FocusOut>', display)
win.bind("<Configure>", display)

w, h = 700, 600
win.geometry('{}x{}'.format(w, h))
win.mainloop()
