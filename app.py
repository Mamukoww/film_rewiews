from forms import FilmForm
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, abort
from films import find_by_name
from models import db, User, Film, Review
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config.update(dict(
    SECRET_KEY="aaa",
    WTF_CSRF_SECRET_KEY="aaaaa"
))
db.init_app(app)
migrate = Migrate(app, db)
Bootstrap(app)


@app.route('/')
def homepage():
    return render_template('index.html', title="FilmReviews")


@app.route('/films')
def all_films():
    filmss = Film.query.all()
    return render_template('allfilms.html', title="FilmReviews", films=filmss)


@app.route("/films/<int:film_id>")
def get_film(film_id):
    film = Film.query.filter_by(id=film_id).first_or_404()
    return render_template("film.html", film=film)


@app.route("/search")
def search():
    name = request.args.get("name", "")
    filmss = Film.query.filter(Film.title.like(f'%{name}%')).all()
    return render_template('allfilms.html', title="FilmReviews", films=filmss)


@app.route('/films/new', methods=['GET', 'POST'])
def create_film():
    film_form = FilmForm()
    if request.method == 'POST' and film_form.validate():
        title = film_form.title.data
        desc = film_form.desc.data
        poster = film_form.poster.data
        release_date = film_form.release_date.data
        new = film_form.new.data
        film = Film(title=title,
                    desc=desc,
                    poster=poster,
                    release_date=release_date,
                    new=new)
        db.session.add(film)
        db.session.commit()
        return render_template('film.html', film=film)
    return render_template('new_film.html', form=film_form)


@app.errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404


if __name__ == '__main__':
    app.run()
