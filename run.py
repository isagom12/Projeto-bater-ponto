from flask import Flask
from models import db, Usuario  # importa Usuario também
import routes
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)

# Configuração do banco de dados (exemplo com SQLite)
app.config['SECRET_KEY'] = 'chave-secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # inicializa o banco de dados com o app
CSRFProtect(app)

# LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

routes.init_app(app)  # Só precisa chamar uma vez

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # cria as tabelas do banco de dados
        # Cria usuário padrão se não existir
        if not Usuario.query.filter_by(nome='admin').first():
            user = Usuario(nome='admin')
            user.set_senha('admin123')
            db.session.add(user)
            db.session.commit()
    app.run(debug=True)