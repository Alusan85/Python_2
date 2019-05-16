from socket import *
import argparse
import json

BUFSIZ = 1024

def parse_args():
    parser = argparse.ArgumentParser(description='Server App')
    parser.add_argument("-a", action="store", dest="addr", type=str, default='localhost',
                        help="enter IP address, default is localhost")
    parser.add_argument("-p", action="store", dest="port", type=int, default=7777,
                        help="enter port number, default is 7777")
    return parser.parse_args()

args = parse_args()
port = args.port
host = args.addr

ADDR = (host, port)

tcpClientSock = socket(AF_INET, SOCK_STREAM)
tcpClientSock.connect(ADDR)  # установка связи с сервером

while True:
    data = input('Введите логин, или пустое поле или хотите выйти > ')  # ввод данных для отправки
    if not data:
        break
    if data == "admin":
        message_dict = {
            "action": "auth",
            "user": {
                "login": "admin",
                "pwd": "sha256"
            }
        }
    else:
        message_dict = {
            "action": "auth",
            "user": {
                "login": "not_admin",
                "pwd": "sha256"
            }
        }

    msg = json.dumps(message_dict)
    msg_b = msg.encode('utf-8')
    tcpClientSock.send(msg_b)

    data = tcpClientSock.recv(BUFSIZ)  # ожидание (получение) ответа
    if not data:
        break
    print('Сообщение от сервера: ', data.decode('utf-8'), 'длинной', len(data), 'байт')
tcpClientSock.close()