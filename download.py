from flask import Flask, render_template


# flask instance
app = Flask(__name__)

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