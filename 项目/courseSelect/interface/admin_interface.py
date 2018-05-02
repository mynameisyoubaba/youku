from db import models
import os
from conf import setting
from lib import common
def  register_interface(name,password):
    admin=models.Admin.get_obj_by_name(name)
    if not admin:
        models.Admin(name,password)
        return True,'注册成功'
    else:
        return False,'用户已存在'


def creta_school_interface(admin_name,name,addr):
    school=models.School.get_obj_by_name(name)
    if not school:
        admin=models.Admin.get_obj_by_name(admin_name)
        admin.creat_school(name,addr)
        return True,'创建学校成功'
    else:
        return False,'学校已经存在'



def creat_teacher_interface(admin_name,teacher_name,password='123'):
    teacher=models.Teacher.get_obj_by_name(teacher_name)
    if not teacher:
        admin=models.Admin.get_obj_by_name(admin_name)
        admin.creat_teacher(teacher_name,password)
        return True,'创建老师成功'
    else:
        return False,'老师已经存在'


def check_all_school():
    school_list=common.check_all_file('school')
    return school_list

def creat_course(admin_name,school_name,course_name):
    course=models.Course.get_obj_by_name(course_name)
    if not course:
        admin=models.Admin.get_obj_by_name(admin_name)
        admin.creat_course(course_name)

        school=models.School.get_obj_by_name(school_name)
        school.add_course(course_name)
        return True ,'创建课程成功'
    else:
        return False,'课程已经存在'
