from flask import Flask, render_template, redirect, request,url_for
from flask_sqlalchemy import SQLAlchemy
from flask.helpers import flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.secret_key = 'delta'

class Shorten(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shortname = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String, nullable=False)

    def __init__(self, shortname, url):
        self.shortname = shortname
        self.url = url

@app.route('/', methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        shortName = request.form['name']
        Url = request.form['url']
        if shortName and Url :
            shorten = Shorten(shortname = shortName , url = Url)
            db.session.add(shorten)
            db.session.commit()
            flash('Successfully stored')
            return redirect('/')
        else:
            flash("Both are mandatory fields")
    return render_template('index.html')

@app.route('/shortUrl/<ShortName>')
def shorten(ShortName):
    shorten = Shorten.query.filter_by(shortname = ShortName).first()
    return redirect(shorten.url)

if __name__ == "__main__":
    app.run(debug=True)