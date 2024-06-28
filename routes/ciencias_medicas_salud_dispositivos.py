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
    'TRL7':2,
    'TRL8':2,
    'TRL9':2
}

fields=['campo_1','campo_2','campo_3','campo_4']

data={
    'campo_1':{
        'title': 'Investigación',
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado una investigación científica inicial, la cual incluye: Revisión de literatura relevante, definición de hipótesis y objetivos.',
                'TRL': 'TRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos experimentales y se ha validado la hipótesis científica.',
                'TRL': 'TRL3_0_1'
            },
        },
            {'pregunta':{
                'enunciado':'Se ha desarrollado el conocimiento necesario para iniciar una nueva tecnología, explorando sus posibles aplicaciones.',
                'TRL': 'TRL2_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha demostrado la viabilidad de la nueva tecnología a través de ensayos in vitro. (pruebas de concepto tecnológico)',
                'TRL': 'TRL3_0_3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis preliminar de Propiedad Intelectual (PI) para asegurarse de que la idea no infringe patentes existentes y para identificar cualquier invención potencial que pueda ser patentada en el futuro.',
                'TRL': 'TRL2_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Fase preclínica/clínica',
        'questions': [
            {'pregunta':{
                'enunciado':'Se han realizado ensayos preclínicos en entorno de laboratorio, donde la tecnología ha demostrado cumplir con los requerimientos de rendimiento y funcionabilidad.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Los ensayos preclínicos han sido validados en entornos simulados cercanos al real, lo que asegura que la tecnología cumple con los requisitos y expectativas de los usuarios.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con autorización del Instituto Nacional de Salud (INS) para la realización de ensayos clínicos. ',
                'TRL': 'TRL5_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se han hecho ensayos clínicos para verificar la seguridad del dispositivo médico y su compatibilidad con el entorno clínico y fisiológico específico en el cual será utilizado.',
                'TRL': 'TRL6_1_3'}
            },
            {'pregunta':{
                'enunciado':'11.	Se ha demostrado el funcionamiento de la tecnología en un entorno operacional real, y ya se cuenta con una Autorización Sanitaria por parte de DIGEMID.',
                'TRL': 'TRL7_1_4'}
            },
        ]
    },

    'campo_3':{
        'title': 'Desarrollo y Producción',
        'questions': [
            {'pregunta':{
                'enunciado':'12.	Se ha realizado un prototipo de la tecnología, basado en los resultados de los ensayos entorno a laboratorio.',
                'TRL': 'TRL4_2_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado una producción limitada de prototipos de la tecnología. (Lote piloto) ',
                'TRL': 'TRL5_2_1'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado la producción mayor (Lote) de la tecnología.',
                'TRL': 'TRL6_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado una producción a gran escala del producto/servicio. ',
                'TRL': 'TRL8_2_3'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'questions': [
        {'pregunta':{
            'enunciado':'Se ha realizado la optimización de la tecnología para que se adapte mejor a las necesidades y preferencias del mercado.',
            'TRL': 'TRL7_3_0'}
        },
        {'pregunta':{
            'enunciado':'El dispositivo médico ha finalizado su desarrollo, pruebas y validaciones, obteniendo la certificación oficial para su uso. ',
            'TRL': 'TRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'La tecnología ha sido lanzada oficialmente al mercado y está disponible para su uso médico.',
            'TRL': 'TRL9_3_2'}
        },
        {'pregunta':{
            'enunciado':'Se han implementado controles de calidad y sistemas de distribución para asegurar que el dispositivo médico llegue a los usuarios finales de manera segura y oportuna.',
            'TRL': 'TRL9_3_3'}
        },
    ]
    },
}

bp_ciencias_medicas_salud_dispositivos=Blueprint('ciencias_medicas_salud_dispositivos',__name__,url_prefix='/ciencias_medicas_salud_dispositivos')

@bp_ciencias_medicas_salud_dispositivos.route('/')
def root():
    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])
    return render_template('fields/ciencias_medicas_salud_dispositivos.1.html')

@bp_ciencias_medicas_salud_dispositivos.route('/evaluacion',methods=['POST'])
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