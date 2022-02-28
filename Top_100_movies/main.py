import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies = response.text

soup = BeautifulSoup(movies, "html.parser")


movie_list = []

name = soup.find_all(name="h3", class_="title")

for item in name:
    text = item.getText()
    movie_list.append(text)

asscending = movie_list[::-1]
print(asscending)

file = open("best_movies.txt", "w")
for element in asscending:
    file.write(element + "\n")
file.close()






