from flask import Flask
from flask_mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ganamika898@gmail.com'
app.config['MAIL_PASSWORD'] = 'parulgupta'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'ganamika898@gmail.com', recipients = ['vipin@ferryipl.com','rajni@ferryipl.com'])
   msg.body = "Hello   How are You  sent By Anamika Gupta Using Flask"
   mail.send(msg)
   return "Sent Sucessfully"

if __name__ == '__main__':
   app.run(debug = True)