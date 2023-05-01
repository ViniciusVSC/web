from flask import Blueprint, render_template

login_bp = Blueprint('login', __name__,template_folder='./templates/')

@login_bp.route('/login')
def login():
    return render_template('login.html')

@login_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
