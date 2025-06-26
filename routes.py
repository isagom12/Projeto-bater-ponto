from flask import render_template, redirect, url_for, request, flash
from models import db, Usuario, Ponto
from forms import FormPonto, FormCadastro, FormLogin
from flask_login import login_user, logout_user, login_required, current_user

def init_app(app):

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = FormLogin()
        if form.validate_on_submit():
            usuario = Usuario.query.filter_by(nome=form.nome.data.strip()).first()
            if usuario and usuario.checar_senha(form.senha.data):
                login_user(usuario)
                return redirect(url_for('index'))
            flash('Usuário ou senha inválidos.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/', methods=['GET', 'POST'])
    @login_required
    def index():
        form = FormPonto()
        if form.validate_on_submit():
            nome = form.nome.data.strip()
            tipo = form.tipo.data

            usuario = Usuario.query.filter_by(nome=nome).first()
            if not usuario:
                flash('Usuário não encontrado. Cadastre-se primeiro.', 'danger')
                return redirect(url_for('cadastro'))
            ponto = Ponto(usuario=usuario)
            db.session.add(ponto)
            db.session.commit()

            flash(f'Ponto de {tipo} registrado para {usuario.nome}!', 'success')
            return redirect(url_for('index'))

        return render_template('index.html', form=form)

    @app.route('/pontos')
    @login_required
    def pontos():
        pontos = Ponto.query.order_by(Ponto.horario.desc()).all()
        return render_template('pontos.html', pontos=pontos)
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        form = FormCadastro()
        if form.validate_on_submit():
            nome = form.nome.data.strip()
            senha = form.senha.data

            if Usuario.query.filter_by(nome=nome).first():
                flash('Nome de usuário já cadastrado.', 'danger')
                return redirect(url_for('cadastro'))

            novo_usuario = Usuario(nome=nome)
            novo_usuario.set_senha(senha)
            db.session.add(novo_usuario)
            db.session.commit()

            login_user(novo_usuario)  # login automático após cadastro
            flash('Cadastro realizado com sucesso! Agora registre o ponto.', 'success')
            return redirect(url_for('index'))

        return render_template('cadastro.html', form=form)

    @app.route('/relatorios')
    def relatorios():
     pontos = Ponto.query.order_by(Ponto.horario.desc()).all()
     return render_template('relatorios.html', pontos=pontos)