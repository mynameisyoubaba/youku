# from core import admin,user
# from socket import *
# client=socket(AF_INET,SOCK_STREAM)
# client.connect(('127.0.0.1',8080))
# def login_auth(type):
#     def auth(func):
#         def wrapper(*args,**kwargs):
#             if type=='user':
#                 if user.user_info['name']:
#                     pass
#                 else:
#                     print('请先登录')
#                     user.login(client)
#             return func(*args,**kwargs)
#         return wrapper
#     return auth
#
