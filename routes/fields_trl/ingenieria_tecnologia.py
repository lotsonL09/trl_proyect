from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl_crl import trl_questions_ingenieria_tecnologia,trl_data
from aditional_data.results import ingenieria_tecno

data=trl_questions_ingenieria_tecnologia

bp_ingenieria_tecnologia=Blueprint('ingenieria_tecnologia',__name__,url_prefix='/ingenieria_tecnologia')

@bp_ingenieria_tecnologia.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('trl/ingenieria_tecnologia.1.html',data=data)

@bp_ingenieria_tecnologia.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Implementación')
    comercial = request.form.getlist('Desarrollo Comercial')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)

    options_marked,results_new,spider_dict=ingenieria_tecno.get_options_marked_and_new_format(results)
    
    level=ingenieria_tecno.get_level(results_new)

    
    window_content={
        'answers':options_marked,
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    return render_template("/resultados/resultados.1.html",data=window_content)
