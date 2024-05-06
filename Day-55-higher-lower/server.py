from flask import Flask
import random

random_number = random.randint(0, 9)

app = Flask(__name__)


@app.route('/')
def home():
    global random_number
    random_number = random.randint(0, 9)
    return ("<h1> Guess a number between 0 and 9 </h1>"
            "<img src='https://i.giphy.com/fDUOY00YvlhvtvJIVm.webp' width=450>")


@app.route('/<int:g_number>')
def guess_number(g_number):
    if g_number < random_number:
        return ("<h1 style='color:red'> Number Too Low, Try Again! </h1>"
                "<img src='https://i.giphy.com/mmYQJFwcnZV5v6BDsj.webp' width=450>")
    elif g_number > random_number:
        return ("<h1 style='color:blue'> Number Too High, Try Again! </h1>"
                "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExeTBteTZydmxoNDJsY2o0eHM1c2xpMTJnZWVpNDV4OXBxcm5sNGprNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qiw4VaWbXYDQqK6mgm/giphy.gif' width=450>")
    else:
        return ("<h1 style='color:#16a800'> You guessed right! </h1>"
                "<img src='https://i.giphy.com/d31wuLJDCbQYersY.webp' width=450>")


if __name__ == "__main__":
    app.run(debug=True)
