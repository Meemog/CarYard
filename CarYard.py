import sqlite3

connection = sqlite3.connect("NewsPaper.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE tblStaff
(
staffID VARCHAR(8),
firstName VARCHAR(15),
surName VARCHAR(15),
primary key (staffID)
)
""")

connection.commit()
connection.close()