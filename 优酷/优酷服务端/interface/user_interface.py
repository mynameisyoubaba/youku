from db import db_handle
def get_userinfo_interface(user_dic):
    return db_handle.select(user_dic['name'],user_dic['user_type'])
def register_interface(user_dic):
    db_handle.save(user_dic)
def save_interface(user_dic):
    db_handle.save(user_dic)
