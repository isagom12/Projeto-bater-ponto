from flask import Flask
from models import db  # importa o objeto db do models.py
import routes  # importa o arquivo routes.py

app = Flask(__name__)

# Configuração do banco de dados (exemplo com SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # inicializa o banco de dados com o app

# Registra as rotas do routes.py
routes.init_app(app)  # Certifique-se de ter uma função init_app(app) em routes.py

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # cria as tabelas do banco de dados
    app.run(debug=True)