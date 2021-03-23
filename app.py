from flask import Flask, render_template, request
from films import films, find_by_name

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title="FilmReviews", films=films)


@app.route("/films/<int:film_id>")
def get_film(film_id):
    return render_template("film.html", film=films[film_id])


@app.route("/search")
def search():
    name = request.args.get("name", "")
    return render_template('index.html', title="FilmReviews", films=find_by_name(name))


if __name__ == '__main__':
    app.run()
