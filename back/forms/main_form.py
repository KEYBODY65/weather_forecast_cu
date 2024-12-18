from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LocationForm(FlaskForm):
    location_A = StringField('Введите название отправной точки:', validators=[DataRequired()])     # Поле для ввода названия отправной точки
    location_B = StringField('Введите название конечной точки:', validators=[DataRequired()])     # Поле для ввода названия конечной точки
    submit = SubmitField('Получить данные о погоде')     # Кнопка для отправки формы
