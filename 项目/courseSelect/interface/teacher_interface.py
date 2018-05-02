from lib import common
from db import models

def check_all_course():
    return common.check_all_file('course')


def check_teach_course(teacher_name):
    obj=models.Teacher.get_obj_by_name(teacher_name)
    return obj.course_list


def choose_teach_course(teacher_name,course_name):
    obj=models.Teacher.get_obj_by_name(teacher_name)
    obj.add_teach_course(course_name)
    return True,'选课成功'


def check_students_interface(course_name):
    obj=models.Course.get_obj_by_name(course_name)
    return obj.student_list


def modify_score_interface(teacher_name,student_name,course_name,score):
    obj=models.Teacher.get_obj_by_name(teacher_name)
    obj.modify_score(student_name,course_name,score)
    return True,'修改成功'

