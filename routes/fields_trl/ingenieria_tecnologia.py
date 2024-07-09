from flask import Blueprint,render_template,request, jsonify
from random import shuffle
from aditional_data.trl_crl import trl_questions_ingenieria_tecnologia,trl_data
from aditional_data.results import ingenieria_tecno
from aditional_data.db import client
import copy



data=copy.deepcopy(trl_questions_ingenieria_tecnologia)

bp_ingenieria_tecnologia=Blueprint('ingenieria_tecnologia',__name__,url_prefix='/ingenieria_tecnologia')

@bp_ingenieria_tecnologia.route('/')
def root():
    # shuffle(data['campo_1']['questions'])
    # shuffle(data['campo_2']['questions'])
    # shuffle(data['campo_3']['questions'])
    # shuffle(data['campo_4']['questions'])
    return render_template('trl/ingenieria_tecnologia.1.html',data=data)

@bp_ingenieria_tecnologia.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Entorno de Desarrollo')
    comercial = request.form.getlist('Implementación y comercialización')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)

    results_new,spider_dict=ingenieria_tecno.get_options_marked_and_new_format(results)
    
    level=ingenieria_tecno.get_level(results_new)

    window_content={
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    json_to_db={
        'participant_data':ingenieria_tecno.valuesCache,
        'form_data':window_content,
        'category':'Ingenieria y Tecnologia'
    }

    client.insert.insert_one(json_to_db)

    return render_template("/resultados/resultados.1.html",data=window_content)

