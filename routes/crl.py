from flask import Blueprint,render_template,request
from enum import Enum
from random import shuffle


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

data={
    'campo_1':{
        'title': 'Iniciacion y Evaluación Preliminar',
        'questions': [
            {'pregunta':{
                'enunciado':'Se tiene una comprensión inicial y superficial de cómo la idea podría ser aplicada en el mercado.',
                'CRL': 'CRL_0_0'}
            },
            {'pregunta':{
                'enunciado':'SSe han identificado los nichos y segmentos de mercado, en donde el producto o servicio puede ir enfocado.',
                'CRL': 'CRL_0_1'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha evaluado la viabilidad técnica, comercial y económica sobre cómo deberían ser los productos o servicios para satisfacer las necesidades del mercado.',
                'CRL': 'CRL_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado un modelo inicial de negocio que evalúa los costos de producción y operación en relación con los ingresos esperados y otros beneficios.',
                'CRL': 'CRL_0_3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha validado la propuesta de valor, utilizando modelos detallados de costo-rendimiento que han sido ajustados con datos obtenidos de estudios de mercado.',
                'CRL': 'CRL_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Investigación y Análisis de mercado',
        'questions': [
            {'pregunta':{
                'enunciado':'Aun no se han llevado a cabo investigaciones formales como estudios de mercado, análisis de la competencia, ni evaluaciones de viabilidad técnica y económica.',
                'CRL': 'CRL_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis de mercado basado en información secundaria: datos disponibles públicamente.',
                'CRL': 'CRL_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se ha identificado aplicaciones específicas y realizando un análisis de mercado preliminar basado en encuestas o entrevistas con clientes potenciales.',
                'CRL': 'CRL_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se tiene alguna documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo.',
                'TRL': 'TRL4'}
            },
            {'pregunta':{
                'enunciado':'Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo relevante (fuera de un entorno controlado, pero no es un entorno operativo final).',
                'TRL': 'TRL6'}
            },
            {'pregunta':{
                'enunciado':'Ha realizado evaluaciones iniciales de eficiencia y sostenibilidad de la tecnología.',
                'TRL': 'TRL5'}
            },
        ]
    },

    'campo_3':{
        'title': 'Implementación',
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7'}
            },
            {'pregunta':{
                'enunciado':'Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias.',
                'TRL': 'TRL7'}
            },
            {'pregunta':{
                'enunciado':'La tecnología ha sido completamente desarrollada e implementada.',
                'TRL': 'TRL8'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
                'TRL': 'TRL8'}
            },
            {'pregunta':{
                'enunciado':'Tu tecnología está en proceso de implementación comercial o ya se encuentra en el mercado.',
                'TRL': 'TRL9'}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de pesca de manera regular.',
                'TRL': 'TRL9'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'questions': [
        {'pregunta':{
            'enunciado':'Se está recopilando y analizando datos de los usuarios/clientes pesqueros para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas para aumentar la adopción y expandirse al mercado.',
            'TRL': 'TRL9'}
        },
        {'pregunta':{
            'enunciado':'Se ha desarrollado material de soporte técnico y formación para los usuarios y clientes potenciales.',
            'TRL': 'TRL8'}
        },
        {'pregunta':{
            'enunciado':'Se ha presentado la tecnología a potenciales clientes y/o empresas pesqueras y ha recibido interés para futuras implementaciones comerciales.',
            'TRL': 'TRL7'}
        },
    ]
    },
}

bp_pesca=Blueprint('pesca',__name__,url_prefix='/pesca')


@bp_pesca.route('/')
def root():

    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])

    return render_template('fields/pesca.1.html',data=data)

@bp_pesca.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    count=0
    print(request.form)
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Implementación')
    comercial = request.form.getlist('Desarrollo Comercial')
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