
from lib import common
from interface import student_interface,common_interface,admin_interface

student_info={
    'name':None
}
def student_register():
    if student_info['name']:
        print('已经登录')
        return
    print('学生注册')
    while True:
        name=input('请输入名字').strip()
        if 'q'== name:break
        password=input('请输入密码').strip()
        conf_password=input('确认密码').strip()
        if password == conf_password:
           flag,msg= student_interface.register_interface(name,password)
           if flag:
               print(msg)
               break
           else:
               print(msg)

        else:
            print('密码不一致')



def student_login():
    if student_info['name']:
        print('已经登录')
        return
    print('学生登录')
    while True:
        name=input('请输入名字:').strip()
        if name == 'q': break
        password=input("请输入密码").strip()
        flag,msg=common_interface.login(name,password,'student')
        if flag:
            print(msg)
            student_info['name']=name
            break
        else:
            print(msg)



@common.login_auth(auth_type='student')
def choose_school():
    print('选择学校')
    while True:
        school_list=admin_interface.check_all_school()
        if not school_list:
            print('学校不存在')
            return
        for i,school in enumerate(school_list):
            print('%s : %s'%(i,school))
        choo_school=input('请选择学校').strip()
        if choo_school.isdigit():
            choo_school=int(choo_school)
            if choo_school<len(school_list):
                flag,msg=student_interface.choose_school_interface(student_info['name'],school_list[choo_school])
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


@common.login_auth(auth_type='student')
def choose_course():
    print('选择课程')
    while True:
        course_list=student_interface.get_course(student_info['name'])
        if not course_list:
            print('没有可选择课程')
            return
        for i,course in enumerate(course_list):
            print('%s : %s '%(i,course))
        choose=input('请选择课程，按数字').strip()
        if choose.isdigit():
            choose=int(choose)
            if choose<len(course_list):
                flag,msg=student_interface.choose_course_interface(student_info['name'],course_list[choose])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)

            else:
                print('请选择存在的课程')

        else:
            print('请输入数字')



@common.login_auth(auth_type='student')
def check_score():
    print('查看成绩')
    scores=student_interface.check_scores(student_info['name'])
    print(scores)


func_dic = {
    '1': student_register,
    '2': student_login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,

}


def student_view():
    while True:
        print('''
        1、注册
        2、登录
        3、选择校区
        4、选择课程
        5、查看成绩

        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()
