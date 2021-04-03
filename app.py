from forms import FilmForm, LoginForm, RegisterForm
from flask_bootstrap import Bootstrap
from models import db, User, Film, Review
from flask import Flask, render_template, request, abort, redirect, url_for
from flask_migrate import Migrate
import datetime
from flask_login import login_user, logout_user, LoginManager, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.secret_key = 'dSalGiK8IC9~fxz'
db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
Bootstrap(app)


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def homepage():
    return render_template('index.html', title="FilmReviews")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        remember_me = form.remember_me.data
        user = User.query.filter_by(email=email).first()
        if not user or not user.check_password(password):
            abort(401)
        login_user(user, remember=remember_me)
        return redirect(url_for('homepage'))
    return render_template('login.html', form=login_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            abort(400)
        first_name = form.first_name.data
        last_name = form.last_name.data
        user = User(email=email, first_name=first_name, last_name=last_name)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for('homepage'))
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homepage'))


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
@login_required
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
