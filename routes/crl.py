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
                'enunciado':'Se han realizado ajustes y mejoras al prototipo del producto o servicio, basándose en los resultados y el feedback de los consumidores.',
                'cRL': 'cRL_1_3'}
            },
            {'pregunta':{
                'enunciado':'Se han establecido relaciones comerciales estratégicas con proveedores, socios y clientes.',
                'CRL': 'CRL_1_4'}
            },

        ]
    },

    'campo_3':{
        'title': 'Desarrollo y Validación Tencica',
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado los ajustes y mejoras del producto o servicio, para que se adapte mejor a las necesidades y preferencias del mercado.',
                'CRL': 'CRL_2_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha completado el diseño final del producto o servicio, asegurando que todas las características y especificaciones están definidas y optimizadas.',
                'CRL': 'CRL_2_1'}
            },
            {'pregunta':{
                'enunciado':'Se tiene el conocimiento detallado y práctico de las normativas y certificaciones necesarias para operar legalmente y con éxito en el mercado. ',
                'CRL': 'CRL_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado y validado modelos financieros detallados que proyectan los ingresos, costos, y rentabilidad del producto o servicio, tomando en cuenta el entorno económico y de mercado local. ',
                'CRL': 'CRL_2_3'}
            },
            {'pregunta':{
                'enunciado':'El producto cumple con todas las certificaciones y regulaciones requeridas para operar en el mercado. ',
                'CRL': 'CRL_2_4'}
            },

        ]
    },

    'campo_4':{
        'title': 'Lanzamiento y Evaluación Post-Lanzamiento',
        'questions': [
        {'pregunta':{
            'enunciado':'Se ha realizado un ajuste en las estrategias y modelos financieros para reflejar mejor la realidad del mercado y maximizar la rentabilidad. ',
            'CRL': 'CRL_3_0'}
        },
        {'pregunta':{
            'enunciado':'El producto/servicio se ha lanzado oficialmente al mercado y ya se han realizado ventas iniciales.',
            'CRL': 'CRL_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se han recopilado opiniones y calificaciones de los primeros clientes para evaluar la aceptación y el desempeño del producto en condiciones reales.',
            'CRL': 'CRL_3_2'}
        },
                {'pregunta':{
            'enunciado':'El producto/servicio cumple o supera las expectativas del mercado y de los clientes, en términos de calidad, precio, y disponibilidad.',
            'CRL': 'CRL_3_3'}
        },
                {'pregunta':{
            'enunciado':'Se ha logrado una sólida posición en el mercado, con una red de distribución establecida y un flujo constante de producción y ventas. ',
            'CRL': 'CRL_3_4'}
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