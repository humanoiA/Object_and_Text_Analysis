import mysql.connector

def connect(column_name,table_name):
    mydb = mysql.connector.connect(
    host="frombckup.clb8pwlmio9e.ap-south-1.rds.amazonaws.com",
    database="atgworld_p1036",
    user="root",
    passwd="8nRy7EbcMn5r",
    charset='latin1',
    use_unicode=True
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('select {} from {}'.format(column_name,table_name))
    row = [item[0] for item in mycursor.fetchall()]
    mydb.close()
    return row
def connect_2_col(column_name,table_name):
    mydb = mysql.connector.connect(
    host="frombckup.clb8pwlmio9e.ap-south-1.rds.amazonaws.com",
    database="atgworld_p1036",
    user="root",
    passwd="8nRy7EbcMn5r",
    charset='latin1',
    use_unicode=True
    )
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('select {} from {}'.format(column_name,table_name))
    row = [[str(item[0]),str(item[1])] for item in mycursor.fetchall()]
    mydb.close()
    return row