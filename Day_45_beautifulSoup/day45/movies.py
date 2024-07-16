from bs4 import BeautifulSoup
import requests

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, 'html.parser')

movies = soup.find_all(name='h3', class_='title')
titles = [(movie.getText()[movie.getText().index(' ')+1:]) for movie in movies]

with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f"{movie}\n")

