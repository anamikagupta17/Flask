from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
 return "Hello Anamika"
 
if __name__ == 	'__main__':
 app.run()
 #app.debug = True
 #app.run()
 #app.run(debug = True)