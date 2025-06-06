from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class FormPonto(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tipo = SelectField('Tipo de Ponto', choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    submit = SubmitField('Registrar Ponto')

class CadastroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')