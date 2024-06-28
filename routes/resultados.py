from flask import Blueprint,render_template

bp_resultados=Blueprint('resultados',__name__,url_prefix='/resultados')

@bp_resultados.route('/')
def root():
    return render_template('fields/resultados.1.html')