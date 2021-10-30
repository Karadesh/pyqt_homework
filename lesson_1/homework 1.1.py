# 1) Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или ip-адресом.
# В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения («Узел доступен», «Узел недоступен»).
# При этом ip-адрес сетевого узла должен создаваться с помощью функции ip_address().
import ipaddress
import subprocess


def host_ping(ip_network):
    for host in ip_network:
        result = subprocess.Popen(['ping', '4', host], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
        if result:
            print(host, ' узел доступен')
        else:
            print(host, ' узел недоступен')


def ip_to_string(*args):
    splitter = args
    ip_list = []
    for i in splitter:
        ip_list.append(i)
    print(ip_list)
    return ip_list



print(host_ping(ip_to_string('127.0.0.1', '80.0.0.3', '50.50.0.1', '1.1.1.0')))

