from flask import Blueprint,render_template

bp_ciencias_medicas_salud=Blueprint('ciencias_medicas_salud',__name__,url_prefix='/ciencias_medicas_salud')

@bp_ciencias_medicas_salud.route('/')
def root():
    return render_template('fields/ciencias_medicas_salud.html')