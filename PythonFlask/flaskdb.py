from flask import Flask, render_template, request
import connection 
app = Flask(__name__)
con=connection.connect()
msg=''


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/enternew')
def new_student():
   return render_template('student2.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   msg=''
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']

         #with connection.connect() as con:
       
         cur = con.cursor()
         #cur.execute("CREATE TABLE customer (emp_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255) , email varchar(255))")

         sql="INSERT INTO students (name,addr,city,pin) VALUES (%s,%s,%s,%s)" 
         values=(nm,addr,city,pin) 
         cur.execute(sql,values)
         con.commit()
         #print(cur._last_executed)
         msg = "Record successfully added"
      except:
            con.rollback()
            msg = "error in insert operation"

      finally:
               return render_template("resul2.html",msg = msg)
      con.close()

@app.route('/list')
def list():
      #con = connection.connect()
      cur = con.cursor()
      cur.execute("select * from students")

      rows = cur.fetchall()
      return render_template("list.html",rows = rows)
   
if __name__ == '__main__':
   app.run(debug = True)        #con.row_factory = con.Row

              