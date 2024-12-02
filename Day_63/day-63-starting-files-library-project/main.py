from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import uuid
import json

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


def get_uuid():
    return str(uuid.uuid4())


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def to_string(self):
        return f"{self.title} - {self.author} - {self.rating}/10"

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'author': self.author, 'rating': self.rating}


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()
        _books = []
        for book in all_books:
            _books.append(book.to_dict())

    return render_template('index.html', books=_books)

@app.route('/delete_book/<book_dict>')
def delete_book(book_dict):
    book_dict = book_dict.replace("\'", "\"")
    book_dict = json.loads(book_dict)
    book_to_delete = db.get_or_404(Book, book_dict['id'])
    db.session.delete(book_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/edit_rating/<book_dict>', methods=['GET','POST'])
def edit_rating(book_dict):
    book_dict = book_dict.replace("\'", "\"")
    book_dict = json.loads(book_dict)

    if request.method == 'POST':
        book_to_update = db.get_or_404(Book, book_dict['id'])
        book_to_update.rating = request.form['new_rating']
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit_rating.html', book_dict=book_dict)

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        _title = request.form['book_name'].title()
        _author = request.form['book_author'].title()
        _rating = request.form['book_rating']

        with app.app_context():
            _new_book = Book(id=get_uuid(), title=_title, author=_author, rating=_rating)
            db.session.add(_new_book)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
