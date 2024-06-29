from flask import Blueprint,render_template,request
from random import shuffle
import re
from aditional_data.trl_crl import trl_questions_salud_dispositivos,trl_data
from aditional_data.results import ciencias_salud_dispositivos

data=trl_questions_salud_dispositivos

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

    options_marked,results_new,spider_dict=ciencias_salud_dispositivos.get_options_marked_and_new_format(results)
    
    level=ciencias_salud_dispositivos.get_level(results_new)

    window_content={
        'answers':options_marked,
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    return render_template("/resultados/resultados.1.html",data=window_content)