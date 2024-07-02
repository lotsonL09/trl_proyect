from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl_crl import trl_questions_salud_dispositivos,trl_data_salud_dispositivos
from aditional_data.results import ciencias_salud_dispositivos
from aditional_data.db import client
import copy

data=copy.deepcopy(trl_questions_salud_dispositivos)

bp_ciencias_medicas_salud_dispositivos=Blueprint('ciencias_medicas_salud_dispositivos',__name__,url_prefix='/ciencias_medicas_salud_dispositivos')

@bp_ciencias_medicas_salud_dispositivos.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('trl/ciencias_medicas_salud_dispositivos.1.html',data=data)

@bp_ciencias_medicas_salud_dispositivos.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Fase preclínica/clínica')
    implementacion = request.form.getlist('Desarrollo y Producción')
    comercial = request.form.getlist('Desarrollo Comercial')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)

    results_new,spider_dict=ciencias_salud_dispositivos.get_options_marked_and_new_format(results)
    
    level=ciencias_salud_dispositivos.get_level(results_new)

    window_content={
        'TRL':level,
        'phase':trl_data_salud_dispositivos[level],
        'spider_data':spider_dict
    }

    json_to_db={
        'participant_data':ciencias_salud_dispositivos.valuesCache,
        'form_data':window_content,
        'category':'Ciencias Medicas y de Salud-Dispositivos'
    }

    client.insert.insert_one(json_to_db)

    return render_template("/resultados/resultados.1.html",data=window_content)