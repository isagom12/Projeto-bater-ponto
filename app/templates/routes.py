from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms import FormPonto
from app.models import RegistroPonto

@app.route('/', methods=['GET', 'POST'])
def index():
    form = FormPonto()
    if form.validate_on_submit():
        registro = RegistroPonto(nome=form.nome.data, tipo=form.tipo.data)
        db.session.add(registro)
        db.session.commit()
        flash('Ponto registrado com sucesso!', 'success')
        return redirect(url_for('index'))
    
    registros = RegistroPonto.query.order_by(RegistroPonto.horario.desc()).all()
    return render_template('index.html', form=form, registros=registros)