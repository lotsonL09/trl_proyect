from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl_crl import crl_questions
from aditional_data.results import crl

data=crl_questions

bp_crl=Blueprint('crl',__name__,url_prefix='/crl')


@bp_crl.route('/')
def root():

    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])

    return render_template('crl/crl.1.html',data=data)

@bp_crl.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    iniciacion_evaluacion = request.form.getlist('Iniciación y Evaluación Preliminar')
    investigacion_analisis = request.form.getlist('Investigación y Análisis de mercado')
    desarrollo_validacion = request.form.getlist('Desarrollo y Validación Técnica')
    lanzamiento_evaluacion = request.form.getlist('Lanzamiento y Evaluación Post-Lanzamiento')
    results.extend(iniciacion_evaluacion)
    results.extend(investigacion_analisis)
    results.extend(desarrollo_validacion)
    results.extend(lanzamiento_evaluacion)
    
    options_marked,results_new,spider_dict=crl.get_options_marked_and_new_format(results)
    
    level=crl.get_level(results_new)

    
    window_content={
        'answers':options_marked,
        'CRL':level,
        'spider_data':spider_dict
    }

    return render_template("/resultados/resultados_crl.1.html",data=window_content)