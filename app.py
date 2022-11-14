from flask import Flask, request, render_template
from mongodb import mongodb


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        movie_name = request.form['name']
        print(movie_name)
        x = mongodb()
        a = x.insert_data(movie_name)
        print(a)
    return render_template('new_form.html')

@app.route('/url', methods=['GET', 'POST'])  # GET REQUEST
def insert_item_html():
    if request.method == 'POST':
        movie_url = request.form['url']
        print(movie_url)
        x = mongodb()
        url = x.read_movie_name(movie_url)
        print(url)
    return render_template('form.html')

app.run()