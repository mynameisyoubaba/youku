from socket import *
from multiprocessing import Process
from threading import Thread

def send_info(conn,client_addr):
    while True:
        print(client_addr)
        data = conn.recv(1024)
        print(data)
        conn.send(data.upper())
    conn.close()

def server():
    sever = socket(AF_INET, SOCK_STREAM)
    sever.bind(('127.0.0.1', 8080))
    sever.listen(5)
    print('start..')
    while True:
        conn,client_addr=sever.accept()
        p=Thread(target=send_info,args=(conn,client_addr))
        p.start()
    sever.close()
if __name__ == '__main__':
    server()


