from flask import Blueprint,render_template,request
from aditional_data.db import engine
from aditional_data.db import engine
from sqlalchemy import text

bp_register=Blueprint('register',__name__,url_prefix='/')

@bp_register.route("/")
def root():
    return render_template("datos.html")

@bp_register.route('/register_participant',methods=['POST'])
def register_participant():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    company=request.form['company']
    job=request.form['job']
    
    stmt=text("INSERT participants(first_name,last_name,company,job) VALUES(:first_name,:last_name,:company,:job)")

    with engine.connect() as conn:
        conn.execute(stmt,{
            "first_name":first_name,
            "last_name":last_name,
            "company":company,
            "job":job
        })
        conn.commit()

    return render_template('home.1.html')