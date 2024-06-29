from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.trl import trl_questions_agricultura_silvicultura,trl_data
from aditional_data.results import agricultura_silvicultura

bp_agricultura_silvicultura=Blueprint('agricultura_silvicultura',__name__,url_prefix='/agricultura_silvicultura')

data=trl_questions_agricultura_silvicultura

@bp_agricultura_silvicultura.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('trl/agricultura_silvicultura.1.html',data=data)

@bp_agricultura_silvicultura.route('/evaluacion',methods=['POST'])
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

    options_marked,results_new=agricultura_silvicultura.get_options_marked_and_new_format(results)
    
    level=agricultura_silvicultura.get_level(results_new)

    
    window_content={
        'answers':options_marked,
        'TRL':level,
        'phase':trl_data[level]
    }

    return render_template("/resultados/resultados.1.html",data=window_content)