import pymongo
import gridfs


class mongodb:

    def __init__(self, db_name, col_name, name):
        self.myclient = pymongo.MongoClient()
        self.db = self.myclient[db_name]
        self.col = self.db[col_name]
        self.name = name
        self.fs = gridfs.GridFS(self.db)

    # used GridFS to insert data into colum
    def insert_data(self, name):
        # Open the image in read-only format.
        with open(name, 'rb') as f:
            contents = f.read()
        # check if the poster exist bt name
        if self.fs.exists({'filename': name}):
            print("already exist")
        else:
            print("adding poster: " + str(self.name))
            # if it doesn't exist then use put to insert into colum
            self.fs.put(contents, filename=self.name)
        return self.fs, contents

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

