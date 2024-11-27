from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    _posts = requests.get(url='https://api.npoint.io/4512202a6dd743464813').json()
    return render_template('index.html', posts=_posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    _posts = requests.get(url='https://api.npoint.io/4512202a6dd743464813').json()
    target_post = None
    for p in _posts:
        if p['id'] == post_id:
            target_post = p
            break
    return render_template('post.html', post=target_post)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
