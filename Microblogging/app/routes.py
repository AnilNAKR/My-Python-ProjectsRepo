from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import Loginform


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful Day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was cool'
        }
    ]
    return render_template("index.html", user=user, posts=posts, title='Home')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = Loginform()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", form=form, title="Sign In")
