
import os
from conf import setting

def login_auth(auth_type):
    from core import admin,student,teacher
    def auth(fun):
        def wrapper(*args,**kwargs):
            if auth_type=='admin':
                if not admin.admin_info['name']:
                    print('管理员没登录')
                    admin.admin_login()
                else:
                    return fun(*args,**kwargs)
            elif auth_type=='student':
                if not student.student_info['name']:
                    print('学生没登录')
                    student.student_login()
                else:
                    return fun(*args,**kwargs)
            elif auth_type == 'teacher':
                if not teacher.teacher_info['name']:
                    print('老师没登录')
                    teacher.teacher_login()
                else:
                    return fun(*args,**kwargs)
        return wrapper
    return auth



def check_all_file(type):
    path=os.path.join(setting.BASE_DB,type)
    if not os.path.isdir(path):
        os.mkdir(path)
    file_list=os.listdir(path)
    return file_list
