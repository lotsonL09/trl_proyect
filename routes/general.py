from flask import Blueprint,render_template,request
from random import shuffle
import re


bp_general=Blueprint('general',__name__,url_prefix='/general')

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
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación .',
                'TRL': 'TRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones controlada.',
                'TRL': 'TRL3_0_1'
            },
        },
            {'pregunta':{
                'enunciado':'Se ha desarrollado modelos conceptuales que describen el funcionamiento práctico de la tecnología.',
                'TRL': 'TRL2_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'La tecnología ha demostrado eficacia en condiciones de laboratorio.',
                'TRL': 'TRL3_0_3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha formulado una hipótesis clara y específica.',
                'TRL': 'TRL2_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'questions': [
            {'pregunta':{
                'enunciado':'Ha modelado y simulado en el laboratorio para probar la tecnología planteada, obteniendo resultados positivos.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha simulado situaciones operativas reales controladas (no necesariamente en el campo o entorno de uso final) para validad la tecnología propuesta.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se ha colaborado con usuarios orientados para realizar pruebas operativas de la tecnología.',
                'TRL': 'TRL6_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se tiene alguna documentación o reportes de las prueban en el laboratorio que muestren la funcionalidad de tu prototipo.',
                'TRL': 'TRL4_1_3'}
            },
            {'pregunta':{
                'enunciado':'Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo relevante (fuera de un entorno controlado, pero no es un entorno operativo final).',
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
                'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7_2_0'}
            },
            {'pregunta':{
                'enunciado':'Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias.',
                'TRL': 'TRL7_2_1'}
            },
            {'pregunta':{
                'enunciado':'La tecnología ha sido completamente desarrollada e implementada.',
                'TRL': 'TRL8_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
                'TRL': 'TRL8_2_3'}
            },
            {'pregunta':{
                'enunciado':'Tu tecnología está en proceso de implementación comercial o ya se encuentra en el mercado.',
                'TRL': 'TRL9_2_4'}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de manera regular.',
                'TRL': 'TRL9_2_5'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'questions': [
        {'pregunta':{
            'enunciado':'Se está recopilando y analizando datos de los usuarios/clientes para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas para aumentar la adopción y expandirse al mercado.',
            'TRL': 'TRL9_3_0'}
        },
        {'pregunta':{
            'enunciado':'Se ha desarrollado material de soporte técnico y formación para los usuarios y clientes potenciales.',
            'TRL': 'TRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se ha presentado la tecnología a potenciales clientes y/o empresas y ha recibido interés para futuras implementaciones comerciales.',
            'TRL': 'TRL7_3_2'}
        },
    ]
    },
}

@bp_general.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('fields/general.1.html',data=data)

@bp_general.route('/evaluacion',methods=['POST'])
def evaluation():
    results=[]
    TRL=None
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

    options_marked=[]

    for result in results:
        try:
            index_0=int(re.findall('[TRL0-9]+',result)[1])
            index_1=int(re.findall('[TRL0-9]+',result)[2])
            option=data[fields[index_0]]['questions'][index_1]['pregunta']['enunciado']
            options_marked.append(option)
        except:
            continue

    if len(options_marked)==0:
        options_marked='No ha seleccionado ninguna opción'

    for level in condictions.keys():
        if results.count(level) == condictions[level]:
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