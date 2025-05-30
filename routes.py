from flask import Flask, app, render_template, redirect, url_for, flash
from models import db, Usuario, Ponto
from datetime import datetime

def init_app(app):

@app.route('/')
def index():
    usuario = Usuario.query.first()
    return render_template('index.html', usuario=Usuario)

@app.route('/bater_ponto/<int:usuario_id>', methods=['POST'])
def bater_ponto(usuario_id):
     usuario = Usuario.query.get(usuario_id)
     if usuario:
          ponto = Ponto(usuario=usuario)
          db.session.add(ponto)
          db.session.commit()
     return redirect(url_for('index'))

@app.route('/pontos')
def lista_pontos():
     pontos = Ponto.query.order_by(Ponto.horario.desc()).all()
     return render_template('pontos.html', pontos=pontos)