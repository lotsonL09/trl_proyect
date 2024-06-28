from flask import Blueprint,render_template,request
from random import shuffle
import re
from aditional_data.trl import trl_questions_ingenieria_tecnologia,fields,trl_data

condictions={
    'TRL1':1,
    'TRL2':2,
    'TRL3':2,
    'TRL4':2,
    'TRL5':2,
    'TRL6':2,
    'TRL7':3,
    'TRL8':3,
    'TRL9':3
}

fields=fields

data=trl_questions_ingenieria_tecnologia

bp_ingenieria_tecnologia=Blueprint('ingenieria_tecnologia',__name__,url_prefix='/ingenieria_tecnologia')



@bp_ingenieria_tecnologia.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('fields/ingenieria_tecnologia.1.html',data=data)

@bp_ingenieria_tecnologia.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    TRL=None
    count=0
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Implementación')
    comercial = request.form.getlist('Desarrollo Comercial')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)
    
    options_marked=[]
    results_new=[]
    for result in results:
        try:
            index_0=int(re.findall('[TRL0-9]+',result)[1])
            index_1=int(re.findall('[TRL0-9]+',result)[2])
            option=data[fields[index_0]]['questions'][index_1]['pregunta']['enunciado']
            options_marked.append(option)
            results_new.append(re.findall('[TRL0-9]+',result)[0])
        except:
            continue

    if len(options_marked)==0:
        options_marked='No ha seleccionado ninguna opción'


    for level in condictions.keys():
        if results_new.count(level) == condictions[level]:
            count+=1
        else:
            break
    
    

    if count == 0:
        TRL='none'
    else:
        TRL=f'TRL{count}'
    
    window_content={
        'answers':options_marked,
        'TRL':TRL,
        'phase':trl_data[TRL]
    }

    return render_template("/fields/resultados.1.html",data=window_content)

