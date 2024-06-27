from flask import Blueprint,render_template,request
from random import shuffle

bp_software_hardware=Blueprint('software_hardware',__name__,url_prefix='/software_hardware')

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
        'title': 'Investigación',
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones de laboratorio .',
                'TRL': 'TRL3'
            },
        },
            {'pregunta':{
                'enunciado':'Se ha realizado una búsqueda de información tecnológica .',
                'TRL': 'TRL2'
            },
            },
            {'pregunta':{
                'enunciado':'Se cuenta con un script/diseño básico del programa/prototipo.',
                'TRL': 'TRL3'
            },
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación técnica básica .',
                'TRL': 'TRL2'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'questions': [
            {'pregunta':{
                'enunciado':'Cuenta con una versión alpha del modelo o prototipo inicial con funciones/componentes básicos integrados.',
                'TRL': 'TRL4'}
            },
            {'pregunta':{
                'enunciado':'Se hacen pruebas de la versión alpha o prototipo inicial realizadas por terceros a nivel de laboratorio.',
                'TRL': 'TRL5'}
            },
            {'pregunta':{
                'enunciado':'Se han hecho pruebas de una versión beta o prototipo mejorado con un grupo de usuarios seleccionados a nivel de entorno de alta fidelidad .',
                'TRL': 'TRL6'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo inicial o versión alpha del modelo .',
                'TRL': 'TRL4'}
            },
            {'pregunta':{
                'enunciado':'Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo de alta fidelidad.',
                'TRL': 'TRL6'}
            },
            {'pregunta':{
                'enunciado':'Ha realizado evaluaciones iniciales de eficiencia y sostenibilidad de la tecnología.',
                'TRL': 'TRL5'}
            },
        ]
    },

    'campo_3':{
        'title': 'Innovacion',
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales con usuarios finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7'}
            },
            {'pregunta':{
                'enunciado':'Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias.',
                'TRL': 'TRL7'}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión estable u optimizada que ha sido completamente desarrollada e implementada.',
                'TRL': 'TRL8'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
                'TRL': 'TRL8'}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión estable u optimizada que se encuentra en condiciones de pleno funcionamiento .',
                'TRL': 'TRL9'}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa, se realiza monitoreo y mantenimiento continuo .',
                'TRL': 'TRL9'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'questions': [
        {'pregunta':{
            'enunciado':'Se está recopilando y analizando datos producto del despliegue y de los usuarios/clientes para realizar las mejoras pertinentes.',
            'TRL': 'TRL9'}
        },
        {'pregunta':{
            'enunciado':'Se ha hecho el lanzamiento de la tecnología al mercado y se cuenta con un informe de su desempeño y de la retroalimentación continua de los usuarios.',
            'TRL': 'TRL8'}
        },
        {'pregunta':{
            'enunciado':'Se tiene un diseño adaptado de la tecnología según las necesidades y/o preferencias del mercado.',
            'TRL': 'TRL7'}
        },
    ]
    },
}

@bp_software_hardware.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('fields/software_hardware.1.html',data=data)

@bp_software_hardware.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    count=0
    print(request.form)
    investigacion = request.form.getlist('Investigación')
    desarrollo = request.form.getlist('Desarrollo Tecnológico')
    implementacion = request.form.getlist('Innovacion')
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