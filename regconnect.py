#!C:\Users\USER\PycharmProjects\project\venv\Scripts\python.exe

print("Content-Type: text/html")
print()

import cgi

print("<h1 style = \"text-align:center;\">Congratulations</h1>")
print("<hr/>")
print("<h1 style = \"text-align:center;\">Registration has been Successful</h1>")
print("<h6 style = \"text-align:center; font-size:15px;\">Click Here to <a style = \"color:#EB5758; text-decoration:none\" href = \"log.html\">log in</a></h6>")
print("<body bgcolor = '#e0e5ec'>")

form = cgi.FieldStorage()

firstName  = form.getvalue("fname")
lastName  = form.getvalue("lname")
userName  = form.getvalue("uname")
email  = form.getvalue("email")
passs  = form.getvalue("passs")
repass = form.getvalue("repass")

import mysql.connector

con = mysql.connector.connect(user = 'root', password = '', host = 'localhost', database = 'we4us')
cur = con.cursor()

cur.execute("insert into reginfo values(%s, %s, %s, %s, %s, %s)", (firstName, lastName, userName, email, passs, repass))
con.commit()

cur.close()
con.close()