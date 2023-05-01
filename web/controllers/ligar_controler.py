from flask import Blueprint, render_template

ligar_bp = Blueprint('ligar', __name__,template_folder='./templates/')

@ligar_bp.route('/ligar')
def ligar():
    return render_template('ligar.html')
