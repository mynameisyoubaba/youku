from core import user,admin
from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


def user_view(client):
    user.user_view(client)
def admin_view(client):
    admin.admin_view(client)

def run():
    while True:
        print('''
        1.客户登录
        2.管理员登录
        ''')
        func_dic={
            '1':user_view,
            '2':admin_view,
        }
        choose=input('choose').strip()
        if choose=='q':break
        client.send(choose.encode('utf-8'))
        # 判断是否在字典内
        if choose in func_dic:
            func_dic[choose](client)
        else:
            print('input illegal')


