# import json
# import os
# import pickle
# import struct
# from conf import setting
# from db import db_handle
# from interface import user_interface
# def register(conn,client_addr):
#     print('注册功能开始')
#     user_dic=conn.recv(1024).decode('utf-8')
#     # print(user_dic,type)
#     user_dic=json.loads(user_dic)
#     # print(user_dic,type)
#     user_info = user_interface.get_userinfo_interface(user_dic)
#     if not user_info:
#         user_interface.register_interface(user_dic)
#         conn.send('1,注册成功'.encode('utf-8'))
#     else:
#         conn.send('0,注册失败，账户已存在'.encode('utf-8'))
#     print('注册功能结束')
#
# def login(conn,client_addr):
#     print('登录功能开始')
#     user_dic = conn.recv(1024).decode('utf-8')
#     # print(user_dic,type)
#     user_dic = json.loads(user_dic)
#     # print(user_dic,type)
#     user_info = user_interface.get_userinfo_interface(user_dic)
#     if user_info:
#         if user_dic['name']==user_info['name'] and user_dic['pwd']==user_info['pwd']:
#             conn.send('1,登录成功'.encode('utf-8'))
#         else:
#             conn.send('2,密码不正确'.encode('utf-8'))
#     else:
#         conn.send('0,用户不存在'.encode('utf-8'))
#     print('登录功能结束')
# def upload_video(conn,client_addr):
#     # 服务端开始接收
#     head_len_bytes = conn.recv(4)  # 先收报头4个bytes,得到报头长度的字节格式
#     x = struct.unpack('i', head_len_bytes)[0]  # 提取报头的长度
#
#     head_bytes = conn.recv(x)  # 按照报头长度x,收取报头的bytes格式
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
#     file_name=os.path.join(path,'11.mp4')
#     with open(file_name, 'wb') as f:
#         while current_size < file_size:
#             recv_data = conn.recv(8192)
#             f.write(recv_data)
#             current_size += len(recv_data)
#             print('recvsize:%s filesize:%s' % (current_size, file_size))
#     print('接收成功')
#     # conn.recv(real_data_len)
# def del_video(conn,client_addr):
#     path=os.path.join(setting.BASE_DIR,'upload')
#     if os.path.isdir(path):
#         list_dir=os.listdir(path)
#         list_dir=pickle.dumps(list_dir)
#         conn.send(list_dir)
#         name=conn.recv(1024)
#         name=name.decode('utf-8')
#         os.rename(os.path.join(setting.BASE_DIR, 'upload', '%s' % name),
#                   os.path.join(setting.BASE_DIR, 'upload', '%s-已删除' % name))
#         list_dir = os.listdir(path)
#         list_dir = pickle.dumps(list_dir)
#         conn.send(list_dir)
# def notice(conn,client_addr):
#     data=conn.recv(1024)
#     data=data.decode('utf-8')
#     notice_path=os.path.join(setting.BASE_DIR,'notice')
#     if not os.path.isdir(notice_path):
#         os.mkdir(notice_path)
#     file_path=os.path.join(notice_path,'notice.txt')
#     with open(file_path,'a',encoding='utf-8') as f:
#         f.write(data)
#     conn.send('发布成功'.encode('utf-8'))
#
# def run(conn,client_addr):
#     while True:
#         func_dic={
#             '1':register,
#             '2':login,
#             '3':upload_video,
#             '4':del_video,
#             '5':notice,
#         }
#         try:
#             # 接收客户端的发送的信息
#             choose=conn.recv(1024).decode('utf-8')
#             if choose == 'q': break
#             # 判断是否在字典内
#             if choose in func_dic:
#                 func_dic[choose](conn,client_addr)
#             else:
#                 print('input illegal(admin)')
#                 break
#         # 客户端断开异常处理
#         except ConnectionResetError:
#             break
