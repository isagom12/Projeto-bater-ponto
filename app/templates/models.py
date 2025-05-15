from app import db
from datetime import datetime

class RegistroPonto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    horario = db.Column(db.DateTime, default=datetime.utcnow)
    tipo = db.Column(db.String(10), nullable=False)  # 'entrada' ou 'saida'

    def __repr__(self):
        return f"{self.nome} - {self.tipo} - {self.horario}"

