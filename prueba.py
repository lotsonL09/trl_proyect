import random

questions={
    'campo_1':{
        'title': 'investigacion',
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones controladas.',
                'TRL': 'TRL3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado modelos conceptuales que describen el funcionamiento práctico de la tecnología.',
                'TRL': 'TRL2'
            },
            },
            {'pregunta':{
                'enunciado':'La tecnología ha demostrado eficacia en condiciones de laboratorio.',
                'TRL': 'TRL3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha formulado una hipótesis clara y específica.',
                'TRL': 'TRL2'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'desarrollo',
        'questions': [
            {'pregunta':{
                'enunciado':'Ha modelado y simulado condiciones marinas en el laboratorio para probar la tecnología planteada, obteniendo resultados positivos.',
                'TRL': 'TRL4'}
            },
            {'pregunta':{
                'enunciado':'Se ha simulado situaciones operativas reales controladas (no necesariamente en el campo o entorno de uso final) para validar la tecnología propuesta.',
                'TRL': 'TRL5'}
            },
            {'pregunta':{
                'enunciado':'Se ha colaborado con pescadores/usuarios para realizar pruebas operativas de la tecnología.',
                'TRL': 'TRL6'}
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
        'title': 'implementacion',
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
        'title': 'comercial',
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

dict_prueba={
    1:[
        {
            1:{
                "pregunta":"Uno"
            }
        },
        {
            2:{
                "pregunta":"Dos"
            }
        },
        {
            3:{
                "pregunta":"Tres"
            }
        },
        {
            4:{
                "pregunta":"Cuatro"
            }
        },
    ],
    2:[
        {
            5:{
                "pregunta":"Cinco"
            }
        },
        {
            6:{
                "pregunta":"Seis"
            }
        },
        {
            7:{
                "pregunta":"Siete"
            }
        },
        {
            8:{
                "pregunta":"Ocho"
            }
        },
    ],
}


random.shuffle(questions['campo_1']['questions'])
random.shuffle(questions['campo_2']['questions'])
random.shuffle(questions['campo_3']['questions'])
random.shuffle(questions['campo_4']['questions'])

print(questions)