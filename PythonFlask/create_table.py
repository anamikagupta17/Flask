import connection
con=connection.connect()
mycursor = con.cursor()
#mycursor.execute("CREATE TABLE employees (emp_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255) , email varchar(255))")
#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Shobhit", "Mooda ")
#mycursor.execute(sql, val)
id=mycursor.lastrowid
print(mycursor.rowcount, "record inserted.")
print(id)

mycursor.execute("SELECT * FROM customers")
myresult2 = mycursor.fetchone()
"""myresult = mycursor.fetchall()


for x in myresult:
  print(x)"""
  
print(myresult2)