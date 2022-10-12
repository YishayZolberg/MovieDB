import os, requests, pymongo
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv('API_KEY')
client = pymongo.MongoClient("mongodb+srv://yishayzolberg:O4Mkld5Pe4KJFSF9@cluster0.rdxvksb.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
user=input("Please enter some movie to search: ")
search_url=f'https://api.themoviedb.org/3/search/movie?query={user}&api_key={api_key}'
jpg_path=''
image_base_url=f'https://image.tmdb.org/t/p/original{jpg_path}'
blabla=requests.get(search_url).json()
jpg_path=blabla.get('results')[0]['backdrop_path']
print(image_base_url,jpg_path, sep='')




# url = api_url.format(key=api_key)
# res = requests.get(url)
# config = res.json()

