# -*- coding: utf-8 -*-
import scrapy

import os

import json

import smtplib
from email.mime.text import MIMEText


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['su.58.com']
    custom_settings = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/41.0.2228.0 Safari/537.36",

                       }

    def __init__(self, *args, **kwargs):
        super(HouseSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://su.58.com/xietang/chuzu/0/?minprice=500_700&PGTID=0d3090a7-0351-dea2-b83c'
                           '-9ccc1b5bc05e&ClickID=2']

    def parse(self, response):
        raw_url = response.xpath('//div[@class="list-box"]//div[@class="des"]//h2//a//@href').extract()
        urls = response.xpath('//div[@class="list-box"]//div[@class="des"]//h2//a//text()').extract()
        time = response.xpath('//div[@class="list-box"]//div[@class="send-time"]//text()').extract()
        money = response.xpath('//div[@class="list-box"]//div[@class="money"]//b//text()').extract()[1]
        index = len(money)
        print(raw_url)
        raw_0 = money[index-1]
        a = [t.replace(raw_0, '0').replace('\n', '').strip() if raw_0 in t else t.replace('\n', '').strip() for t in urls]
        print(a)
        print(len(a))
        global raw_2
        raw_2 = ''
        tuple_str = self.process_str2(a,'厅')
        source1 = self.replace_to_num(a, tuple_str)

        # 厅前不是 1 或者 0 就是 2
        for one in source1:
            x_1 = one.find('厅')
            if one[x_1 - 1] != '0' and one[x_1 - 1] != '1':
                raw_2 = one[x_1 - 1]
                break
        b = [t.replace(raw_2, '2') for t in source1]
        t = self.process_str2(b, '室')
        source_home = self.replace_to_num2(b, t)
        final = []

        # 替换大于3的房间统一为4
        for item in source_home:
            x_1 = item.find('室')
            if item[x_1 - 1] != '1' and item[x_1 - 1] != '2' and item[x_1 - 1] != '3':
                four = item[x_1 - 1]
                item2 = item.replace(four, '4')
                final.append(item2)
            else:
                final.append(item)

        print(final)
        send_times = []
        for x in range(len(time)):
            if '小时前' in time[x] or '分钟' in time[x]:
                send_times.append(x)

        # 获取几小时前的网址
        def chosen_list(target, list1):
            listx = []
            for x in list1:
                listx.append(target[x])
            return listx
        print(time)
        print(send_times)

        final2 = chosen_list(final, send_times)
        urls2 = chosen_list(raw_url, send_times)
        info_urls = dict(zip(final2, urls2))

        if os.path.exists('/home/mayinghao/data.json'):
            try:
                with open('/home/mayinghao/data.json', 'r+') as f:

                    data = json.load(f)
                    print(data)
                    if len(data) < 5:
                        for k, v in info_urls.items():
                            data[k] = v

                        f.seek(0)
                        json.dump(data, f)
                    if len(data) >= 5:
                        print('%d的长度' % (len(info_urls)))
                        self.send_mail('mythmyh2@hotmail.com', '500-700斜塘租房', ''.join(str(info_urls)))

                        os.remove('/home/mayinghao/data.json')

            except json.decoder.JSONDecodeError as err:
                print(err)
                pass

        else:
            if len(info_urls) >= 5:
                print(len(info_urls))
                print(''.join(str(info_urls)))
                self.send_mail('mythmyh2@hotmail.com', '500-700斜塘租房', ''.join(str(info_urls)))
            else:
                with open('/home/mayinghao/data.json', 'w') as f:
                    print('%d的长度'%(len(info_urls)))
                    json.dump(info_urls, f)

    # 替换厅 1
    def replace_to_num(self, lists, tuple_str):
        print(tuple_str)
        arg_cn, source_num = tuple_str[1], tuple_str[0]
        return [t.replace(arg_cn, '1')for t in lists]

    # 替换室 3
    def replace_to_num2(self, lists, tuple_str):
        print(tuple_str)
        arg_cn, source_num = tuple_str[1], tuple_str[0]
        return [t.replace(arg_cn, '3') for t in lists]

    # 如果是一室一厅一卫
    def process_str(self, arg,list_raw):
        arg = arg.replace('\n', '')
        position_3 = arg.find('卫')
        if arg[position_3-1] == arg[position_3-3] and arg[position_3-3] == arg[position_3-5]:
            s = arg[position_3-1]
            raw = '1'
            index = 0
            for x in list_raw:
                new = x.replace(s, raw)
                list_raw[index] = new

        return arg, list_raw

        pass

    # 获取对应编码最大值
    def process_str2(self, list_raw, prefix):
        stat = set()
        list_stat = []
        list_map = {}
        for x in list_raw:
            position = x.find(prefix)
            stat.add(x[position-1])
            list_stat.append(x[position-1])

        for str1 in stat:
            print(str(list_stat.count(str1))+','+str1)
            if str1 != '2' and str1 != '1':
                list_map[list_stat.count(str1)] = str1

        b = max(list_map.items())
        return b

    def closed(spider, reason):
        pass

    def send_mail(self,to_list, subject, content):
        mail_host = 'smtp.163.com'  # smtp地址如果不知可以百度如“163邮箱smtp地址”
        mail_user = 'novang'  # 此账号密码是用来给人发送邮件的
        mail_pass = 'myh159375.'  # 此账号密码是用来给人发送邮件的
        mail_postfix = '163.com'  # 邮箱地址，smtp地址删去smtp字符如“163.com”

        me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = me
        msg['to'] = to_list

        try:
            s = smtplib.SMTP_SSL()
            s.connect(mail_host)
            s.login(mail_user, mail_pass)
            s.sendmail(me, to_list, msg.as_string())
            s.close()
            return True
        except Exception:

            return False







