# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
class client:


    def getname(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 获取本地主机名
        host = socket.gethostname()

        # 设置端口号
        port = 9995

        # 连接服务，指定主机和端口
        s.connect((host, port))

        # 接收小于 1024 字节的数据
      #  msg = s.recv(1024)
        #'''
        i = 11
        while 1:
            yield
            i += 1
            s.send(str(i).encode('utf-8'))
            print('hello world')
            print(i)
            if i==20:
                s.close()
                break

b = client()
c = b.getname()
import time

next(c)
for t in range(3,10):
    time.sleep(2)
    next(c)


