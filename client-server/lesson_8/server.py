import socket
from sys import argv
import log.server_log_config
import log
from logging.handlers import TimedRotatingFileHandler
import logging

logger = logging.getLogger('server')
logger.setLevel(logging.INFO)
logger.addHandler(log.server_log_config.handler)

UDP_len = 65535
script, host, port = argv


def listen(host=str(host), port=int(port)):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print(f'listening: {host}: {port}')
    logger.info(f'SERVER: listening: {host}: {port}')

    members = []
    while True:
        msg, addr = s.recvfrom(UDP_len)

        if addr not in members:
            members.append(addr)

        if not msg:
            continue

        client_id = addr[1]
        msg_text = msg.decode('utf-8')
        if msg_text == '__join':
            print(f'Client{client_id} is here')
            logger.info(f'SERVER: Client{client_id} connected')
            continue
        elif msg_text == '__disconnect':
            print(f'Client {client_id} is disconnected')
            logger.info(f'SERVER: Client {client_id} is disconnected')
            members.remove(addr)

        message_carcas = '{}__{}'
        if msg_text == '__members':
            print(f'Client {client_id} requested members')
            active = [f'client{m[1]}' for m in members if m != addr]
            members_msg = ';'.join(active)
            s.sendto(message_carcas.format('members', members_msg).encode('utf-8'), addr)
            continue


if __name__ == '__main__':
    listen()
