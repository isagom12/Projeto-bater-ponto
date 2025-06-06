from flask import render_template, redirect, url_for, request, flash
from models import db, Usuario, Ponto
from forms import FormPonto, FormCadastro

def init_app(app):

    @app.route('/', methods=['GET', 'POST'])
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
    def pontos():
        pontos = Ponto.query.order_by(Ponto.horario.desc()).all()
        return render_template('pontos.html', pontos=pontos)
    
    
    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        form = FormCadastro()
        if form.validate_on_submit():
            nome = form.nome.data.strip()
            email = form.email.data.strip()
            senha = form.senha.data

            if Usuario.query.filter_by(email=email).first():
                flash('Email já cadastrado.', 'danger')
                return redirect(url_for('cadastro'))

            novo_usuario = Usuario(nome=nome, email=email)
            novo_usuario.set_senha(senha)
            db.session.add(novo_usuario)
            db.session.commit()

            flash('Cadastro realizado com sucesso! Agora registre o ponto.', 'success')
            return redirect(url_for('index'))

        return render_template('cadastro.html', form=form)
