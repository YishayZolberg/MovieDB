from EHAB import TMDBDownloader
from mongodb import mongodb


def main():
    a = TMDBDownloader()
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


if __name__ == '__main__':
    main()
