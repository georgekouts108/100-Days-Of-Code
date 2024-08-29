from flask import Flask, render_template
from datetime import datetime as dt
import requests

app = Flask(__name__)
NAME = 'George Koutsaris'
YEAR = dt.now().year

@app.route('/')
def home():
    blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    print(blogs)
    return render_template('index.html', blogs=blogs, name=NAME, current_year=YEAR)

@app.route('/guess/<name>')
def guess(name):
    genderize_results = requests.get(f'https://api.genderize.io?name={name}')
    gender = genderize_results.json()['gender']
    agify_results = requests.get(f'https://api.agify.io?name={name}')
    age = agify_results.json()['age']
    return render_template('guess.html', target_name=name,
                           gender=gender, age=age, name=NAME, current_year=YEAR)

@app.route('/blogs/<blog_id>')
def get_blog(blog_id):
    blogs = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    target_blog = [blog for blog in blogs if blog['id'] == int(blog_id)][0]

    return render_template('blog.html',
                           name=NAME, current_year=YEAR, blog=target_blog)


if __name__ == '__main__':
    app.run(debug=True)
