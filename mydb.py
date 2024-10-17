import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'DP042354',
    )

#prepare cursor object (using the connector declare above)
cursorObject = dataBase.cursor() 

# #create data base, Creates Data base but there is an error if it is already created
# cursorObject.execute("CREATE DATABASE 3340data") 

#Message in console to see if it worked 
print("Hello data base 3340data")