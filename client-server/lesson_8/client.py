import socket
import threading
import os
import random
from sys import argv
import logging
import log
import log.client_log_config

logger = logging.getLogger('')
UDP_len = 65535

commands = ('.members',
            '.connect',
            '.exit',
            '.help'
            )

help_commands = """
.members - active clients
.connect (client) - connect to client
.exit - disconnect
"""

script, ip, port = argv


def listen(s: socket.socket, host=str(ip), port = int(port)):
    while True:
        msg, addr = s.recvfrom(UDP_len)
        msg_port = addr[-1]
        msg = msg.decode('utf-8')
        allowed_ports = threading.current_thread().allowed_ports
        if msg_port not in allowed_ports:
            continue
        if not msg:
            continue

        if '__' in msg:
            command, content = msg.split('__')
            if command == 'members':
                logger.info(f'CLIENT: command "members"')
                for n, member in enumerate(content.split(';'), start=1):
                    print('\r\r'+ f'{n}){member}' + '\n' + 'you: ', end='')
        else:
            peer_name = f'client{msg_port}'
            print('\r\r' + f'{peer_name}: ' + msg + '\n' + f'you: ', end='')
            logger.info(f'CLIENT: message from {peer_name}')


def start_listen(target, socket, host, port):
    th = threading.Thread(target=target, args=(socket, host, port), daemon=True)
    th.start()
    return th


def connect(host=str(ip), port=int(port)):
    own_port = random.randint(8000, 9999)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, own_port))
    listen_thread = start_listen(listen, s, host, port)
    allowed_ports = [port]
    listen_thread.allowed_ports = allowed_ports
    sendto = (host, port)
    s.sendto('__join'.encode('utf-8'), sendto)
    logger.info(f'CLIENT: connected to {host}, {port}')
    while True:
        msg = input(f'you: ')
        command = msg.split(' ')[0]
        if command in commands:
            if msg == '.members':
                s.sendto('__members'.encode('utf-8'), sendto)
                logger.info('CLIENT: Members request')

            if msg == '.exit':
                try:
                    peer_port = sendto[-1]
                    allowed_ports.remove(peer_port)
                    sendto = (host, port)
                    print(f'Disconnect from client{peer_port}')
                    logger.info(f'CLIENT: Disconnected from client {peer_port}')
                    if peer_port == port:
                        s.sendto('__disconnect'.encode('utf-8'), sendto)
                        logger.info(f'CLIENT: disconnected from server. Port: {peer_port}')
                        break
                except ValueError:
                    s.sendto('__disconnect'.encode('utf-8'), sendto)
                    break



            if msg.startswith('.connect'):
                peer = msg.split(' ')[-1]
                peer_port = int(peer.replace('client', ''))
                allowed_ports.append(peer_port)
                sendto = host, peer_port
                print(f'connected to client {peer_port}')
                logger.info(f'CLIENT: connected to client {peer_port}')

            if msg == '.help':
                print(help_commands)
                logger.info('CLIENT: HELP request')
        else:
            s.sendto(msg.encode('utf-8'), sendto)
            logger.info('CLIENT: Message sended')
    s.close()


if __name__ == '__main__':
    os.system('clear')
    print('Welcome!')
    connect()
