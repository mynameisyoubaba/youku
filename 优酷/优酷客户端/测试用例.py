# res='1,success'.split(',')
# if res[0]=='1':
#     print(res[1])
#
# import os
#
# file_size=os.path.getsize(r"C:\Users\sjh\PycharmProjects\优酷客户端\upload\沧海一声笑-GAI.flac")
# print(file_size)

def del_video(client):
    list_dir=client.recv(1024)
    list_dir=pickle.loads(list_dir)
    for k,v in enumerate(list_dir):
        print(k,v)
    choose=input('choose').strip()
    choose=int(choose)
    name=list_dir[choose]
    client.send(name.encode('utf-8'))
    list_dir=client.recv(1024)
    list_dir=pickle.loads(list_dir)
    print('删除后的目录')
    for k,v in enumerate(list_dir):
        print(k,v)