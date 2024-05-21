from flask import Flask, render_template
import requests

age_endpoint = "https://api.agify.io/"
country_code_endpoint = "https://api.nationalize.io/"
gender_endpoint = "https://api.genderize.io/"
country_endpoint = "https://api.first.org/data/v1/countries/"

parameters = {
    "name": input("Enter Name: ")
}

country_code_response = requests.get(url=country_code_endpoint, params=parameters)
country_code_data = country_code_response.json()
country_code = country_code_data['country'][0].get('country_id')

country_name_response = requests.get(url=country_endpoint)
country_name_data = country_name_response.json()
person_country = country_name_data['data'][country_code]['country']

print(person_country)
