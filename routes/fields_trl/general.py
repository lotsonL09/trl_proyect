from flask import Blueprint,render_template,request
from random import shuffle
import re
from aditional_data.trl import trl_questions_general,fields,trl_data
from aditional_data.results import general


bp_general=Blueprint('general',__name__,url_prefix='/general')


fields=fields

data=trl_questions_general

@bp_general.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('trl/general.1.html',data=data)

@bp_general.route('/evaluacion',methods=['POST'])
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

    options_marked,results_new,spider_dict=general.get_options_marked_and_new_format(results)

    level=general.get_level(results_new)

    window_content={
        'answers':options_marked,
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    return render_template("/resultados/resultados.1.html",data=window_content)