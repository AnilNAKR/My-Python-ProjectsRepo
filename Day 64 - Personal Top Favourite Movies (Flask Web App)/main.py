from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from sqlalchemy.sql.expression import desc

MOVIESDB_API_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
MOVIES_DETAILS_ENDPOINT = "https://api.themoviedb.org/3/movie/51876"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMGMxZTAxZTkwYTA3MjQxMjRlNGM1YTE2ZTllNmRkYyIsInN1YiI6IjY2MzI1YmJhZDE4NTcyMDEyYjMzY2Q3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.m3T12CGmOYOG5Z_91ZmmnekUzleLuvIYkXcqOKcbm2w"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///movies.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    year: Mapped[int] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, unique=True, nullable=True)
    review: Mapped[str] = mapped_column(String(300), nullable=True)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake,
#     Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles
#     they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     image_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
#
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()


class AddMovie(FlaskForm):
    title = StringField('Movie title', validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditMovieReview(FlaskForm):
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    # result = db.session.execute(db.select(Movie).order_by(Movie.rating)).scalars().all()
    result = db.session.execute(db.select(Movie).order_by(desc(Movie.rating))).scalars().all()

    for i in range(len(result)):
        result[i].ranking = i + 1
    db.session.commit()

    return render_template("index.html", movies=result)


@app.route('/add', methods=["POST", "GET"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        movie_title = form.title.data
        parameters = {
            "query": movie_title,
        }
        response = requests.get(url=MOVIESDB_API_ENDPOINT, params=parameters, headers=headers)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route('/edit', methods=["POST", "GET"])
def edit():
    form = EditMovieReview()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)


@app.route('/delete')
def delete():
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_selected)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        headers1 = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMGMxZTAxZTkwYTA3MjQxMjRlNGM1YTE2ZTllNmRkYyIsInN1YiI6IjY2MzI1YmJhZDE4NTcyMDEyYjMzY2Q3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.m3T12CGmOYOG5Z_91ZmmnekUzleLuvIYkXcqOKcbm2w"
        }
        response1 = requests.get(url=api_url, headers=headers1, params={"language": "en-US"})
        data = response1.json()
        new_movie = Movie(
            title=data['title'],
            year=int(data["release_date"].split("-")[0]),
            description=data['overview'],
            image_url=f'https://image.tmdb.org/t/p/w500{data["poster_path"]}',
            rating=round(float(data['vote_average']), 1),
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
