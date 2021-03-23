from flask import Flask, render_template
from films import films


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html', title="FilmReviews", films=films)

@app.route("/films/<int:film_id>")
def get_film(film_id):
    return render_template("film.html", film=films[film_id])


if __name__ == '__main__':
    app.run()
