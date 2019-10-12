import mysql.connector
def user_posts():
    mydb = mysql.connector.connect(
    host="frombckup.clb8pwlmio9e.ap-south-1.rds.amazonaws.com",
    database="atgworld_p1036",
    user="root",
    passwd="8nRy7EbcMn5r",
    charset='latin1',
    use_unicode=True
    )
    '''mydb=mysql.connector.connect(host='localhost',
                                            database='aryu',
                                            user='root',
                                            password='6ff949d8e428')
    '''
    #print(mydb)
    #batch_size = 42
    mycursor = mydb.cursor(buffered=True)
    c=0
    mycursor.execute('select description from p1036_mst_article')
    '''count=mycursor.fetchone()[0]
    batch=5000
    for i in range(1,count,batch):
        mycursor.execute('select * from p1036_mst_article LIMIT {},{}'.format(i,i+batch))
        for row in mycursor:
        c+=1
        if c>200:
            break'''
    '''
    c=0
    for row in mycursor:
        print(row)
        c+=1'''
    row = [item[0] for item in mycursor.fetchall()]
    #print(len(row))
    mydb.close()
    return row