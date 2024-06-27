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

questions={
    'investigacion':{
        'pregunta_1':{
            'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
            'TRL': 'TRL1'
        },
        'pregunta_2':{
            'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones controladas.',
            'TRL': 'TRL3'
        },
        'pregunta_3':{
            'enunciado':'Se ha desarrollado modelos conceptuales que describen el funcionamiento práctico de la tecnología.',
            'TRL': 'TRL2'
        },
        'pregunta_4':{
            'enunciado':'La tecnología ha demostrado eficacia en condiciones de laboratorio.',
            'TRL': 'TRL3'
        },
        'pregunta_5':{
            'enunciado':'Se ha formulado una hipótesis clara y específica.',
            'TRL': 'TRL2'
        },
    },
    'desarrollo':{
        'pregunta_1':{
            'enunciado':'Ha modelado y simulado condiciones marinas en el laboratorio para probar la tecnología planteada, obteniendo resultados positivos.',
            'TRL': 'TRL4'
        },
        'pregunta_2':{
            'enunciado':'Se ha simulado situaciones operativas reales controladas (no necesariamente en el campo o entorno de uso final) para validar la tecnología propuesta.',
            'TRL': 'TRL5'
        },
        'pregunta_3':{
            'enunciado':'Se ha colaborado con pescadores/usuarios para realizar pruebas operativas de la tecnología.',
            'TRL': 'TRL6'
        },
        'pregunta_4':{
            'enunciado':'Se tiene alguna documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo.',
            'TRL': 'TRL4'
        },
        'pregunta_5':{
            'enunciado':'Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo relevante (fuera de un entorno controlado, pero no es un entorno operativo final).',
            'TRL': 'TRL6'
        },
        'pregunta_6':{
            'enunciado':'Ha realizado evaluaciones iniciales de eficiencia y sostenibilidad de la tecnología.',
            'TRL': 'TRL5'
        },
    },
    'implementacion':{
        'pregunta_1':{
            'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso.',
            'TRL': 'TRL7'
        },
        'pregunta_2':{
            'enunciado':'Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias.',
            'TRL': 'TRL7'
        },
        'pregunta_3':{
            'enunciado':'La tecnología ha sido completamente desarrollada e implementada.',
            'TRL': 'TRL8'
        },
        'pregunta_4':{
            'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
            'TRL': 'TRL8'
        },
        'pregunta_5':{
            'enunciado':'Tu tecnología está en proceso de implementación comercial o ya se encuentra en el mercado.',
            'TRL': 'TRL9'
        },
        'pregunta_5':{
            'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de pesca de manera regular.',
            'TRL': 'TRL9'
        },
    },
    'comercial':{
        'pregunta_1':{
            'enunciado':'Se está recopilando y analizando datos de los usuarios/clientes pesqueros para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas para aumentar la adopción y expandirse al mercado.',
            'TRL': 'TRL9'
        },
        'pregunta_2':{
            'enunciado':'Se ha desarrollado material de soporte técnico y formación para los usuarios y clientes potenciales.',
            'TRL': 'TRL8'
        },
        'pregunta_3':{
            'enunciado':'Se ha presentado la tecnología a potenciales clientes y/o empresas pesqueras y ha recibido interés para futuras implementaciones comerciales.',
            'TRL': 'TRL7'
        },
    },
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