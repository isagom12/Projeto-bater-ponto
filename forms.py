from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class FormPonto(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    tipo = SelectField('Tipo de Ponto', choices=[('entrada', 'Entrada'), ('saida', 'Saída')])
    submit = SubmitField('Registrar Ponto')

class FormCadastro(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class FormLogin(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')