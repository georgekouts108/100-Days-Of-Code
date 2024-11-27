from flask import Flask, render_template, request
import requests
import smtplib
import os

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
    return render_template('contact.html', header='Contact Me')

@app.route('/contact-form-handle', methods=['POST'])
def contact_form_handle():

    _name = request.form['name']
    _email = request.form['email']
    _phone = request.form['phone']
    _message = request.form['message']

    _body = f"_name = {_name}\n_email = {_email}\n_phone={_phone}\n_msg = {_message}"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=_email, password=os.environ['GMAIL_SENDER_PWD'])
    connection.sendmail(
        from_addr=_email,
        to_addrs='georgekoutsaris1@yahoo.com',
        msg=f"Subject:'New Message'\n\n{_body}"
    )
    connection.close()

    return render_template('contact.html', header='Successfully sent message')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
