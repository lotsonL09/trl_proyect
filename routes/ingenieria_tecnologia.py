from flask import Blueprint,render_template,request
from random import shuffle
import re


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

fields=['campo_1','campo_2','campo_3','campo_4']

data={
    'campo_1':{
        'title': 'Investigación',
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se han realizado pruebas experimentales iniciales en condiciones de laboratorio.',
                'TRL': 'TRL3_0_1'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha realizado una búsqueda de información tecnológica.',
                'TRL': 'TRL2_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha realizado la validación de principios básicos a nivel de laboratorio.',
                'TRL': 'TRL3_0_3'
            },
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación técnica básica .',
                'TRL': 'TRL2_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'questions': [
            {'pregunta':{
                'enunciado':'Se cuenta con un prototipo considerado con al menos nivel de banco de pruebas con componentes básicas integradas.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con un prototipo considerado con al menos nivel piloto un entorno de alta fidelidad.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se han realizado pruebas operativas de la tecnología en entornos relevantes o simulados en condiciones controladas .',
                'TRL': 'TRL6_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad del prototipo considerado de al menos nivel de banco de pruebas.',
                'TRL': 'TRL4_1_3'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad del prototipo considerado de al menos nivel de banco de pruebas.',
                'TRL': 'TRL6_1_4'}
            },
            {'pregunta':{
                'enunciado':'Ha realizado evaluaciones iniciales de eficiencia y sostenibilidad de la tecnología.',
                'TRL': 'TRL5_1_5'}
            },
        ]
    },

    'campo_3':{
        'title': 'Implementación',
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales con usuarios finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7_2_0'}
            },
            {'pregunta':{
                'enunciado':'Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias.',
                'TRL': 'TRL7_2_1'}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión final que ha sido completamente desarrollada e implementada.',
                'TRL': 'TRL8_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
                'TRL': 'TRL8_2_3'}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión final que se encuentra en condiciones de pleno funcionamiento.',
                'TRL': 'TRL9_2_4'}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa, se realiza monitoreo y mantenimiento continuo.',
                'TRL': 'TRL9_2_5'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'questions': [
        {'pregunta':{
            'enunciado':'Se está recopilando y analizando datos producto del despliegue y de los usuarios/clientes para realizar las mejoras pertinentes.',
            'TRL': 'TRL9_3_0'}
        },
        {'pregunta':{
            'enunciado':'Se ha hecho el lanzamiento de la tecnología al mercado y se cuenta con un informe de su desempeño y de la retroalimentación continua de los usuarios.',
            'TRL': 'TRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se tiene un diseño adaptado de la tecnología según las necesidades y/o preferencias del mercado.',
            'TRL': 'TRL7_3_2'}
        },
    ]
    },
}

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
        TRL='No hay nivel de TRL'
    else:
        TRL=f'Se encuentra en TRL{count}'
    
    window_content={
        'answers':options_marked,
        'TRL':TRL
    }

    return window_content

