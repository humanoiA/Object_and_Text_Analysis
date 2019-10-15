import database_connection
import urllib.request
import bs4
import traceback
from darkflow.net.build import TFNet
import cv2
import os
def img_url():
    img_url_list=list()
    posts_list=database_connection.connect_2_col('id,description','p1036_mst_article')
    #posts_list=user_posts('description','p1036_mst_article')
    #print(posts_list[:25])
    for user_post in posts_list:
        soup = bs4.BeautifulSoup(user_post[1], "html.parser")
        images = soup.findAll('img')
        for image in images:
            if 'atg.world' in str(image['src']) or str(image['src']).startswith('file:') or str(image['src']).endswith('.gif'):
                pass
            else:
                img_url_list.append([str(image['src']),user_post[0]])
    return img_url_list
num=0
img_l=img_url()
options = {"model": "cfg/yolov2.cfg", "load": "bin/yolov2.weights", "threshold": 0.1, "gpu" :0.7}

tfnet = TFNet(options)
for img in img_l:
    #num+=1
    try:    
        urllib.request.urlretrieve(img[0], img[0].split('/')[-1])

        imgcv = cv2.imread(img[0].split('/')[-1])
        result = tfnet.return_predict(imgcv)
        objects=list()
        for things in result:
            if things['confidence']>0.57:
                objects.append(things['label'])
                #print(things['label'])
        myset=set(objects)
        if myset != set():
            print(str(myset)+'-->'+str(img[1]))
            #current_res=result[i]
            #next_res=result[i+1]
            #if current_res['label']!=next_res['label']:
             #   print('Label-->%s'%current_res['label'])
                #print('Confidence-->%s'%current_res['confidence'])
        os.remove(img[0].split('/')[-1])
    except Exception as e:
        pass
        #traceback.print_exc()
        #print(img)#print(db_conn.img_url())