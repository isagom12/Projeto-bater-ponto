from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class FormPonto(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tipo = SelectField('Tipo de Ponto', choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    submit = SubmitField('Registrar Ponto')