from socket import *
import argparse
import json

BUFSIZ = 1024  # размер буфера 1Кбайт


def parse_args():
    parser = argparse.ArgumentParser(description='Client App')
    parser.add_argument("-a", action="store", dest="addr", type=str, default='localhost',
                        help="enter IP address, default is localhost")
    parser.add_argument("-p", action="store", dest="port", type=int, default=7777,
                        help="enter port number, default is 7777")
    return parser.parse_args()

args = parse_args()
port = args.port
host = args.addr

ADDR = (host, port)

tcpServerSock = socket(AF_INET, SOCK_STREAM)  # создаем сокет сервера
tcpServerSock.bind(ADDR)                      # связываем сокет с адресом
tcpServerSock.listen(5)                       # устанавливаем максимальное число клиентов одновременно обслуживаемых

def build_error_for_client(code, error) -> bytes:
    resp_msg = {
        "response": code,
        "error": error
    }
    resp_msg_str = json.dumps(resp_msg)
    return resp_msg_str.encode("utf-8")

def send_msg_to_client(client, msg: bytes)->None:
    client.send(msg)


while True:                                 # бесконечный цикл сервера
    print('Waiting for client...')
    tcpClientSock, addr = tcpServerSock.accept()  # ждем клиента, при соединении .accept() вернет имя сокета клиента и его адрес (создаст временный сокет tcpClientSock)
    print('Connected from: {}'.format(addr))
    while True:                             # цикл связи
        data = tcpClientSock.recv(BUFSIZ)   # принимает данные от клиента
        if not data:
            break                           # разрываем связь если данных нет
        try:
            data_d = json.loads(data)
        except Exception as e:
            print(e)
            msg = build_error_for_client(400, "bad data")
            send_msg_to_client(tcpClientSock, msg)
            continue

        if "action" not in data_d:
            code = 400
            error = "Action field is req"
            resp_msg_b = build_error_for_client(code=code, error=error)
            send_msg_to_client(tcpClientSock, resp_msg_b)
            continue

        action = data_d["action"]

        if action == "auth":
            user = data_d["user"]
            login = user["login"]
            if login != "admin":
                code = 500
                error = "admin only"

                resp_msg_b = build_error_for_client(code=code, error=error)
                send_msg_to_client(tcpClientSock, resp_msg_b)
            else:
                resp_msg = {
                    "response": 200,
                    "alert": "Hello admin !"
                }
                resp_msg_str = json.dumps(resp_msg)
                resp_msg_b = resp_msg_str.encode("utf-8")
                send_msg_to_client(tcpClientSock, resp_msg_b)
    tcpClientSock.close()
tcpServerSock.close()                          # закрытие сокета сервера