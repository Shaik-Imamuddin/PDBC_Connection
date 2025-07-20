import mysql.connector
def dbConnect():
    connection = mysql.connector.connect(
        host='localhost',
        database='PDBC',
        user='root',
        password='Immu@9866'
    )
    if connection.is_connected():
        print("Connection Established")
        return connection
    return None
dbConnect()