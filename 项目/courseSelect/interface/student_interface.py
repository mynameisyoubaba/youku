from db import models

def register_interface(name,password):
    student=models.Student.get_obj_by_name(name)
    if not student:
        models.Student(name,password)
        return True,'注册成功'
    else:
        return False,'用户存在'


def choose_school_interface(student_name,school_name):
    student=models.Student.get_obj_by_name(student_name)
    if student.school:
        return False,'已经选择了学校，不能在选了'
    else:
        student.choose_school(school_name)
        return True,'成功'

def get_course(name):
    student=models.Student.get_obj_by_name(name)

    if student.school:
        school=models.School.get_obj_by_name(student.school)

        return school.course_list
    else:
        return False


def choose_course_interface(name,course_name):
    student=models.Student.get_obj_by_name(name)
    student.choose_course(course_name)
    course=models.Course.get_obj_by_name(course_name)
    course.add_student(name)
    return True,'成功'


def check_scores(name):
    student=models.Student.get_obj_by_name(name)
    return student.scores






