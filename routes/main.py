from flask import Blueprint,render_template

bp_main=Blueprint('main',__name__,'/')

@bp_main.route('/')
def root():
    return render_template('home.1.html')