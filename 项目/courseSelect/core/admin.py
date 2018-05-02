from lib import common
from interface import admin_interface
from interface import common_interface
admin_info={
    'name':None
}
def admin_register():
    if admin_info['name']:
        print('已经登录')
        return
    print('管理员注册')
    while True:
        name=input('请输入您的名字:').strip()
        if name=='q':break
        password=input('请输入密码：').strip()
        con_password=input('请确认密码：').strip()
        if password == con_password:
            flag,msg=admin_interface.register_interface(name,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致 ')


def admin_login():
    if admin_info['name']:
        print('已经登录')
        return
    print('管理员登陆')
    while True:
        name=input('请输入名字:').strip()
        if name == 'q': break
        password=input("请输入密码").strip()
        flag,msg=common_interface.login(name,password,'admin')
        if flag:
            print(msg)
            admin_info['name']=name
            break
        else:
            print(msg)



@common.login_auth(auth_type='admin')
def creat_school():
    print('创建学校')
    while True:
        school_name=input('学校名称').strip()
        schoocl_addr=input('学校地址').strip()
        flag,msg=admin_interface.creta_school_interface(admin_info['name'],school_name,schoocl_addr)
        if flag:
            print(msg)
            break
        else:
            print(msg)



@common.login_auth(auth_type='admin')
def creat_teacher():
    print('创建老师')
    while True:
        name=input('老师名字').strip()
        flag,msg=admin_interface.creat_teacher_interface(admin_info['name'],name)
        if flag:
            print(msg)
            break
        else:
            print(msg)

@common.login_auth(auth_type='admin')
def creat_course():
    while True:
        school_list=admin_interface.check_all_school()
        for i,school in enumerate(school_list):
            print('%s : %s'%(i,school))

        choo_school=input('请选择学校').strip()
        if choo_school.isdigit():
            choo_school=int(choo_school)
            if choo_school>=0 and choo_school<len(school_list):
                # school_list[choo_school]
                course_name=input('课程名字 ').strip()
                flag,msg=admin_interface.creat_course(admin_info['name'],school_list[choo_school],course_name)
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
                    continue
            else:
                print('请选择存在的学校')
                continue
        else:
            print('请输入数字')
            continue


func_dic = {
    '1': admin_register,
    '2': admin_login,
    '3': creat_school,
    '4': creat_teacher,
    '5': creat_course

}


def admin_view():
    while True:
        print('''
        1、注册
        2、登录
        3、创建学校
        4、创建老师
        5、创建课程
        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()
