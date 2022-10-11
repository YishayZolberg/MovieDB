import os, requests
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv('API_KEY')
#api_url=os.getenv('URL')

user=input("Please enter some movie to search: ")
search_url=f'https://api.themoviedb.org/3/search/movie?query={user}&api_key={api_key}'
jpg_path=''
image_base_url=f'https://image.tmdb.org/t/p/w1280{jpg_path}'
blabla=requests.get(search_url).json()
jpg_path=blabla.get('results')[0]['backdrop_path']
print(image_base_url,jpg_path, sep='')




# url = api_url.format(key=api_key)
# res = requests.get(url)
# config = res.json()

