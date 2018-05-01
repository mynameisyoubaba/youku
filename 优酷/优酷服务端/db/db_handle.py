import json
import os

from conf import setting
def select(name,type):
    path=os.path.join(setting.BASE_DB,type)
    if not os.path.isdir(path):
        os.mkdir(path)
    file_path=os.path.join(path,'%s.json'%name)
    if os.path.exists(file_path):
        with open(file_path,'r',encoding='utf-8') as f:
            return json.load(f)
    else:
        return False

def save(user_dic):
    path=os.path.join(setting.BASE_DB,user_dic['user_type'])
    if not os.path.isdir(path):
        os.mkdir(path)
    file_path=os.path.join(path,'%s.json'%user_dic['name'])
    # print(user_dic,type)
    with open(file_path,'w',encoding='utf-8') as f:
        json.dump(user_dic,f)
