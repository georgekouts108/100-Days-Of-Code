from flask import Flask, render_template
from forms import LoginForm
from flask_bootstrap import Bootstrap5
import os

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
app.secret_key = os.environ['SECRET_KEY']
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    my_login_form = LoginForm()
    if my_login_form.validate_on_submit():
        email = my_login_form.email.data
        pwd = my_login_form.password.data
        _success = email == 'admin@email.com' and pwd == '12345678'
        return render_template(('success.html' if _success else 'denied.html'))

    return render_template('login.html', login_form=my_login_form)


if __name__ == '__main__':
    app.run(debug=True)
