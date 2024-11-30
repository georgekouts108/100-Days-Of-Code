import os
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
bootstrap = Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe location on Google Maps (URL)',
                               validators=[DataRequired(), URL(message='must enter a valid URL')])
    open_time = StringField('Open Time (e.g. 8AM)', validators=[DataRequired()])
    close_time = StringField('Close Time (e.g. 9PM)', validators=[DataRequired()])

    coffee_rating = SelectField('Coffee Rating', choices=[('0', '✘')] + [(str(r), '☕' * r) for r in range(1, 6)],
                                validators=[DataRequired()])

    wifi_rating = SelectField('WiFi Rating', choices=[('0', '✘')] + [(str(r), '💪' * r) for r in range(1, 6)],
                              validators=[DataRequired()])

    power_rating = SelectField('Power Rating', choices=[('0', '✘')] + [(str(r), '🔌' * r) for r in range(1, 6)],
                               validators=[DataRequired()])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe = form.cafe.data
        location_url = form.location_url.data
        open_time = form.open_time.data
        close_time = form.close_time.data
        coffee_rating = form.coffee_rating.data
        wifi_rating = form.wifi_rating.data
        power_rating = form.power_rating.data

        new_row = [cafe, location_url, open_time, close_time, coffee_rating, wifi_rating, power_rating]
        with open('cafe-data.csv', 'a') as file:
            writer_object = csv.writer(file)
            writer_object.writerow(new_row)
            file.close()
        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
