from lib import common
from interface import common_interface,teacher_interface
teacher_info={
    'name':None
}
def teacher_login():
    if teacher_info['name']:
        print('已经登录')
        return
    print('老师登录')
    while True:
        name=input('请输入名字:').strip()
        if name == 'q': break
        password=input("请输入密码").strip()
        flag,msg=common_interface.login(name,password,'teacher')
        if flag:
            print(msg)
            teacher_info['name']=name
            break
        else:
            print(msg)

@common.login_auth(auth_type='teacher')
def check_course():
    print('查看教授课程')
    course_list=teacher_interface.check_teach_course(teacher_info['name'])
    if not course_list:
        print('请先选择课程')
        return
    for course in course_list:
        print(course)


@common.login_auth(auth_type='teacher')
def choose_course():
    print('选择教授课程')
    course_list=teacher_interface.check_all_course()
    if not course_list:
        print('请先联系管理员创建课程')
        return
    while True:
        for i,course in enumerate(course_list):
            print('%s :%s'%(i,course))

        choose=input('请选择课程（数字）').strip()
        if choose == 'q':break
        if choose.isdigit():
            choose=int(choose)
            if choose<len(course_list):
                flag,msg=teacher_interface.choose_teach_course(teacher_info['name'],course_list[choose])
                if flag:
                    print(msg)
                    break
                else:
                    print(msg)
            else:
                print('请输入范围内的数字')

        else:
            print('请输入数字')

@common.login_auth(auth_type='teacher')
def check_student():
    print('查看课程下学生')
    while True:
        course_list = teacher_interface.check_teach_course(teacher_info['name'])
        if not course_list:
            print('请先选择课程')
            return
        for i,course in enumerate(course_list):
            print('%s:%s'%(i,course))
        choose = input('请选择课程（数字）').strip()
        if choose == 'q': break
        if choose.isdigit():
            choose = int(choose)
            if choose < len(course_list):
                student_list=teacher_interface.check_students_interface(course_list[choose])
                for i,student in enumerate(student_list):
                    print('%s:%s'%(i,student))
                break

            else:
                print('请输入范围内的数字')
        else:
            print('请输入数字')


@common.login_auth(auth_type='teacher')
def modify_score():
    print('修改成绩')
    while True:
        course_list = teacher_interface.check_teach_course(teacher_info['name'])
        if not course_list:
            print('请先选择课程')
            return
        for i, course in enumerate(course_list):
            print('%s:%s' % (i, course))
        choose = input('请选择课程（数字）').strip()
        if choose == 'q': break
        if choose.isdigit():
            choose = int(choose)
            if choose < len(course_list):
                student_list = teacher_interface.check_students_interface(course_list[choose])
                for i, student in enumerate(student_list):
                    print('%s:%s' % (i, student))
                choose2=input('请选择学生编号：').strip()
                if choose2.isdigit():
                    choose2=int(choose2)
                    score=input('请输入分数').strip()
                    if score.isdigit():
                        score=int(score)
                        # teacher_name, student_name, course_name, score
                        flag,msg=teacher_interface.modify_score_interface(teacher_info['name'],student_list[choose2],course_list[choose],score)
                        if flag:
                            print(msg)
                            break
                        else:
                            print(msg)
                    else:
                        print('请输入数字')
                        continue
                else:
                    print('请输入数字')
                    continue


            else:
                print('请输入范围内的数字')
        else:
            print('请输入数字')


func_dic = {
    '1': teacher_login,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': modify_score,

}


def teacher_view():
    while True:
        print('''
        1、登录
        2、查看教授课程
        3、选择教授课程
        4、查看课程下学生
        5、修改学生成绩
        ''')
        choice = input('please choice>>:').strip()
        if choice == 'q': break
        if choice not in func_dic: continue

        func_dic[choice]()