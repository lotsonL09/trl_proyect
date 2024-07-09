from flask import Blueprint,render_template,request
from aditional_data.trl_crl import trl_questions_software_hardware,trl_data
from aditional_data.results import software_hardware
from aditional_data.db import client
import copy
from flask import jsonify

bp_software_hardware=Blueprint('software_hardware',__name__,url_prefix='/software_hardware')

data=copy.deepcopy(trl_questions_software_hardware)

@bp_software_hardware.route('/')
def root():
    # shuffle(data['campo_1']['questions'])
    # shuffle(data['campo_2']['questions'])
    # shuffle(data['campo_3']['questions'])
    # shuffle(data['campo_4']['questions'])
    return render_template('trl/software_hardware.1.html',data=data)
    #return jsonify(data)

@bp_software_hardware.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Entorno de Desarrollo')
    comercial = request.form.getlist('Implementación y Comercialización')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)
    
    results_new,spider_dict=software_hardware.get_options_marked_and_new_format(results)
    
    level=software_hardware.get_level(results_new)
    
    
    window_content={
        'TRL':level,
        'phase':trl_data[level],
        'spider_data':spider_dict
    }

    json_to_db={
        'participant_data':software_hardware.valuesCache,
        'form_data':window_content,
        'category':'Software y Hardware'
    }

    client.insert.insert_one(json_to_db)
    return render_template("/resultados/resultados.1.html",data=window_content)
    #return jsonify(window_content)