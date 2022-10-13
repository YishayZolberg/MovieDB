from flask import Flask, request, render_template
from EHAB import TMDBDownloader as TMDB
from mongodb import mongodb
from dotenv import load_dotenv
import os

def main():
    a = TMDB()
    a.getURL()
    a.getposterURL()
    a.download_image(a.getname())
    movie_name = a.getname() + ".jpg"
    db_name = "movies"
    col_name = "posters"
    mdb = mongodb(db_name, col_name, movie_name)
    mdb.insert_data(movie_name)
    mdb.read_data()
    #mdb.del_data(movie_name)


app = Flask(__name__)
@app.route("/")
def home_page():
    return "<p>Hello, World!</p>"

@app.route('/search', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        movie_name = request.form['name']
        imdb_id, file_name=TMDB.search_and_download(movie_name)
        mongodb.insert_data(os.getenv('URL') + file_name,movie_name,imdb_id)
        binary_file = mongodb.read_data(movie_name)
        image_url="https://image.tmdb.org/t/p/w1280"
        #image = b64encode(binary_file).decode("utf-8")
        src = "data:image/gif;base64," + image_url
        return f'<img src={src}>'
    return render_template('new_form.html')
