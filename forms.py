from flask_wtf import FlaskForm
from wtforms import \
    StringField, \
    DateTimeField, \
    BooleanField, \
    SubmitField

from wtforms.widgets import TextArea


class FilmForm(FlaskForm):
    title = StringField('Название')
    desc = StringField('Описание', widget=TextArea())
    poster = StringField('Ссылка на изображение')
    release_date = DateTimeField('Дата выхода')
    new = BooleanField('Новинка')
    submit_button = SubmitField('Сохранить')
