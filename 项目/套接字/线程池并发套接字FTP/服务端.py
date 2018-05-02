from socket import *
import os
from multiprocessing import Process
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
Tpool=ThreadPoolExecutor(3)
import json
path=os.path.dirname(__file__)
print(path)
def register_interface(name,pwd):
    path=os.path.dirname(__file__)
    BASE_DB=os.path.join(path,'db')
    with open('%s/%s.json'%(BASE_DB,name),'w',encoding='utf-8'):
        pass
# def register(conn,client_info):
#     print('注册开始')
#     if client_info['user_register_info']['name'] in :
#         res={'flag':'true','msg':'登录成功'}
#         res=json.dumps(res).encode('utf-8')
#         conn.send(res)
#     else:
#         res=('true','登录成功',)
#         conn.send(res)
# def login(conn,client_info):
#     print('登录开始')
#     if client_info['user_login_info']['name']== user_dic['name'] and client_info['user_login_info']['pwd'] == user_dic['pwd']:
#         res={'flag':'True','msg':'登录成功'}
#         res=json.dumps(res).encode('utf-8')
#         conn.send(res)
#     else:
#         res=('False','用户名或密码错误',)
#         conn.send(res)
def upload():
    pass
def download():
    pass
def send_info(conn,client_addr):
    while True:
        print(client_addr)
        client_info = conn.recv(1024)
        client_info = client_info.decode('utf-8')
        client_info=json.loads(client_info)
        if client_info['func'] =='login':
            login(conn,client_info)
    conn.close()


def server():
    sever = socket(AF_INET, SOCK_STREAM)
    sever.bind(('127.0.0.1', 8080))
    sever.listen(5)
    print('start..')
    while True:
        conn,client_addr=sever.accept()
        Tpool.submit(send_info,conn,client_addr)

    sever.close()
if __name__ == '__main__':
    server()


