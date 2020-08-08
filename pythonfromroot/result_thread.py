from threading import Thread
from bilibili.spiders.package_socket_client_and_server import receive_port
import threading
from bilibili.spiders.Directory import AbsDirectory
import os


class WrapThreadResult(Thread):

    def __init__(self, func, args):
        super(WrapThreadResult, self).__init__()
        self.func = func
        self.args = args
        self.result = ''

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        threading.Thread.join(self)
        try:
            return self.result
        except Exception:
            return None


def get_login_status(port, infos):

    dameon = WrapThreadResult(receive_port, (port,))
    dameon.start()
    os.chdir(AbsDirectory.file_path + 'bilibili/bilibili/spiders/')
    print(os.getcwd())
    os.system('python acfun_cookie.py {} {} {}'.format(infos[0], infos[1], infos[2]))
    return dameon.get_result()


