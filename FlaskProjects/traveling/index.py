from flask import Flask, render_template, request, url_for,redirect,session,flash
import connection 
con=connection.connect()

app = Flask(__name__)
app.secret_key = 'development key'
cur = con.cursor()
cur.execute("select * from m01_menu where m_menu_status=1")
rows = cur.fetchall()
cur.execute("select * from m02_menu where m_menu_status=1")
rows2 = cur.fetchall()
msg=''
@app.route('/')
def index():
    
    return render_template('index.html',rows=rows)
@app.route('/home')
def home():
    return render_template('index.html',rows=rows)

@app.route('/blog')
def blog():
    return render_template('blog.html',rows=rows)

@app.route('/hotels')
def hotels():
    return render_template('hotels.html',rows=rows)

@app.route('/about')
def about():
    return render_template('about.html',rows=rows)


@app.route('/contact')
def contact():
    return render_template('contact.html',rows=rows)

@app.route('/hotelroom')
def hotelroom():
    return render_template('hotel-room.html',rows=rows)

@app.route('/services')
def services():
    return render_template('services.html',rows=rows)

@app.route('/tourplace')
def tourplace():
    return render_template('tour-place.html',rows=rows)

@app.route('/tour')
def tour():
    return render_template('tours.html',rows=rows)
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/recoverpassword')
def recoverpassword():
    return render_template('recover_password.html')

@app.route('/login_dashboard',methods = ['POST', 'GET'])
def login_dashboard():
    if request.method == 'POST':
        cur.execute("select * from m00_site where m00_status=1")
        result = cur.fetchone()
        while result is not None:
            name=result[5]
            password=result[6]
            if request.form['username'] == name :
                if request.form['userpassword'] == password:
                    data={'sitename': result[1], 'contactperson':result[7], 'email': result[4]}
                    session['data'] = data
                    return render_template('/backend/dashboard.html',result=session['data'],rows=rows2)
                else:
                    #return redirect(url_for('login'))
                    return render_template('login.html',error="Wrong Password")

            else:
                #return redirect(url_for('login'))
                return render_template('login.html',error="Wrong Username")
            
@app.route('/dashboard')
def dashboard():          
    return render_template('/backend/dashboard.html',result=session['data'],rows=rows2)
@app.route('/view_add_member')
def view_add_member():
        return render_template('/backend/add_member.html',rows=rows2,result=session['data'])
    
@app.route('/add_member',methods = ['POST', 'GET'])
def add_member():
    msg=''
    if request.method == 'POST':
        try:
            sql="INSERT INTO m03_member_details (m03_mem_name,m03_fname,m_phone_no,m_dob,m_address,m_gender,m_email,m_qualification,m_current_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)" 
            values=(request.form['txtname'],request.form['txtfname'],request.form['txtphone'],request.form['txtdob'],request.form['txtaddress'],request.form['ddgender'],request.form['txtemail'],request.form['ddqualification'],request.form['txtcurrentstatus']) 
            cur.execute(sql,values)
            con.commit()
            msg = "Record successfully added"
            
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            #return redirect(url_for('view_add_member',msg=msg))
            flash(msg)
            return redirect(url_for('view_add_member'))
            #return render_template('/backend/add_member.html',rows=rows2,result=session['data'],msg=msg)
        con.close()
        
@app.route('/member_detail')
def member_detail():
    cur.execute("select * from m03_member_details where m_status=1")
    data = cur.fetchall()
    return render_template("/backend/member_detail.html",data = data,rows=rows2,result=session['data'])

@app.route('/view_edit/<id>')
def view_edit(id):
    cur.execute("select * from m03_member_details where m_status=1 and m03_memid=" +id )
    result2 = cur.fetchone()
    return render_template("/backend/view_edit.html",data = result2,rows=rows2,result=session['data'])


@app.route('/update_member',methods = ['POST', 'GET'])
def update_member():
    msg=''
    if request.method == 'POST':
        try:
            cur.execute("UPDATE  m03_member_details SET m03_mem_name= '" +request.form['txtname']+ "', m03_fname= '" +request.form['txtfname']+ "', m_phone_no= '" +request.form['txtphone']+ "', m_dob= '" +request.form['txtdob']+ "', m_address= '" +request.form['txtaddress']+ "', m_gender= '" +request.form['ddgender']+ "', m_email= '" +request.form['txtemail']+ "', m_qualification= '" +request.form['ddqualification']+ "', m_current_status= '" +request.form['txtcurrentstatus']+ "' where m03_memid = " +request.form['id'])
            con.commit()
            msg = "Record Updated successfully "
            
        except:
            con.rollback()
            msg = "Error in Update operation"

        finally:
            #return redirect(url_for('view_add_member',msg=msg))
            flash(msg)
            return redirect(url_for('member_detail'))
            #return render_template('/backend/add_member.html',rows=rows2,result=session['data'],msg=msg)
        con.close()
        
        
@app.route('/view_delete/<id>')
def view_delete(id):
        msg=''
        try:
            cur.execute("update m03_member_details set m_status=0 where m03_memid =" +id)
            con.commit()
            msg = "Record Deleted successfully "
        except:
            con.rollback()
            msg = "Error in Delete operation"

        finally:
            flash(msg)
            return redirect(url_for('member_detail'))
        con.close()    
        


if __name__ == '__main__':
    app.run(debug = True)