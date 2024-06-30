fields=['campo_1','campo_2','campo_3','campo_4']

trl_data={
    'none':'none',
    'TRL1':'Investigación Básica',
    'TRL2':'Investigación Aplicada',
    'TRL3':'Investigación Aplicada',
    'TRL4':'Investigación Aplicada',
    'TRL5':'Desarrollo Tecnológico',
    'TRL6':'Desarrollo Tecnológico',
    'TRL7':'Desarrollo Tecnológico',
    'TRL8':'Innovación',
    'TRL9':'Innovación',
}

condictions_crl={
    'CRL1':2,
    'CRL2':2,
    'CRL3':2,
    'CRL4':2,
    'CRL5':2,
    'CRL6':2,
    'CRL7':3,
    'CRL8':3,
    'CRL9':2
}

condictions_ing_tec=condictions_general=condictions_agri_silvi=condictions_pesca=condictions_software_hardware={
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

condictions_salud_dispositivos={
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

condictions_salud_medicamentos={
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

#El resto de disciplinas
factor_investigacion=1.2
factor_desarrollo_tecnologico=1
factor_implementacion=1
factor_desarrollo_comercial=2

#Salud-Dispositivos
factor_fase_preclinica_clinica=1.2
factor_desarrollo_produccion=1.5
factor_desarrollo_comercial_dispositivos=1.5

#Salud-Medicamentos
factor_ensayos_preclinicos=1.5
factor_ensayos_clinicos=1.2
factor_aprobacion_comercializacion=1.5

#CRL
factor_iniciacion_evaluacion_preliminar=1.2
factor_investigacion_analisis_mercado=1.2
factor_desarrollo_validacion_tecnica=1.2
factor_lanzamiento_evaluacion_post_lanzamiento=1.2

crl_questions={
    'campo_1':{
        'title': 'Iniciación y Evaluación Preliminar',
        'factor':factor_iniciacion_evaluacion_preliminar,
        'questions': [
            {'pregunta':{
                'enunciado':'Se tiene una comprensión inicial y superficial de cómo la idea podría ser aplicada en el mercado.',
                'CRL': 'CRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se han identificado los nichos y segmentos de mercado, en donde el producto o servicio puede ir enfocado.',
                'CRL': 'CRL2_0_1'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha evaluado la viabilidad técnica, comercial y económica sobre cómo deberían ser los productos o servicios para satisfacer las necesidades del mercado.',
                'CRL': 'CRL3_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado un modelo inicial de negocio que evalúa los costos de producción y operación en relación con los ingresos esperados y otros beneficios.',
                'CRL': 'CRL4_0_3'
            },
            },
            {'pregunta':{
                'enunciado':'Se ha validado la propuesta de valor, utilizando modelos detallados de costo-rendimiento que han sido ajustados con datos obtenidos de estudios de mercado.',
                'CRL': 'CRL5_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Investigación y Análisis de mercado',
        'factor':factor_investigacion_analisis_mercado,
        'questions': [
            {'pregunta':{
                'enunciado':'Aun no se han llevado a cabo investigaciones formales como estudios de mercado, análisis de la competencia, ni evaluaciones de viabilidad técnica y económica.',
                'CRL': 'CRL1_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis de mercado basado en información secundaria: datos disponibles públicamente.',
                'CRL': 'CRL2_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se ha identificado aplicaciones específicas y realizando un análisis de mercado preliminar basado en encuestas o entrevistas con clientes potenciales.',
                'CRL': 'CRL3_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ajustes y mejoras al prototipo del producto o servicio, basándose en los resultados y el feedback de los consumidores.',
                'CRL': 'CRL4_1_3'}
            },
            {'pregunta':{
                'enunciado':'Se han establecido relaciones comerciales estratégicas con proveedores, socios y clientes.',
                'CRL': 'CRL5_1_4'}
            },

        ]
    },

    'campo_3':{
        'title': 'Desarrollo y Validación Técnica',
        'factor':factor_desarrollo_validacion_tecnica,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado los ajustes y mejoras del producto o servicio, para que se adapte mejor a las necesidades y preferencias del mercado.',
                'CRL': 'CRL6_2_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha completado el diseño final del producto o servicio, asegurando que todas las características y especificaciones están definidas y optimizadas.',
                'CRL': 'CRL7_2_1'}
            },
            {'pregunta':{
                'enunciado':'Se tiene el conocimiento detallado y práctico de las normativas y certificaciones necesarias para operar legalmente y con éxito en el mercado. ',
                'CRL': 'CRL6_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado y validado modelos financieros detallados que proyectan los ingresos, costos, y rentabilidad del producto o servicio, tomando en cuenta el entorno económico y de mercado local. ',
                'CRL': 'CRL7_2_3'}
            },
            {'pregunta':{
                'enunciado':'El producto cumple con todas las certificaciones y regulaciones requeridas para operar en el mercado.',
                'CRL': 'CRL7_2_4'}
            },

        ]
    },

    'campo_4':{
        'title': 'Lanzamiento y Evaluación Post-Lanzamiento',
        'factor':factor_lanzamiento_evaluacion_post_lanzamiento,
        'questions': [
        {'pregunta':{
            'enunciado':'Se ha realizado un ajuste en las estrategias y modelos financieros para reflejar mejor la realidad del mercado y maximizar la rentabilidad.',
            'CRL': 'CRL8_3_0'}
        },
        {'pregunta':{
            'enunciado':'El producto/servicio se ha lanzado oficialmente al mercado y ya se han realizado ventas iniciales.',
            'CRL': 'CRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se han recopilado opiniones y calificaciones de los primeros clientes para evaluar la aceptación y el desempeño del producto en condiciones reales.',
            'CRL': 'CRL8_3_2'}
        },
                {'pregunta':{
            'enunciado':'El producto/servicio cumple o supera las expectativas del mercado y de los clientes, en términos de calidad, precio, y disponibilidad.',
            'CRL': 'CRL9_3_3'}
        },
                {'pregunta':{
            'enunciado':'Se ha logrado una sólida posición en el mercado, con una red de distribución establecida y un flujo constante de producción y ventas.',
            'CRL': 'CRL9_3_4'}
        },
    ]
    },
}

trl_questions_pesca={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones controladas.',
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
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'Ha modelado y simulado condiciones marinas en el laboratorio para probar la tecnología planteada, obteniendo resultados positivos.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha simulado situaciones operativas reales controladas (no necesariamente en el campo o entorno de uso final) para validar la tecnología propuesta.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se ha colaborado con pescadores/usuarios para realizar pruebas operativas de la tecnología.',
                'TRL': 'TRL6_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se tiene alguna documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo.',
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
        'factor':factor_implementacion,
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
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de pesca de manera regular.',
                'TRL': 'TRL9_2_5'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'factor':factor_desarrollo_comercial,
        'questions': [
        {'pregunta':{
            'enunciado':'Se está recopilando y analizando datos de los usuarios/clientes pesqueros para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas para aumentar la adopción y expandirse al mercado.',
            'TRL': 'TRL9_3_0'}
        },
        {'pregunta':{
            'enunciado':'Se ha desarrollado material de soporte técnico y formación para los usuarios y clientes potenciales.',
            'TRL': 'TRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se ha presentado la tecnología a potenciales clientes y/o empresas pesqueras y ha recibido interés para futuras implementaciones comerciales.',
            'TRL': 'TRL7_3_2'}
        },
    ]
    },
}

trl_questions_ingenieria_tecnologia={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
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
                'enunciado':'Se cuenta con documentación técnica básica.',
                'TRL': 'TRL2_0_4'
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'factor':factor_desarrollo_tecnologico,
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
                'enunciado':'Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo relevante o simulado en condiciones controladas.',
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
        'factor':factor_implementacion,
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
        'factor':factor_desarrollo_comercial,
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

trl_questions_software_hardware={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones de laboratorio .',
                'TRL': 'TRL3_0_1'
            },
        },
            {'pregunta':{
                'enunciado':'Se ha realizado una búsqueda de información tecnológica .',
                'TRL': 'TRL2_0_2'
            },
            },
            {'pregunta':{
                'enunciado':'Se cuenta con un script/diseño básico del programa/prototipo.',
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
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'Cuenta con una versión alpha del modelo o prototipo inicial con funciones/componentes básicos integrados.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se hacen pruebas de la versión alpha o prototipo inicial realizadas por terceros a nivel de laboratorio.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se han hecho pruebas de una versión beta o prototipo mejorado con un grupo de usuarios seleccionados a nivel de entorno de alta fidelidad.',
                'TRL': 'TRL6_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo inicial o versión alpha del modelo.',
                'TRL': 'TRL4_1_3'}
            },
            {'pregunta':{
                'enunciado':'Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo de alta fidelidad.',
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
        'factor':factor_implementacion,
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
                'enunciado':'La tecnología cuenta con una versión estable u optimizada que ha sido completamente desarrollada e implementada.',
                'TRL': 'TRL8_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
                'TRL': 'TRL8_2_3'}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión estable u optimizada que se encuentra en condiciones de pleno funcionamiento.',
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
        'factor':factor_desarrollo_comercial,
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

trl_questions_general={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
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
        'factor':factor_desarrollo_tecnologico,
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
        'factor':factor_implementacion,
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
        'factor':factor_desarrollo_comercial,
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

trl_questions_agricultura_silvicultura={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1_0_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas experimentales iniciales en condiciones controladas.',
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
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'Ha modelado y simulado condiciones marinas en el laboratorio para probar la tecnología planteada, obteniendo resultados positivos.',
                'TRL': 'TRL4_1_0'}
            },
            {'pregunta':{
                'enunciado':'Se ha simulado situaciones operativas reales controladas (no necesariamente en el campo o entorno de uso final) para validar la tecnología propuesta.',
                'TRL': 'TRL5_1_1'}
            },
            {'pregunta':{
                'enunciado':'Se ha colaborado con pescadores/usuarios para realizar pruebas operativas de la tecnología.',
                'TRL': 'TRL6_1_2'}
            },
            {'pregunta':{
                'enunciado':'Se tiene alguna documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo.',
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
        'factor':factor_implementacion,
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7_2_0'}
            },
            {'pregunta':{
                'enunciado':'Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias .',
                'TRL': 'TRL7_2_1'}
            },
            {'pregunta':{
                'enunciado':'La tecnología ha sido completamente desarrollada e implementada.',
                'TRL': 'TRL8_2_2'}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes para el sector agrícola.',
                'TRL': 'TRL8_2_3'}
            },
            {'pregunta':{
                'enunciado':'Tu tecnología está en proceso de implementación comercial o ya se encuentra en el mercado agrícola.',
                'TRL': 'TRL9_2_4'}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de agrícolas de manera regular.',
                'TRL': 'TRL9_2_5'}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'factor':factor_desarrollo_comercial,
        'questions': [
        {'pregunta':{
            'enunciado':'Se está recopilando y analizando datos de los usuarios/clientes agrícolas para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas para aumentar la adopción y expandirse al mercado.',
            'TRL': 'TRL9_3_0'}
        },
        {'pregunta':{
            'enunciado':'Se ha desarrollado material de soporte técnico y formación para los usuarios y clientes potenciales .',
            'TRL': 'TRL8_3_1'}
        },
        {'pregunta':{
            'enunciado':'Se ha presentado la tecnología a potenciales clientes y/o empresas agrícolas y ha recibido interés para futuras implementaciones comerciales.',
            'TRL': 'TRL7_3_2'}
        },
    ]
    },
}

trl_questions_salud_medicamentos={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
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
        'factor':factor_ensayos_preclinicos,
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
                'enunciado':'Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 1.',
                'TRL': 'TRL5_1_3'}
            },
        ]
    },

    'campo_3':{
        'title': 'Ensayos Clínicos',
        'factor':factor_ensayos_clinicos,
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
        'factor':factor_aprobacion_comercializacion,
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

trl_questions_salud_dispositivos={
    'campo_1':{
        'title': 'Investigación',
        'factor':factor_investigacion,
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
        'factor':factor_fase_preclinica_clinica,
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
                'enunciado':'Se ha demostrado el funcionamiento de la tecnología en un entorno operacional real, y ya se cuenta con una Autorización Sanitaria por parte de DIGEMID.',
                'TRL': 'TRL7_1_4'}
            },
        ]
    },

    'campo_3':{
        'title': 'Desarrollo y Producción',
        'factor':factor_desarrollo_produccion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado un prototipo de la tecnología, basado en los resultados de los ensayos entorno a laboratorio.',
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
        'factor':factor_desarrollo_comercial_dispositivos,
        'questions': [
        {'pregunta':{
            'enunciado':'Se ha realizado la optimización de la tecnología para que se adapte mejor a las necesidades y preferencias del mercado.',
            'TRL': 'TRL7_3_0'}
        },
        {'pregunta':{
            'enunciado':'El dispositivo médico ha finalizado su desarrollo, pruebas y validaciones, obteniendo la certificación oficial para su uso.',
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

tree_content ={
    'Ingeniería y Tecnología':{
        'content':trl_questions_ingenieria_tecnologia,
        'conditions':condictions_ing_tec
    }
    ,
    'Agricultura y Silvicultura':{
        'content':trl_questions_agricultura_silvicultura,
        'conditions':condictions_agri_silvi
    },
    'Software y Hardware':{
        'content':trl_questions_software_hardware,
        'conditions':condictions_software_hardware
    },
    'Ciencias Médicas y de la Salud-medicamentos':{
        'content':trl_questions_salud_medicamentos,
        'conditions':condictions_salud_medicamentos
    },
    'Ciencias Médicas y de la Salud-dispositivos':{
        'content':trl_questions_salud_dispositivos,
        'conditions':condictions_salud_dispositivos
    },
    'General':{
        'content':trl_questions_general,
        'conditions':condictions_general
    },
    'Pesca':{
        'content':trl_questions_pesca,
        'conditions':condictions_pesca
    },
    'CRL':{
        'content':crl_questions,
        'conditions': condictions_crl
    }
}




