from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)  # nome é único
    senha_hash = db.Column(db.String(128), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.now)  # Data de cadastro

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def checar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def get_id(self):
        return str(self.id)

class Ponto(db.Model):
    __tablename__ = 'ponto'

    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.DateTime, default=datetime.now)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', backref='pontos')

    def __repr__(self):
        return f"<Ponto {self.usuario.nome} - {self.horario}>"