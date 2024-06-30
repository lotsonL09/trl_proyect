from flask import Blueprint,render_template,request, jsonify
from aditional_data.db import engine
from aditional_data.db import engine
from sqlalchemy import text
from aditional_data.results import ingenieria_tecno, general,agricultura_silvicultura,crl,ciencias_salud_dispositivos,ciencias_salud_medicamentos,software_hardware,pesca

bp_register=Blueprint('register',__name__,url_prefix='/')

# Main home
@bp_register.route("/")
def root():
    return render_template("datos.html")

@bp_register.route('/register_participant',methods=['POST'])
def register_participant():
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    company=request.form['company']
    job=request.form['job']

    objData = {
        'first_name' : first_name,
        'last_name':last_name,
        'company':company,
        'job':job
    }

    ingenieria_tecno.valuesCache = objData
    general.valuesCache = objData
    agricultura_silvicultura.valuesCache = objData
    software_hardware.valuesCache = objData
    ciencias_salud_medicamentos.valuesCache = objData
    ciencias_salud_dispositivos.valuesCache = objData
    crl.valuesCache = objData
    pesca.valuesCache = objData

    return jsonify({'message':'Conexion exitosa', 'error':False})


@bp_register.route("/datos/db", methods=['POST'])
def data_db():
    respuesta = request.data
    print(respuesta)
    