import database_connection
import bs4
#from darkflow.net.build import TFNet
import cv2
from bs4 import BeautifulSoup
from bs4.element import Comment
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
def tag_visible(element):
    '''This function is a helper function to removes all the html tags from the element
            it finds all visible text excluding scripts, comments, css etc.
            
            return:
                True or False
    '''
    #function to remove html tags
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    ''' This function is used to extract text from html page ,it uses function tag_visible() as a helper funciton 
            parameter:
                html content of page
            return:
                String of all visible text
    '''
    #function to extract text from html page
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)
stop = stopwords.words('english')
articles=database_connection.connect_2_col('id,description','p1036_mst_article')
predefined_groups=database_connection.connect('group_name','p1036_mst_group')
for i in articles:
    word_tokens_post = word_tokenize(text_from_html(i[1]))
    for j in range(len(predefined_groups)):
        w_token=word_tokenize(str(predefined_groups[j]))
        filter_grp=[a for a in w_token if a not in stop]
        predefined_groups[j]=' '.join(filter_grp)
    #lmtzr = WordNetLemmatizer()
    #group_list=str()
    filtered_sentence = [a for a in word_tokens_post if a not in stop]
    filtered_sentence=[x.lower() for x in filtered_sentence]
    for j in range(len(predefined_groups)):
        if predefined_groups[j].lower() in filtered_sentence:
            print(str(predefined_groups[j])+'-->'+str(i[0]))
    #filtered_groups=[a for a in word_tokens if a not in stop]