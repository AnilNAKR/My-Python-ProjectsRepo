from flask import Flask, render_template, request
import requests
from posts import Posts
import smtplib
import os

my_email = os.environ.get('MAIL_ID')
my_passkey = os.environ.get('MAIL_PASSKEY')

blog_posts_endpoint = "https://api.npoint.io/674f5423f73deab1e9a7"

blog_posts = requests.get(url=blog_posts_endpoint).json()
my_posts = []
for post in blog_posts:
    post_obj = Posts(post['id'], post['body'], post['title'], post['subtitle'], post['image_url'])
    my_posts.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html", all_posts=my_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        data = request.form
        name = data['name']
        email = data['email']
        phone = data['phone']
        message = data['message']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_passkey)
            connection.sendmail(from_addr=my_email,
                                to_addrs="anilnakr7@gmail.com",
                                msg=f"Subject: Customer Review\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n"
                                    f"Message: {message}")
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for blog_post in my_posts:
        if blog_post.idy == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
