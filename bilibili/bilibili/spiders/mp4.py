
import threading
import os

'''
for x in os.listdir('./tomcat/full/'):
    video = VideoFileClip('./tomcat/full/'+x)
    L.append(video)
    
    final_clip = concatenate_videoclips(L)
final_clip.to_videofile('./target4.mp4', fps=30, remove_temp=False)
'''
#for filename in os.listdir('./tomcat/full'):
 #   print(filename)

'''
t='https://tx-video.acfun.cn/mediacloud/acfun/acfun_video/segment/CICKthIQ4ImCARpASmtIY2VWbXBMcmhOdUNfMDZfWUx' \
            'VdmNZcDBsZDNqLThaYzFMX2Zic1QtdEhocTBjak5JNU9FdEQ3dWJjRDdpVQ.ts'
b=t.split(r'/segment/')
print(b[1])

/home/mayinghao/bilibili/bilibili/spiders/tomcat/full/
'''
''' 
for listname in os.listdir('./tomcat/full/'):
    newname = listname[len(listname)-8:len(listname)]
    os.rename('./tomcat/full/'+listname, './tomcat/full/' + newname)
'''

'''
def run():
    os.system('cd /home/mayinghao/PycharmProjects/abtv && python socket2.py ')


t = threading.Thread(target=run)
t.start()

 '''


class Info:
    lista = []
    url = ''
    filename = ''
