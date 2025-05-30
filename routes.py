from flask import render_template, redirect, url_for, request
from models import db, Usuario, Ponto
from datetime import datetime

def init_app(app):
    # Página inicial com botão para bater ponto
    @app.route('/')
    def index():
        usuario = Usuario.query.first()  # Aqui pode ajustar para múltiplos usuários (opcional)
        return render_template('index.html', usuario=usuario)

    # Rota para bater ponto (POST)
    @app.route('/bater_ponto/<int:usuario_id>', methods=['POST'])
    def bater_ponto(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            ponto = Ponto(usuario=usuario)
            db.session.add(ponto)
            db.session.commit()
        return redirect(url_for('index'))

    # Rota para listar todos os pontos registrados
    @app.route('/pontos')
    def lista_pontos():
        pontos = Ponto.query.order_by(Ponto.horario.desc()).all()
        return render_template('pontos.html', pontos=pontos)

    # Rota para cadastro de novos usuários
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            novo_usuario = Usuario(nome=nome, email=email, senha=senha)
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('cadastro.html')
