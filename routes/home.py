from flask import Blueprint,render_template

bp_home=Blueprint('main',__name__,'/')

@bp_home.route('/')
def root():
    return render_template('home.1.html')

@bp_home.route('/trl_fields/')
def get_fields():
    return render_template('/fields/trl_fields.html')
