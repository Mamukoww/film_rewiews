from flask import Flask, render_template, request, abort
from films import films, find_by_name
from flask_sqlalchemy import SQLAlchemy
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db.init_app(app)



@app.route('/')
def homepage():
    return render_template('index.html', title="FilmReviews", films=films)


@app.route("/films/<int:film_id>")
def get_film(film_id):
    if film_id not in films:
        abort(404)
    return render_template("film.html", film=films[film_id])


@app.route("/search")
def search():
    name = request.args.get("name", "")
    return render_template('index.html', title="FilmReviews", films=find_by_name(name))


@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404


if __name__ == '__main__':
    app.run()
