# import json,struct
# import os,sys
# import pickle
# from conf import setting
#
# def register(client):
#     name = input('name').strip()
#     pwd = input('pwd').strip()
#     conf_pwd = input('conf_pwd').strip()
#     user_dic = {
#         'name': name,
#         'pwd': pwd,
#         'vip': None,
#         'video_list': [],
#         'user_type':'user',
#     }
#     if pwd == conf_pwd:
#         user_dic = json.dumps(user_dic)
#         # print(user_dic,type)
#         client.send(user_dic.encode('utf-8'))
#         data=client.recv(1024).decode('utf-8')
#         # print(data,type)
#         res = data.split(',')
#         if res[0] == '1':
#             print(res[1])
#         else:
#             print(res[1])
#     else:
#         print('输入有误')
#
# def login(client):
#     name = input('name').strip()
#     pwd = input('pwd').strip()
#     user_dic = {
#         'name': name,
#         'pwd': pwd,
#         'user_type': 'user',
#     }
#     user_dic = json.dumps(user_dic)
#     # print(user_dic,type)
#     client.send(user_dic.encode('utf-8'))
#     data = client.recv(1024).decode('utf-8')
#     # print(data,type)
#     res = data.split(',')
#     if res[0] == '1':
#         print(res[1])
#     else:
#         print(res[1])
#
# def upload_video(client):
#     path = os.path.join(setting.BASE_DIR, 'upload')
#     if os.path.isdir(path):
#         list_dir = os.listdir(path)
#         list_dir = pickle.dumps(list_dir)
#         for k, v in enumerate(list_dir):
#             print(k, v)
#         choose = input('choose').strip()
#         choose = int(choose)
#         name = list_dir[choose]
#     # 上传视频：获得文件路径，自定义报头，for循环发送，标记收费和免费
#     # 为避免粘包,必须自定制报头
#     if not os.path.isdir(path):
#         os.mkdir(path)
#     file_name=os.path.join(path,'11.mp4')
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
#     #客户端开始发送
#     client.send(head_len_bytes) #先发报头的长度,4个bytes
#     client.send(head_bytes) #再发报头的字节格式
#     # client.sendall(data) #然后发真实内容的字节格式
#     current_size=0
#     with open(file_name,'rb') as f:
#         for line in f:
#             client.send(line)
#             current_size+=len(line)
#             print(current_size)
#     print('上传成功')
#
# def del_video(client):
#     list_dir=client.recv(1024)
#     list_dir=pickle.loads(list_dir)
#     for k,v in enumerate(list_dir):
#         print(k,v)
#     choose=input('choose').strip()
#     choose=int(choose)
#     name=list_dir[choose]
#     client.send(name.encode('utf-8'))
#     list_dir=client.recv(1024)
#     list_dir=pickle.loads(list_dir)
#     print('删除后的目录')
#     for k,v in enumerate(list_dir):
#         print(k,v)
#
# def notice(client):
#     notice=input('notice').strip()
#     client.send(notice.encode('utf-8'))
#     data=client.recv(1024)
#     print(data.decode('utf-8'))
#
# def other():
#     pass
#
# def admin_view(client):
#     while True:
#         print('''
#             1.注册
#             2.登录
#             3.上传视频（普通视频，收费视频）
#             4.删除视频（字段标识）
#             5.发布公告
#             6.扩展（总用户量，解锁用户）
#             ''')
#         func_dic = {
#             '1': register,
#             '2': login,
#             '3': upload_video,
#             '4': del_video,
#             '5': notice,
#             '6': other,
#         }
#         choose = input('choose').strip()
#         if choose=='q':break
#         client.send(choose.encode('utf-8'))
#         if choose in func_dic:
#             func_dic[choose](client)
#         else:
#             print('input illegal')
