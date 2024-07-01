from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl_crl import trl_data,trl_questions_pesca
from aditional_data.results import pesca
from aditional_data.db import client
import copy
data=copy.deepcopy(trl_questions_pesca)

bp_pesca=Blueprint('pesca',__name__,url_prefix='/pesca')

@bp_pesca.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('trl/pesca.1.html',data=data)

@bp_pesca.route('/evaluacion',methods=['POST'])
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
    
    results_new,spider_dict=pesca.get_options_marked_and_new_format(results)
    
    level=pesca.get_level(results_new)

    window_content={
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }
    
    json_to_db={
        'participant_data':pesca.valuesCache,
        'form_data':window_content
    }

    client.insert.insert_one(json_to_db)

    return render_template("/resultados/resultados.1.html",data=window_content)