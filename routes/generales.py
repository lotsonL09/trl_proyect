from flask import Blueprint,render_template

bp_general=Blueprint('generales',__name__,url_prefix='/generales')

@bp_general.route('/')
def root():
    return render_template('fields/generales.1.html')