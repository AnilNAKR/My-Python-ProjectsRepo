# URL Building and Templating with jinja in your flask application

from flask import Flask, render_template
import requests
import random
import datetime

age_endpoint = "https://api.agify.io/"
country_code_endpoint = "https://api.nationalize.io/"
gender_endpoint = "https://api.genderize.io/"
country_endpoint = "https://api.first.org/data/v1/countries/"

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=random_number, year=current_year)


@app.route('/guess/<name>')
def guess(name):
    name_parameters = {"name": name}

    age_response = requests.get(url=age_endpoint, params=name_parameters)
    age = age_response.json()
    person_name = age.get('name')
    person_age = age.get('age')

    country_code_response = requests.get(url=country_code_endpoint, params=name_parameters)
    country_code_data = country_code_response.json()
    country_code = country_code_data['country'][0].get('country_id')

    country_name_response = requests.get(url=country_endpoint)
    country_name_data = country_name_response.json()
    person_country = country_name_data['data'][country_code]['country']

    gender_response = requests.get(url=gender_endpoint, params=name_parameters)
    gender = gender_response.json()
    person_gender = gender.get('gender')

    return render_template("person_guess.html",
                           age=person_age, country=person_country, gender=person_gender,
                           name=person_name.title())


@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/2d2020861891e7e22be0"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
