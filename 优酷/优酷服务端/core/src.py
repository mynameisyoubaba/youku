from socket import *
from core import user,admin

def user_view(conn,client_addr):
    user.run(conn,client_addr)
def admin_view(conn,client_addr):
    # admin.run(conn,client_addr)
    pass

def run():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print('start')
    while True:
        func_dic={
            '1':user_view,
            '2':admin_view,
        }
        # 接收客户端的链接请求
        conn,client_addr=server.accept()
        print('已连接，',client_addr)
        # 接收客户端的发送的信息
        print('接收客户端的发送的信息')
        choose=conn.recv(1024).decode('utf-8')
        print(choose)
        # 判断是否在字典内
        if choose in func_dic:
            print('choose为真')
            func_dic[choose](conn,client_addr)
        else:
            print('input illegal')
#