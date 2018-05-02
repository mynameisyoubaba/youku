from socket import *

sever=socket(AF_INET,SOCK_STREAM)
sever.bind(('127.0.0.1',8080))
sever.listen(5)

while True:
    conn,client_addr=sever.accept()
    while True:
        print(client_addr)
        data=conn.recv(1024)
        print(data)
        conn.send(data.upper())
    conn.close()
sever.close()