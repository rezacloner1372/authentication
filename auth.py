import mysql.connector
import re
from mysql.connector import errorcode
print('connecting to db')
try:
  mydb = mysql.connector.connect(
    user="",
    password='',
    host="",
    database=""
)
  print('connected to db')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

mycursor = mydb.cursor()
def askname():
  username = input("username:")
  if re.match(r"[^@]+@[a-zA-Z]+\.[a-zA-Z]+", username):
    print("address is valid")
    password = input("password (string and int):")
    if re.match(r"[a-zA-Z]+[0-9 ]", password):
      print("password is valid")
    else:
      print("password is not valid use strin and int")
      askname()
    return mycursor.execute("INSERT INTO auth (username, password) VALUES (%s, %s)" , ( username,password ))
  else:
    print("not valid exp: expression@string.string")
    askname()
askname()
mydb.commit()
