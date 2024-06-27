from flask import Blueprint,render_template,request
from enum import Enum

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

#trl_levels=['TRL1','TRL2','TRL3','TRL4','TRL5','TRL6','TRL7','TRL8','TRL9']

bp_pesca=Blueprint('pesca',__name__,url_prefix='/pesca')


@bp_pesca.route('/')
def root():
    return render_template('fields/pesca.1.html')

@bp_pesca.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    count=0
    investigacion = request.form.getlist('investigacion[]')
    desarrollo = request.form.getlist('desarrollo[]')
    implementacion = request.form.getlist('implementacion[]')
    comercial = request.form.getlist('comercial[]')
    results.extend(investigacion)
    results.extend(desarrollo)
    results.extend(implementacion)
    results.extend(comercial)
    print(results)
    for level in condictions.keys():
        print('nivel',level)
        print(results.count(level))
        print('condicion',condictions[level])
        if results.count(level) == condictions[level]:
            count+=1
        else:
            break
    if count == 0:
        return 'No hay nivel de TRL'
    else:
        return f'Se encuentra en TRL{count}'