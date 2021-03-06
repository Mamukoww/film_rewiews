from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, BooleanField, SubmitField, RadioField
from wtforms.validators import Email, DataRequired, EqualTo
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


class RegisterForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    first_name = StringField(label='Имя', validators=[DataRequired()])
    last_name = StringField(label='Фамилия', validators=[DataRequired()])
    password = StringField(label='Пароль', widget=PasswordInput(), validators=[DataRequired()])
    confirmation = StringField(label='Подтверждение пароля', widget=PasswordInput(),
                               validators=[DataRequired(), EqualTo('password')])


class ReviewForm(FlaskForm):
    rating = RadioField(label='Оценка', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], validators=[DataRequired()])
    body = StringField(label='Комментарий', widget=TextArea(), validators=[DataRequired()])