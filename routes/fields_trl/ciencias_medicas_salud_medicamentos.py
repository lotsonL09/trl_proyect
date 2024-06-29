from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl import trl_questions_salud_medicamentos,trl_data
from aditional_data.results import ciencias_salud_medicamentos

data=trl_questions_salud_medicamentos

bp_ciencias_medicas_salud_medicamentos=Blueprint('ciencias_medicas_salud_medicamentos',__name__,url_prefix='/ciencias_medicas_salud_medicamentos')

@bp_ciencias_medicas_salud_medicamentos.route('/')
def root():

    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('trl/ciencias_medicas_salud_medicamentos.1.html',data=data)

@bp_ciencias_medicas_salud_medicamentos.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Ensayos Preclínicos')
    implementacion = request.form.getlist('Ensayos Clínicos')
    comercial = request.form.getlist('Aprobación y Comercialización')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)

    options_marked,results_new,spider_dict=ciencias_salud_medicamentos.get_options_marked_and_new_format(results)
    
    level=ciencias_salud_medicamentos.get_level(results_new)

    window_content={
        'answers':options_marked,
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    return render_template("/resultados/resultados.1.html",data=window_content)