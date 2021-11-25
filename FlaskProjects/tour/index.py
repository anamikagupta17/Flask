from flask import Flask, render_template, request, url_for


app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/hotels')
def hotels():
    return render_template('hotels.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/hotelroom')
def hotelroom():
    return render_template('hotel-room.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/tourplace')
def tourplace():
    return render_template('tour-place.html')

@app.route('/tour')
def tour():
    return render_template('tours.html')

if __name__ == '__main__':
    app.run(debug = True)