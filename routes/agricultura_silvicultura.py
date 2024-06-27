from flask import Blueprint,render_template

bp_agricultura_silvicultura=Blueprint('agricultura_silvicultura',__name__,'/agricultura_silvicultura')

@bp_agricultura_silvicultura.route('/')
def root():
    return render_template('fields/agricultura_silvicultura.html')