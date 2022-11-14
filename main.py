from EHAB import TMDBDownloader
from mongodb import mongodb
import webbrowser
import app
import app
def main():

    a = TMDBDownloader()
    #a.get_id()
    #a.getURL()
    a.getposterURL("Avatar")
    #a.download_image(a.getname())
    #print("h= " +str(h))
    movie_name = "Avatar"
    #mdb = mongodb()
    #mdb.insert_data(movie_name)
    #mdb.read_data()
    #mdb.del_data("hitman")
    #webbrowser.open(a)
    #mdb.read_movie_name("Avatar")

if __name__ == '__main__':
    main()
