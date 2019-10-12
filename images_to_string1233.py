
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
import mysql.connector
import bs4
from io import BytesIO
import requests



#System path for tesseract.exe
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'




def db_connection(column_name,table_name):
    mydb = mysql.connector.connect(
    host="frombckup.clb8pwlmio9e.ap-south-1.rds.amazonaws.com",
    database="atgworld_p1036",
    user="root",
    passwd="8nRy7EbcMn5r",
    charset='latin1',
    use_unicode=True
    )
    
    mycursor = mydb.cursor(buffered=True)
    c=0
    mycursor.execute('select {} from {}'.format(column_name,table_name))
    row = [item[0] for item in mycursor.fetchall()]
    mydb.close()
    return row


# In[4]:


def img_url(column_name,table_name):
    img_url_list=[]
    posts_list=db_connection(column_name,table_name)
    for user_post in posts_list:
        soup = bs4.BeautifulSoup(user_post, "html.parser")
        images = soup.findAll('img')
        for image in images:
            img_url_list.append(str(image['src']))
    return img_url_list

# def user_posts():
#     mydb = mysql.connector.connect(
#     host="frombckup.clb8pwlmio9e.ap-south-1.rds.amazonaws.com",
#     database="atgworld_p1036",
#     user="root",
#     passwd="8nRy7EbcMn5r",
#     charset='latin1',
#     use_unicode=True
#     )
#     mycursor = mydb.cursor(buffered=True)
#     c=0
#     mycursor.execute('select description from p1036_mst_article')
#     row = [item[0] for item in mycursor.fetchall()]
#     mydb.close()
#     return row




articles_images_url_list=img_url('description','p1036_mst_article')

#len(articles_images_url_list)


for i in range(50):
    im=str(articles_images_url_list[i])
    
    print(im)
    if im.startswith('http'):
        response = requests.get(im)

        try:
            img = Image.open(BytesIO(response.content))
            text=pytesseract.image_to_string(img,lang='eng')
            plt.imshow(img)
            plt.show(img)
            print(text)
            print('-'*50)

        except Exception as e:
            print('Skipping ', i)
            print('Exception found ',e)
            print("Status code",response.status_code)
            print('-'*50)
            i+=1
            continue
    else:
        print('Invalid url')
        print('-'*50)
        continue
        




profile_img_url_list=db_connection('profile_image','p1036_mst_article')




#len(profile_img_url_list)




profile_img_list=[]
for i in profile_img_url_list:
    i=i.replace(' ','')
    if len(i) is not 0:
        p='https://s3.ap-south-1.amazonaws.com/atg-storage-s3/assets/Frontend/images/article_image/'+str(i)
        profile_img_list.append(p)
        


# In[17]:


print('list for profile images\n\n ',profile_img_list)


# In[16]:


for i in range(100):
    im=str(profile_img_list[i])
    
    print(im)
    response = requests.get(im)

    try:
        img = Image.open(BytesIO(response.content))
        text=pytesseract.image_to_string(img,lang='eng')
        plt.imshow(img)
        plt.show(img)
        print(text)
        print('-'*50)

    except Exception as e:
        print('Skipping ', i)
        print('-'*50)
        i+=1
        continue



