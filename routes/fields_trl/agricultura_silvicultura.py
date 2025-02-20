from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl_crl import trl_questions_agricultura_silvicultura,trl_data
from aditional_data.results import agricultura_silvicultura
from aditional_data.db import client
import copy

bp_agricultura_silvicultura=Blueprint('agricultura_silvicultura',__name__,url_prefix='/agricultura_silvicultura')

data=copy.deepcopy(trl_questions_agricultura_silvicultura)

@bp_agricultura_silvicultura.route('/')
def root():
    # shuffle(data['campo_1']['questions'])
    # shuffle(data['campo_2']['questions'])
    # shuffle(data['campo_3']['questions'])
    # shuffle(data['campo_4']['questions'])
    return render_template('trl/agricultura_silvicultura.1.html',data=data)

@bp_agricultura_silvicultura.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo tecnológico')
    implementacion = request.form.getlist('Entorno de desarrollo')
    comercial = request.form.getlist('Implementación comercial')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)

    results_new,spider_dict=agricultura_silvicultura.get_options_marked_and_new_format(results)
    
    level=agricultura_silvicultura.get_level(results_new)

    window_content={
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    json_to_db={
        'participant_data':agricultura_silvicultura.valuesCache,
        'form_data':window_content,
        'category':'Agricultura y Silvicultura'
    }

    client.insert.insert_one(json_to_db)

    return render_template("/resultados/resultados.1.html",data=window_content)