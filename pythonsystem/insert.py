import sqlite3
#conn = sqlite3.connect('database.db')

with sqlite3.connect("database.db") as con:cur = con.cursor()
print ("Opened database successfully");
cur.execute("INSERT INTO students (name,addr,city,pin)VALUES ('abc1','aa 20','aaa1','1234a')")

con.commit()
msg = "Record successfully added"
print (msg)
con.close()