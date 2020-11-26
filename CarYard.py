import sqlite3

connection = sqlite3.connect("Newspaper.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE tblSale
(
saleID VARCHAR(8),
regNo VARCHAR(8),
custID VARCHAR(8),
staffID VARCHAR(8),
date DATE,
salePrice DECIMAL(5,2),
primary key (saleID),
FOREIGN KEY (regNO) REFERENCES tblCar(regNo),
FOREIGN KEY (custID) REFERENCES tblCustomer(custID),
FOREIGN KEY (staffID) REFERENCES tblStaff(staffID)
)
""")

connection.commit()
connection.close()