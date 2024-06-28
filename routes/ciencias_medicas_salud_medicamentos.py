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
    'TRL8':3,
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
                'enunciado':'Se han llevado a cabo ensayos in vitro que proporcionan evidencia inicial de que el concepto es viable y de que los principios del fármaco son efectivos bajo condiciones biológicas controladas.',
                'TRL': 'TRL3_0_1'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha realizado una investigación científica que explora las posibles aplicaciones terapéuticas del fármaco.',
                'TRL': 'TRL2_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos experimentales y se ha validado la hipótesis científica en un entorno de laboratorio.',
                'TRL': 'TRL3_0_3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado el conocimiento necesario para iniciar el desarrollo de un nuevo medicamento, con un propósito definido de aplicación.',
                'TRL': 'TRL2_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Ensayos Preclínicos',
        'questions': [
            {'pregunta':{
                'enunciado':'Se han realizado ensayos preclínicos in vitro (en células o tejidos) e in vivo (en animales), para identificar posibles efectos adversos del medicamento.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se han realizado estudios de evaluación de dosis, efectos tóxicos a corto y largo plazo, y posibles efectos secundarios.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos preclínicos en un entorno de laboratorio, donde se ha evaluado la farmacodinámica y la farmacocinética del nuevo medicamento.',
                'TRL': 'TRL4_1_2'}
            },
            {'pregunta':{
                'enunciado':'4.	Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 1.',
                'TRL': 'TRL5_1_3'}
            },
        ]
    },

    'campo_3':{
        'title': 'Ensayos Clínicos',
        'questions': [
            {'pregunta':{
                'enunciado':'He realizado ensayos clínicos de fase 1, donde el nuevo medicamento se ha administrado a un pequeño grupo de voluntarios sanos.',
                'TRL': 'TRL6_2_0'}
            },
            {'pregunta':{
                'enunciado':'Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 2.',
                'TRL': 'TRL6_2_1'}
            },
            {'pregunta':{
                'enunciado':'He realizado ensayos clínicos de fase 2, donde se ha evaluado la eficacia del medicamento y su dosis óptima.',
                'TRL': 'TRL7_2_2'}
            },
            {'pregunta':{
                'enunciado':'Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 3.',
                'TRL': 'TRL7_2_3'}
            },
            {'pregunta':{
                'enunciado':'He realizado ensayos clínicos de fase 3, donde el medicamento se ha administrado a un gran número de pacientes con la enfermedad o condición que el medicamento se destina a tratar.',
                'TRL': 'TRL8_2_4'}
            },
        ]
    },

    'campo_4':{
        'title': 'Aprobación y Comercialización',
        'questions': [
        {'pregunta':{
            'enunciado':'Se ha confirmado la eficacia del medicamento mediante la realización de ensayos preclínicos y clínicos, donde se han monitoreado los efectos secundarios, y ha comparado los resultados con tratamientos estándar o placebos.',
            'TRL': 'TRL8_3_0'}
        },
        {'pregunta':{
            'enunciado':'El medicamento cuenta con la aprobación de las autoridades regulatorias para ser lanzado oficialmente al mercado.',
            'TRL': 'TRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se ha realizado una producción a gran escala del medicamento.',
            'TRL': 'TRL9_3_2'}
        },
        {'pregunta':{
            'enunciado':'Se ha realizado una producción a gran escala del medicamento.',
            'TRL': 'TRL9_3_2'}
        },
    ]
    },
}

bp_ciencias_medicas_salud_medicamentos=Blueprint('ciencias_medicas_salud_medicamentos',__name__,url_prefix='/bp_ciencias_medicas_salud_medicamentos')

@bp_ciencias_medicas_salud_medicamentos.route('/')
def root():

    shuffle(data['campo_1']['questions'])
    shuffle(data['campo_2']['questions'])
    shuffle(data['campo_3']['questions'])
    shuffle(data['campo_4']['questions'])

    return render_template('fields/pesca.1.html',data=data)

@bp_ciencias_medicas_salud_medicamentos.route('/evaluacion',methods=['POST'])
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