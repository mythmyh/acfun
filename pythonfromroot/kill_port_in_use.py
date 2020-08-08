import os


def kill_ports_posix(ports):
    feedback = os.popen('lsof -i:'+ports)
    results = feedback.readlines()
    if len(results) != 0:
        types = results[1].split(' ')
        types_c = [x for x in types if x != '']
        print('Thread',types_c[1],'using ',ports,' has been killed.')
        os.system('kill -9 '+types_c[1])
    else:
        print(ports, ' not in using')


def kill_port_nt(port):
    z = os.popen('netstat -aon|findstr '+str(port))
    results = z.readlines()
    if len(results) != 0:
        oa = results[0].replace('\n', '').split(' ')
        f_oa = [x for x in oa if x != '']
        passport = f_oa[4]
        os.system('taskkill /f /PID '+passport)
        print(passport, 'has been killed')


def kill_multiple_ports(*args):
    if os.name == 'posix':
        for x in args:
            kill_ports_posix(str(x))
    elif os.name == 'nt':
        for x in args:
            kill_port_nt(str(x))


kill_multiple_ports(9995, 9997, 9998, 10001, 12010)


