from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import json
from pprint import pprint

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

tmdb_api_key = '32da256d807acf02fc35f42331cb02d6'
tmdb_read_access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMmRhMjU2ZDgwN2FjZjAyZmMzNWY0MjMzMWNiMDJkNiIsIm5iZiI6MTczMzE4NzE1OS4wMjEsInN1YiI6IjY3NGU1NjU3Nzk5YmMwNDcyZGVlOWFkMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.6sJ94306aRztbMtSBv3eXY76k9dVn_e_cRsE9Rezlao'
def query_movie(movie_title):
    url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
    results = requests.get(url, params={"api_key": tmdb_api_key, "query": movie_title}).json()['results']
    return results

# CREATE FORMS
class RateMovieForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    done = SubmitField(label='Done')

class AddMovieForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField(label='Done')

# CREATE DB
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'year': self.year,
            'description': self.description,
            'rating': self.rating,
            'ranking': self.ranking,
            'review': self.review,
            'img_url': self.img_url
        }



with app.app_context():
    db.create_all()

@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(Movie.rating))
        all_films = result.scalars()
        films = []
        for film in all_films:
            films.append(film.to_dict())

    return render_template("index.html", movies=films)

@app.route('/add', methods=['GET','POST'])
def add():
    add_movie_form = AddMovieForm()
    if request.method == 'POST':
        movie_title = str(add_movie_form.title.data).title()
        query = query_movie(movie_title)
        return render_template('select.html', query=query)

    return render_template('add.html', form=add_movie_form)

@app.route('/choose_film', methods=['GET','POST'])
def choose_film():
    movie_id = request.args.get("film_id")
    if movie_id:
        movie_api_url = f"{'https://api.themoviedb.org/3/movie'}/{movie_id}"
        # The language parameter is optional, if you were making the website for a different audience
        # e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": tmdb_api_key, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{'https://image.tmdb.org/t/p/w500'}{data['poster_path']}",
            description=data["overview"],
            rating=7.5,
            review='',
            ranking=10
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", mid=new_movie.id))

@app.route('/edit/<mid>', methods=['GET','POST'])
def edit(mid):
    rate_movie_form = RateMovieForm()
    if request.method == 'POST':
        movie_to_update = db.get_or_404(Movie, mid)
        movie_to_update.rating = float(rate_movie_form.rating.data)
        movie_to_update.review = rate_movie_form.review.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('edit.html', mid=mid, form=rate_movie_form)
@app.route('/delete/<mid>')
def delete(mid):
    movie_to_delete = db.get_or_404(Movie, mid)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
