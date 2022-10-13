from urllib.request import urlopen

import pymongo
import gridfs
import requests

from EHAB import TMDBDownloader

class mongodb:

    def __init__(self):
        self.myclient = pymongo.MongoClient()
        self.db = self.myclient["movies"]
        self.col = self.db["posters"]
        self.tmdb_downloader = TMDBDownloader()
        self.fs = gridfs.GridFS(self.db)

    # used GridFS to insert data into colum
    def insert_data(self,name):
        self.name = name
        movie_id = self.tmdb_downloader.getposterURL(name)[1]
        f = self.tmdb_downloader.getposterURL(name)[0]
        print(f)
        h = requests.get(f, stream=True)
        # check if the poster exist by name
        if self.fs.exists({'my_id': movie_id}):
            print("already exist")
        else:
            print("adding poster: " + str(self.name))
            # if it doesn't exist then use put to insert into colum
            self.fs.put(h.raw , filename=self.name, my_id=movie_id, html=f)

    # check if the poster exist before attempting delete
    def del_data(self, name):
        col = self.db["fs.files"]
        a = col.find()
        print(a)
        for x in a:
            if x['filename'] == name:
                print("deleting " + str(x.get('filename')))
                col.delete_one(x)
            else:
                print("not found")

    def update_data(self):
        pass

    # read data from fs.file colum
    def read_data(self):
        col = self.db["fs.files"]
        x = col.find({})
        for document in x:
            print("poster: " + str(document['filename']))

    def read_movie_name(self,name):
        # check if the poster exist by name
        if self.fs.exists({'filename': name}):
            f = self.tmdb_downloader.getposterURL(name)[1]
            #print(f)
            return f
        else:
            # if it doesn't exist then print to the user
            print("poster doesnt exist")

