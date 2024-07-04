from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl_crl import trl_questions_general,fields,trl_data
from aditional_data.results import general
from aditional_data.db import client
import copy

bp_general=Blueprint('general',__name__,url_prefix='/general')


fields=fields

data=copy.deepcopy(trl_questions_general)

@bp_general.route('/')
def root():
    # shuffle(data['campo_1']['questions'])
    # shuffle(data['campo_2']['questions'])
    # shuffle(data['campo_3']['questions'])
    # shuffle(data['campo_4']['questions'])
    return render_template('trl/general.1.html',data=data)

@bp_general.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Entorno de desarrollo')
    comercial = request.form.getlist('Implementación Comercial')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)

    results_new,spider_dict=general.get_options_marked_and_new_format(results)

    level=general.get_level(results_new)

    window_content={
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    json_to_db={
        'participant_data':general.valuesCache,
        'form_data':window_content,
        'category':'General'
    }

    client.insert.insert_one(json_to_db)

    return render_template("/resultados/resultados.1.html",data=window_content)