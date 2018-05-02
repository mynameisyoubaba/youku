import json
# import os
# import pickle
# import struct
# from conf import setting
# from db import db_handle
from interface import user_interface
def register(conn,client_addr):
    print('注册功能开始')
    user_dic=conn.recv(1024).decode('utf-8')
    # print(user_dic,type)
    user_dic=json.loads(user_dic)
    # print(user_dic,type)
    user_info = user_interface.get_userinfo_interface(user_dic)
    if not user_info:
        user_interface.register_interface(user_dic)
        conn.send('1,注册成功'.encode('utf-8'))
    else:
        conn.send('0,注册失败，账户已存在'.encode('utf-8'))
    print('注册功能结束')
def login(conn,client_addr):
    print('登录功能开始')
    user_dic = conn.recv(1024).decode('utf-8')
    # print(user_dic,type)
    user_dic = json.loads(user_dic)
    # print(user_dic,type)
    user_info = user_interface.get_userinfo_interface(user_dic)
    if user_info:
        if user_dic['name']==user_info['name'] and user_dic['pwd']==user_info['pwd']:
            conn.send('1,登录成功'.encode('utf-8'))
            return user_info
        else:
            conn.send('2,密码不正确'.encode('utf-8'))
    else:
        conn.send('0,用户不存在'.encode('utf-8'))
    print('登录功能结束')
def vip(conn,client_addr):
    user_info=login(conn, client_addr)
    print(user_info['vip'])
    user_info['vip']=True
    user_interface.save_interface(user_info)
def check_video(conn,client_addr):
    path = os.path.join(setting.BASE_DIR, 'upload')
    if os.path.isdir(path):
        list_dir = os.listdir(path)
        list_dir = pickle.dumps(list_dir)
        conn.send(list_dir)
#
# def download_free_video(conn,client_addr):
#     path = os.path.join(setting.BASE_DIR, 'upload')
#     if os.path.isdir(path):
#         list_dir = os.listdir(path)
#         list_dir = pickle.dumps(list_dir)
#         conn.send(list_dir)
#     name = conn.recv(1024)
#     name = name.decode('utf-8')
#     path=os.path.join(setting.BASE_DIR,'upload')
#     if not os.path.isdir(path):
#         os.mkdir(path)
#     file_name=os.path.join(path,name)
#     file_size = os.path.getsize(file_name)
#     print(file_size,'文件大小')
#     header = {'file_size': file_size, 'file_name': file_name,
#               'md5': '8f6fbf8347faa4924a76856701edb0f3'}  # 1T数据,文件路径和md5值
#     # 为了该报头能传送,需要序列化并且转为bytes
#     head_bytes = bytes(json.dumps(header), encoding='utf-8')  # 序列化并转成bytes,用于传输
#     # 为了让客户端知道报头的长度,用struck将报头长度这个数字转成固定长度:4个字节
#     head_len_bytes = struct.pack('i', len(head_bytes))  # 这4个字节里只包含了一个数字,该数字是报头的长度
#     # 真实内容的字节格式
#     with open(file_name,'rb') as f:
#         data=f.read()
#     #服务端开始发送
#     conn.send(head_len_bytes) #先发报头的长度,4个bytes
#     conn.send(head_bytes) #再发报头的字节格式
#     # client.sendall(data) #然后发真实内容的字节格式
#     current_size=0
#     with open(file_name,'rb') as f:
#         for line in f:
#             conn.send(line)
#             current_size+=len(line)
#             print(current_size)
#     print('发送给客户端成功')
def run(conn,client_addr):
    while True:
        print('user_view开始')
        func_dic={
            '1':register,
            '2':login,
            # '3':vip,
            # '4':check_video,
            # '5':download_free_video,
            # '6': 1,
        }
        try:
            # 接收客户端的发送的信息
            choose=conn.recv(1024).decode('utf-8')
            if choose == 'q': break
            # 判断是否在字典内
            if choose in func_dic:
                print('1.3')

                func_dic[choose](conn,client_addr)
            else:
                print('input illegal')
                break
        # 客户端断开异常处理
        except ConnectionResetError:
            break
