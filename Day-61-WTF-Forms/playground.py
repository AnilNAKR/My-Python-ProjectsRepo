from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), validators.Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), validators.Length(min=8)])
    submit = SubmitField(label='Log In')

app = Flask(__name__)
app.secret_key = "qazwsxedcrfvtgbyhnujm9876"

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # Process form data if it's valid
        # You can access form fields using login_form.email.data, login_form.password.data, etc.
        return "Form submitted successfully!"
    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    app.run(debug=True)
