from flask import Flask, render_template
import requests
from post import Post

blog_data_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"

posts_response = requests.get(url=blog_data_endpoint).json()
post_objects = []
for post in posts_response:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.idy == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
