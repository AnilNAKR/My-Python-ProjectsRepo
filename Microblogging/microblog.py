# from flask import Flask, render_template
# from config import Config
from app import app

#
# app = Flask(__name__)
# app.config.from_object(Config)
#
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Miguel'}
#     posts = [
#         {
#             'author': {'username': 'John'},
#             'body': 'Beautiful day in Portland!'
#         },
#         {
#             'author': {'username': 'Susan'},
#             'body': 'The Avengers movie was so cool!'
#         }
#     ]
#     return render_template("index.html", title="Home", user=user, posts=posts)
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
