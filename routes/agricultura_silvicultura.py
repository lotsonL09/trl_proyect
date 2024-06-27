from flask import Blueprint,render_template

bp_agricultura_silvicultura=Blueprint('agricultura_silvicultura',__name__,url_prefix='/agricultura_silvicultura')

@bp_agricultura_silvicultura.route('/')
def root():
    return render_template('fields/agricultura_silvicultura.1.html')