import socket
import sys
import os
from bilibili.spiders.Directory import AbsDirectory
print(sys.path)

def start_acfun():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9997
    serversocket.bind((host, port))
    serversocket.listen(5)

    while True:
        total_data = ''
        clientsocket, addr = serversocket.accept()
        while True:
            msg = clientsocket.recv(500*1024)
            if not msg:
                break
            total_data += msg.decode('utf-8')
        print(total_data)

        a = msg.decode('utf-8')
        import sys
        print(sys.getsizeof(a))
        list1 = a.split(',')
        from scrapy import cmdline
        os.chdir(AbsDirectory.file_path+'bilibili/bilibili/spiders/')
        print(os.getcwd()+','+a)
        script = 'scrapy crawl acfun -a list_url=' + total_data
        cmdline.execute(script.split())
        clientsocket.close()


if __name__ == '__main__':
    start_acfun()
