from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],'/img'))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)