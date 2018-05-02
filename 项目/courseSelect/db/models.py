from db import db_handler
class BaseClass:
    @classmethod
    def get_obj_by_name(cls,name):
        return db_handler.select(name,cls.__name__.lower())

    def save(self):
       db_handler.save(self)

class Admin(BaseClass):


    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.save()

    def creat_school(self,school_name,school_address):
        school=School(school_name,school_address)
        school.save()

    def creat_course(self,course_name):
        course=Course(course_name)
        course.save()

    def creat_teacher(self,name,password):
        teacher=Teacher(name,password)
        teacher.save()

class School(BaseClass):
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.course_list=[]

    def add_course(self,course_name):
        self.course_list.append(course_name)
        self.save()

class Course(BaseClass):
    def __init__(self,name):
        self.name=name
        self.student_list=[]

    def add_student(self,name):
        self.student_list.append(name)
        self.save()




class Teacher(BaseClass):
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.course_list=[]

    def add_teach_course(self,course_name):
        self.course_list.append(course_name)
        self.save()


    def modify_score(self,student_name,course_name,score):
        obj=Student.get_obj_by_name(student_name)
        obj.scores[course_name]=score
        obj.save()


class Student(BaseClass):
    def __init__(self,name,password):
        self.name=name
        self.password=password
        self.school=None
        self.course_list=[]
        self.scores={}
        self.save()

    def choose_school(self,school):
        self.school=school
        self.save()

    def choose_course(self,course_name):
        self.course_list.append(course_name)
        self.scores[course_name]=0
        self.save()

