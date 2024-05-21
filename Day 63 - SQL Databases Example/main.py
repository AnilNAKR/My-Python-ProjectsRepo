# import sqlite3
#
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(4, 'Harry Potter and the Goblet of Fire', 'J. K. Rowling', '7')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, Float

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
# Initialize the app with the extension
db.init_app(app)


# Create the table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"Book <{self.title}>"


# Create table schema in the database. Requires application context
with app.app_context():
    db.create_all()

# Create database record
with app.app_context():
    newbook = Book(title="Harry Potter & the Order of the phoenix", author="J.K.Rowling", rating=8.5)
    db.session.add(newbook)
    db.session.commit()

# Querying the data
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    for b in all_books:
        print(b)

# Updating the data
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter & the chamber of secrets")).scalar()
    book_to_update.title = "Harry Potter & the half blood prince"
    db.session.commit()


# update a record by Primary Key
book_id = 1
with app.app_context():
    # book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter & the Philosopher's stone"
    db.session.commit()


# Deleting a book data row
book_id = 1
with app.app_context():
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
