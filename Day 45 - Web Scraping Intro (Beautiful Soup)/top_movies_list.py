from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")
rev_output = []
for movie in movie_titles:
    rev_output.append(movie.getText())

output = rev_output[::-1]

# print(output)

with open("top-movies-list.txt", 'w', encoding='utf-8') as file:
    for movie in output:
        file.write(movie+'\n')

