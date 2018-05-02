import json
from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
def view():
    while True:
        print('''
        1.注册
        2.登录
        3.上传
        4.下载
        ''')
        func_dic={
            '1':register,
            '2':login,
            '3':upload,
            '4':download,
        }
        choose=input('choose').strip()
        func_dic[choose]()
def register():
    while True:
        name = input('name').strip()
        pwd = input('pwd').strip()
        conf_pwd=input('conf_pwd').strip()
        if pwd==conf_pwd:
            date_packet={
                'func':'register',
                'user_register_info':{'name':name,'pwd':pwd,}
            }
            client_info=json.dumps(date_packet)
            client.send(client_info.encode('utf-8'))
            res=client.recv(1024)
            res=res.decode('utf-8')
            res=json.loads(res)
            if res['flag']=='True':
                print('注册成功')
                break
            else:
                print('账户已存在')
        else:
            print('两次密码输入不一致')
def login():
    while True:
        name = input('name').strip()
        pwd = input('pwd').strip()
        date_packet={
            'func':'login',
            'user_login_info':{'name':name,'pwd':pwd,}
        }
        client_info=json.dumps(date_packet)
        client.send(client_info.encode('utf-8'))
        res=client.recv(1024)
        res=res.decode('utf-8')
        res=json.loads(res)
        if res['flag']=='true':
            print('登录成功')
            break
        else:
            print('账户或密码错误')
def upload():
    pass
def download():
    pass
while True:
    view()
    # client.send(name.encode('utf-8'))
    # user_name = client.recv(1024)
    # print(user_name)
    # client.send(pwd.encode('utf-8'))
    # login_info=client.recv(1024)
    # print(login_info.decode('utf-8'))

    # print(msg.decode('utf-8'))

