# 导入 socket、sys 模块
import socket


class xtc:
    info = ''


class server:

    def getfull(self):
        # 创建 socket 对象
        print('start socket!')
        serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        # 获取本地主机名
        host = socket.gethostname()

        port = 9995

        # 绑定端口号
        serversocket.bind((host, port))

        # 设置最大连接数，超过后排队
        serversocket.listen(5)
        if 1:
            print('server ')
            clientsocket, addr = serversocket.accept()
            print('hello world')

            while True:
                # 建立客户端连接
                print("连接地址: %s" % str(addr))
                msg = '欢迎！' + "\r\n"
                msg1 = '我们'+'\r\n'

                try:
                    clientsocket.send(msg.encode('utf-8'))
                    clientsocket.send(msg1.encode('utf-8'))
                    str1 = clientsocket.recv(1024).decode('utf-8')
                    print(str1 + "server")
                    yield str1
                except (ConnectionResetError, BrokenPipeError):
                    print('下载完成！')
                    clientsocket.close()
                    break


if __name__ == '__main__':
    b = server()
