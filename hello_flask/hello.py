from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('<h1 style="text-align:center"> Hello World! </h1>'
            '<p style="text-align:center"> My name is Anil </p>'
            '<img src="https://media1.tenor.com/m/MFt1WVDeUhUAAAAd/smol-illegally-smol-cat.gif" align="center">')


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


@app.route('/username/<name>')
def greet(name):
    return f"Hello {name}!"


#  Creating variable paths and converting the path to a specified data type
@app.route('/talk/<name>/<int:number>')
def talk(name, number):
    return f"Hello, I am {name} & I am currently ranked no.{number} in the list!"


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Anil")
new_user.is_logged_in = True
create_blog_post(new_user)

if __name__ == "__main__":
    app.run(debug=True)
