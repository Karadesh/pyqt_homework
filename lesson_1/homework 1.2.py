# 2) Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
# Меняться должен только последний октет каждого адреса.
# По результатам проверки должно выводиться соответствующее сообщение.
import ipaddress
import subprocess


def host_range_ping(string_ip_one, string_ip_two):
    ip_one = ipaddress.ip_address(string_ip_one)
    ip_two = ipaddress.ip_address(string_ip_two)
    for i in range(1, 256):
        if ip_one > ip_two:
            return 'pinging is complete'
            break
        else:
            result = subprocess.Popen(['ping', '4', str(ip_one)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
            if result:
                print(str(ip_one), 'is avaliable')
            else:
                print(str(ip_one), 'is not avaliable')
            ip_one = ip_one + 1




print(host_range_ping('192.168.1.1','192.168.1.3'))


