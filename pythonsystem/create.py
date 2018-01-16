import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";

conn.execute('CREATE TABLE students (ID INT PRIMARY KEY NOT NULL,name TEXT NOT NULL, sur TEXT NOT NULL, addr TEXT, city TEXT, telephone INTEGER(10) NOT NULL)')
print "Table created successfully";
conn.close()