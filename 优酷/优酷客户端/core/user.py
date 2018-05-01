import json,struct
import os,sys
import pickle
# from conf import setting
# BASE_DIR=os.path.dirname(os.path.dirname(__file__))
# sys.path.append(BASE_DIR)
# from lib import common
user_info={
    'name':None,
    'is_vip':None,
}
def register(client):
    while True:
        if user_info['name']:
            print('已登录')
            break
        name = input('name').strip()
        pwd = input('pwd').strip()
        conf_pwd = input('conf_pwd').strip()
        user_dic = {
            'name': name,
            'pwd': pwd,
            'vip': None,
            'video_list': [],
            'user_type':'user',
        }
        if pwd == conf_pwd:
            user_dic = json.dumps(user_dic)
            # print(user_dic,type)
            client.send(user_dic.encode('utf-8'))
            data=client.recv(1024).decode('utf-8')
            # print(data,type)
            res = data.split(',')
            if res[0] == '1':
                print(res[1])
                break
            else:
                print(res[1])
                break
        else:
            print('输入有误')
            break
#
def login(client):
    while True:
        name = input('name').strip()
        pwd = input('pwd').strip()
        user_dic = {
            'name': name,
            'pwd': pwd,
            'user_type': 'user',
        }
        user_dic = json.dumps(user_dic)
        # print(user_dic,type)
        client.send(user_dic.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print(data)
        res = data.split(',')
        if res[0] == '1':
            print(res[1])
            user_info={
                'name':name,
                'is_vip':True,
            }
            print(user_info)
            break
        else:
            print(res)
            print(res[1])
            break

# # @common.login_auth('user')
# def vip(client):
#     login(client)
#     pay=input('pay VIP money').strip()
#     if pay.isdigit():
#         print('开通成功')
#
# def check_video(client):
#     list_dir=client.recv(1024)
#     list_dir=pickle.loads(list_dir)
#     for k,v in enumerate(list_dir):
#         print(k,v)
#     quit=input('退出请按Q').strip()
#
# # @common.login_auth
# def download_free_video(client):
#     if user_info['is_vip']:
#         pass
#     else:
#         time=0
#         time+=1
#         if time=='5':
#             print(time)
#             print('广告结束')
#     list_dir = client.recv(1024)
#     list_dir = pickle.loads(list_dir)
#     for k, v in enumerate(list_dir):
#         print(k, v)
#     choose = input('choose').strip()
#     choose = int(choose)
#     name = list_dir[choose]
#     # user_dic=
#     # video_list.
#
#     client.send(name.encode('utf-8'))
#     # 选择文件名，发送下载对应文件的请求，服务端接收请求，服务端发送对应文件的信息
#     head_len_bytes = client.recv(4)  # 先收报头4个bytes,得到报头长度的字节格式
#     x = struct.unpack('i', head_len_bytes)[0]  # 提取报头的长度
#
#     head_bytes = client.recv(x)  # 按照报头长度x,收取报头的bytes格式
#     print(head_bytes,'接收到的bytes')
#     head_bytes=head_bytes.decode('utf-8')
#     print(head_bytes,'decode后的bytes')
#     header = json.loads(head_bytes)  # 提取报头
#     print(header,'header')
#     # 最后根据报头的内容提取真实的数据,比如
#     # real_data_len = conn.recv()
#     path=os.path.join(setting.BASE_DIR,'upload')
#     if not os.path.isdir(path):
#         os.mkdir(path)
#     file_size = header['file_size']
#     current_size = 0
#     file_name=os.path.join(path,name)
#     with open(file_name, 'wb') as f:
#         while current_size < file_size:
#             recv_data = client.recv(8192)
#             f.write(recv_data)
#             current_size += len(recv_data)
#             # print('recvsize:%s filesize:%s' % (current_size, file_size))
#     print('接收成功')
# def other():
#     pass
#
def user_view(client):
    while True:
        print('''
            1.注册
            2.登录
            3.冲会员
            4.查看视频
            5.下载普通视频
            6.下载收费视频
            7.查看观影记录
            8.查看历史公告
            ''')
        func_dic = {
            '1': register,
            '2': login,
            # '3': vip,
            # '4': check_video,
            # '5': download_free_video,
            # '6': other,
        }
        choose = input('choose').strip()
        client.send(choose.encode('utf-8'))
        if choose in func_dic:
            func_dic[choose](client)
        else:
            print('input illegal')
