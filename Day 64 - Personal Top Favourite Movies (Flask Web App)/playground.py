import requests

url = "https://api.themoviedb.org/3/movie/51876?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMGMxZTAxZTkwYTA3MjQxMjRlNGM1YTE2ZTllNmRkYyIsInN1YiI6IjY2MzI1YmJhZDE4NTcyMDEyYjMzY2Q3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.m3T12CGmOYOG5Z_91ZmmnekUzleLuvIYkXcqOKcbm2w"
}

response = requests.get(url, headers=headers)

data = response.json()['vote_average']
print(round(float(data), 1))