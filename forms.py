from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import Email, DataRequired
from wtforms.widgets import TextArea, PasswordInput


class FilmForm(FlaskForm):
    title = StringField('Название')
    desc = StringField('Описание', widget=TextArea())
    poster = StringField('Ссылка на изображение')
    release_date = DateTimeField('Дата выхода')
    new = BooleanField('Новинка')
    submit_button = SubmitField('Сохранить')


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = StringField(label='Пароль', widget=PasswordInput(), validators=[DataRequired()])
    remember_me = BooleanField(label='Запомнить меня')
