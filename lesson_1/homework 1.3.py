# 3) Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
# Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль tabulate).


import ipaddress
import subprocess
from tabulate import tabulate

def host_range_ping(string_ip_one, string_ip_two):
    ip_one = ipaddress.ip_address(string_ip_one)
    ip_two = ipaddress.ip_address(string_ip_two)
    reachable = []
    unreachable = []
    total_data = {'Reachable': [], 'Unreachable': []}
    for i in range(1, 256):
        if ip_one > ip_two:
            total_data['Reachable'] = reachable
            total_data['Unreachable'] = unreachable
            #return 'pinging is complete'
            return (tabulate(total_data, headers='keys', stralign='center'))
        else:
            result = subprocess.Popen(['ping', '4', str(ip_one)], shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE).wait()
            if result:
                #print(str(ip_one), 'is avaliable')
                reachable.append(str(ip_one))
            else:
                #print(str(ip_one), 'is not avaliable')
                unreachable.append(str(ip_one))
            ip_one = ip_one + 1


print(host_range_ping('192.168.1.1', '192.168.1.5'))
