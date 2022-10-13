import requests
import os

from dotenv import load_dotenv

load_dotenv()


class TMDBDownloader:

    def __init__(self):
        self.name = "saving private ryan"
        self.api_key = os.getenv('API_KEY')
        self.api_token = os.getenv('ACCESS_TOKEN')
        self.api_url = os.getenv('URL')
        self.CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
        self.file_name = self.name
        search_url = f'https://api.themoviedb.org/3/search/movie?query={self.name}&api_key={self.api_key}'
        self.request = requests.get(search_url)

    def getname(self):
        jpg_path1 = self.request.json()
        j = jpg_path1.get('results')[0].get('original_title')
        print(j)
        return j

    def getURL(self):
        url = self.CONFIG_PATTERN.format(key=self.api_key)
        r = requests.get(url)
        IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
        r = requests.get(IMG_PATTERN.format(key=self.api_key, imdbid='tt0095016'))
        api_response = r.json()
        #print(api_response)
        return api_response

    def getposterURL(self):
        jpg_path = ''
        image_base_url = f'https://image.tmdb.org/t/p/w1280{jpg_path}'
        request = self.request
        jpg_path = request.json()
        j = jpg_path.get('results')[0].get('backdrop_path')
        a = (image_base_url + j)
        #print(a)
        return a

    def download_image(self, name):
        response = requests.get(self.getposterURL())
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
