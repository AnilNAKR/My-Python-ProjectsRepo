from flask import Flask, render_template
import requests
from posts import Posts

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


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for blog_post in my_posts:
        if blog_post.idy == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
