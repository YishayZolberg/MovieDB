from EHAB import TMDBDownloader
from mongodb import mongodb
import webbrowser

def main():
    #a = TMDBDownloader()
    #a.getURL()
    #a.getposterURL()
    #a.download_image(a.getname())
    #print("h= " +str(h))
    #movie_name = a.getname() + ".jpg"
    db_name = "movies"
    col_name = "posters"
    mdb = mongodb(db_name, col_name)
    #mdb.insert_data()
    mdb.read_data()
    #mdb.del_data(movie_name)
    a =mdb.read_movie_name()
    webbrowser.open(a)

if __name__ == '__main__':
    main()
