# # import os
# from conf import setting
# # path=os.path.join(setting.BASE_DIR,'upload')
# # if os.path.isdir(path):
# #     list_dir=os.listdir(path)
# #
# #     for k, v in enumerate(list_dir):
# #         print(k, v)
#
# import os, sys
#
# # 列出目录
# print ("目录为: %s"%os.listdir(os.getcwd()))
#
# # 重命名
# name='12.mp4'
# os.rename(os.path.join(setting.BASE_DIR,'upload','%s'%name),os.path.join(setting.BASE_DIR,'upload','%s-已删除'%name))
#
# print ("重命名成功。")
#
# # 列出重命名后的目录
# print ("目录为: %s" %os.listdir(os.getcwd()))
from socket import *
try:
    # 接收客户端的链接请求
    conn, client_addr = server.accept()
    print('已连接，', client_addr)
    # 接收客户端的发送的信息
    choose = conn.recv(1024).decode('utf-8')
    print(choose)
    # 判断是否在字典内
    if choose in func_dic:
        func_dic[choose](conn, client_addr)
    else:
        print('input illegal')
# 客户端断开异常处理
except ConnectionResetError:
    break
    pass