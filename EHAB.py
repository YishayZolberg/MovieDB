import requests
import os
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('API_KEY')
api_token=os.getenv('ACCESS_TOKEN')
api_url=os.getenv('URL')
print(api_key)
CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
#KEY = api_key

url = CONFIG_PATTERN.format(key=api_key)
r = requests.get(url)
config = r.json()

IMG_PATTERN = 'http://api.themoviedb.org/3/movie/{imdbid}/images?api_key={key}'
r = requests.get(IMG_PATTERN.format(key=api_key,imdbid='tt0095016'))
api_response = r.json()
print(api_response)

api1 = 'https://api.themoviedb.org/3/movie/157336?api_key=api_key&append_to_response=images'
print(api1)