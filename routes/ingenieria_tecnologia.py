from flask import Blueprint,render_template

bp_ingenieria_tecnologia=Blueprint('ingenieria_tecnologia',__name__,url_prefix='/ingenieria_tecnologia')

@bp_ingenieria_tecnologia.route('/')
def root():
    return render_template('fields/ingenieria_tecnologia.1.html')