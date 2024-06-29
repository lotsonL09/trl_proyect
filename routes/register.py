from flask import Blueprint,render_template,request
from aditional_data.db import engine

bp_register=Blueprint('register',__name__,url_prefix='/register')

@bp_register.route("/")
def root():
    return render_template("formulario.html")

@bp_register.route('/register_participant',methods=['POST'])
def register_participant():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    company=request.form['company']
    job=request.form['job']
    print(first_name)
    print(last_name)
    print(company)
    print(job)
    return 'Formulario hecho'