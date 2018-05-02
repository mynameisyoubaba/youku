import os
from conf import setting
import pickle
def save(obj):
    path=os.path.join(setting.BASE_DB,obj.__class__.__name__.lower())
    if not os.path.isdir(path):
        os.mkdir(path)
    path_file=os.path.join(path,obj.name)
    with open(path_file,'wb') as f:
        pickle.dump(obj,f)



def select(name,type):
    path=os.path.join(setting.BASE_DB,type)
    if not os.path.isdir(path):
        os.mkdir(path)

    path_file=os.path.join(path,name)
    if os.path.exists(path_file):
        with open(path_file,'rb') as f:
            return pickle.load(f)

    return False