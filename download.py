from flask import Flask, render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# flask instance
app = Flask(__name__)

#secret key
app.config['SECRET_KEY'] = 'my keys.com'

#class form
class Nameform(FlaskForm):
	name = StringField("Enter your name", validators=[DataRequired()])
	submit = SubmitField("submit")


#route decorator
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'),500

@app.route('/')
def index():
	name = '<strong>Kyle</strong>'
	return render_template('index.html',name=name)

#route decorator
@app.route('/user/<name>')

def user(name):
	return render_template('user.html', username=name)

@app.route('/name', methods=['GET','POST'])

def username():
	name= None
	form = Nameform()
	if form.validate_on_submit():
		name = form.name.data
		flash('Your form submited sucessfully')
	return render_template('form.html',name=name,
		form=form)





























