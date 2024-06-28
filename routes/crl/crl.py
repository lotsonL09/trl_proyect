from flask import Blueprint,render_template,request
from random import shuffle
from aditional_data.crl import crl_questions,fields

import re

fields= fields

condictions={
    'CRL1':2,
    'CRL2':2,
    'CRL3':2,
    'CRL4':2,
    'CRL5':2,
    'CRL6':2,
    'CRL7':3,
    'CRL8':3,
    'CRL9':2
}

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
    count=0
    CRL=None

    iniciacion_evaluacion = request.form.getlist('Iniciacion y Evaluación Preliminar')
    investigacion_analisis = request.form.getlist('Investigación y Análisis de mercado')
    desarrollo_validacion = request.form.getlist('Desarrollo y Validación Técnica')
    lanzamiento_evaluacion = request.form.getlist('Lanzamiento y Evaluación Post-Lanzamiento')
    results.extend(iniciacion_evaluacion)
    results.extend(investigacion_analisis)
    results.extend(desarrollo_validacion)
    results.extend(lanzamiento_evaluacion)
    
    options_marked=[]
    results_new=[]
    print('resultados',results)
    for result in results:
        try:
            index_0=int(re.findall('[CRL0-9]+',result)[1])
            index_1=int(re.findall('[CRL0-9]+',result)[2])
            option=data[fields[index_0]]['questions'][index_1]['pregunta']['enunciado']
            options_marked.append(option)
            results_new.append(re.findall('[CRL0-9]+',result)[0])
        except:
            continue
    print('resultados nuevos',results_new)
    if len(options_marked)==0:
        options_marked='No ha seleccionado ninguna opción'
    for level in condictions.keys():
        if results_new.count(level) == condictions[level]:
            count+=1
        else:
            break
    if count == 0:
        CRL='none'
    else:
        CRL=f'CRL{count}'
    print(options_marked)
    window_content={
        'answers':options_marked,
        'CRL':CRL
    }

    return render_template("/resultados/resultados_crl.1.html",data=window_content)