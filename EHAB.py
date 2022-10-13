import requests
import os
from dotenv import load_dotenv

load_dotenv()


class TMDBDownloader:

    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_token = os.getenv('ACCESS_TOKEN')
        self.api_url = os.getenv('URL')
        self.CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'




    def getURL(self):
        url = self.CONFIG_PATTERN.format(key=self.api_key)
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
        r = requests.get(IMG_PATTERN.format(key=self.api_key, imdbid='tt0095016'))
        api_response = r.json()
        return api_response


    def getposterURL(self,name):
        jpg_path = ''
        image_base_url = f'https://image.tmdb.org/t/p/w1280{jpg_path}'
        search_url = f'https://api.themoviedb.org/3/search/movie?query={name}&api_key={self.api_key}'
        request = requests.get(search_url)
        jpg_path = request.json()
        j = jpg_path.get('results')[0].get('backdrop_path')
        h = jpg_path.get('results')[0].get('id')
        a = (image_base_url + j)
        #print(a)
        return a,h

    def download_image(self,name):
        search_url = f'https://api.themoviedb.org/3/search/movie?query={name}&api_key={self.api_key}'
        response = requests.get(search_url)
        file = open(name, "wb")
        file.write(response.content)
        file.close()
        return response

    # api_key= os.getenv('API_KEY')
    # api_token= os.getenv('ACCESS_TOKEN')
    # api_url=os.getenv('URL')
    # CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
    # KEY = api_key

    # url = CONFIG_PATTERN.format(key=api_key)
    # r = requests.get(url)
    # config = r.json()

    # IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
    # r = requests.get(IMG_PATTERN.format(key=api_key,imdbid='tt0095016'))
    # api_response = r.json()
    # ----------------------------------------
    # api1 = 'https://api.themoviedb.org/3/movie/157336?api_key=api_key&append_to_response=images'

    # user="kingdom of heaven"#  input("Please enter some movie to search: ")
    # search_url=f'https://api.themoviedb.org/3/search/movie?query={user}&api_key={api_key}'
    # jpg_path=''
    # image_base_url=f'https://image.tmdb.org/t/p/w1280{jpg_path}'
    # blabla=requests.get(search_url)
    # jpg_path=blabla.json()
    # j =jpg_path.get('results')[0].get('backdrop_path')
    # print(image_base_url,j,sep="")

    # jpg_path.results[1].backdrop_path
