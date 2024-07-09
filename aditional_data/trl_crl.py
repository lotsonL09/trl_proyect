fields=['campo_1','campo_2','campo_3','campo_4']

trl_data={
    'none':'none',
    'TRL 1':'Investigación Básica',
    'TRL 2':'Investigación Aplicada',
    'TRL 3':'Investigación Aplicada',
    'TRL 4':'Investigación Aplicada',
    'TRL 5':'Desarrollo Tecnológico',
    'TRL 6':'Desarrollo Tecnológico',
    'TRL 7':'Desarrollo Tecnológico',
    'TRL 8':'Innovación',
    'TRL 9':'Innovación',
}

trl_data_salud_dispositivos={
    'none':'none',
    'TRL 1':'Investigación Básica',
    'TRL 2':'Investigación Aplicada',
    'TRL 3':'Investigación Aplicada',
    'TRL 4':'Fase Preclínica',
    'TRL 5':'Fase Preclínica',
    'TRL 6':'Fase Clínica',
    'TRL 7':'Fase Clínica',
    'TRL 8':'Validación y Certificación',
    'TRL 9':'Comercialización',
}

trl_data_salud_medicamentos={
    'none':'none',
    'TRL 1':'Investigación Básica',
    'TRL 2':'Investigación Aplicada',
    'TRL 3':'Investigación Aplicada',
    'TRL 4':'Fase Preclínica',
    'TRL 5':'Fase Preclínica',
    'TRL 6':'Fase Clínica',
    'TRL 7':'Fase Clínica',
    'TRL 8':'Fase Clínica',
    'TRL 9':'Comercialización',
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
    'TRL4':3,
    'TRL5':2,
    'TRL6':2,
    'TRL7':3,
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
factor_desarrollo_tecnologico=1.2
factor_implementacion=1.2
factor_desarrollo_comercial=1.2

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
                'enunciado':'Se ha realizado una revisión inicial de información disponible para identificar oportunidades y necesidades del mercado.',
                'CRL': 'CRL1_0_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han identificado los nichos y segmentos de mercado, en donde el producto o servicio puede ir enfocado.',
                'CRL': 'CRL2_0_1',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha evaluado la viabilidad técnica, comercial y económica sobre cómo deberían ser los productos o servicios para satisfacer las necesidades del mercado.',
                'CRL': 'CRL3_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado un modelo inicial de negocio que evalúa los costos de producción y operación en relación con los ingresos esperados y otros beneficios.',
                'CRL': 'CRL4_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha validado la propuesta de valor, utilizando modelos detallados de costo-rendimiento que han sido ajustados con datos obtenidos de estudios de mercado.',
                'CRL': 'CRL5_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Investigación y Análisis de mercado',
        'factor':factor_investigacion_analisis_mercado,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado una exploración inicial de ideas basadas en la identificación preliminar de necesidades del cliente y oportunidades de mercado.',
                'CRL': 'CRL1_1_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado una evaluación preliminar de la viabilidad comercial basándose en información secundaria disponible, como reportes de cámaras de comercio, estudios sectoriales y otros datos públicos.',
                'CRL': 'CRL2_1_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han identificado aplicaciones específicas para el producto o servicio, y además se ha realizado un análisis de mercado preliminar basado en encuestas o entrevistas con clientes potenciales.',
                'CRL': 'CRL3_1_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ajustes y mejoras al prototipo del producto o servicio, basándose en los resultados y el feedback de los consumidores.',
                'CRL': 'CRL4_1_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han establecido relaciones comerciales estratégicas con proveedores, socios y clientes.',
                'CRL': 'CRL5_1_4',
                'chained':False}
            },

        ]
    },

    'campo_3':{
        'title': 'Desarrollo y Validación Técnica',
        'factor':factor_desarrollo_validacion_tecnica,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado los ajustes y mejoras del producto o servicio, para que se adapte mejor a las necesidades y preferencias del mercado.',
                'CRL': 'CRL6_2_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se tiene el conocimiento detallado y práctico de las normativas y certificaciones necesarias para operar legalmente y con éxito en el mercado.',
                'CRL': 'CRL6_2_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha completado el diseño final del producto o servicio, asegurando que todas las características y especificaciones están definidas y optimizadas.',
                'CRL': 'CRL7_2_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado y validado modelos financieros detallados que proyectan los ingresos, costos, y rentabilidad del producto o servicio, tomando en cuenta el entorno económico y de mercado local.',
                'CRL': 'CRL7_2_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'El producto cumple con todas las certificaciones y regulaciones requeridas para operar en el mercado.',
                'CRL': 'CRL7_2_4',
                'chained':False}
            },

        ]
    },

    'campo_4':{
        'title': 'Lanzamiento y Evaluación Post-Lanzamiento',
        'factor':factor_lanzamiento_evaluacion_post_lanzamiento,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado un ajuste en las estrategias y modelos financieros para reflejar mejor la realidad del mercado y maximizar la rentabilidad.',
                'CRL': 'CRL8_3_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'El producto/servicio se ha lanzado oficialmente al mercado y ya se han realizado ventas iniciales.',
                'CRL': 'CRL8_3_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han recopilado opiniones y calificaciones de los primeros clientes para evaluar la aceptación y el desempeño del producto en condiciones reales.',
                'CRL': 'CRL8_3_2',
                'chained':False}
            },
                    {'pregunta':{
                'enunciado':'El producto/servicio cumple o supera las expectativas del mercado y de los clientes, en términos de calidad, precio, y disponibilidad.',
                'CRL': 'CRL9_3_3',
                'chained':False}
            },
                    {'pregunta':{
                'enunciado':'Se ha logrado una sólida posición en el mercado, con una red de distribución establecida y un flujo constante de producción y ventas.',
                'CRL': 'CRL9_3_4',
                'chained':False}
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
                'enunciado':'Se ha determinado los problemas y requerimientos del sector pesquero/acuícola.',
                'TRL': 'TRL1_0_0',
                'chained':False
                }
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado modelos conceptuales que describen el funcionamiento práctico de la tecnología orientada a pesca/acuicultura.',
                'TRL': 'TRL2_0_1',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha corroborado la hipótesis teórica con pruebas iniciales en condiciones controladas.',
                'TRL': 'TRL3_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha mejorado o refinado la tecnología de pesca/acuicultura basadas en datos de laboratorio o condiciones controladas.',
                'TRL': 'TRL4_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se tiene evidencia de resultados positivos del desempeño de la tecnología o producto mínimo viable.',
                'TRL': 'TRL7_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta para pesca/acuicultura ha demostrado eficacia en condiciones de laboratorio o semejantes.',
                'TRL': 'TRL3_1_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha evaluado la funcionalidad del prototipo o tecnología acuícola/pesca.',
                'TRL': 'TRL5_1_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha colaborado con pescadores/acuicultores para realizar pruebas operativas del producto mínimo viable o prototipo con una integración de sus componentes/subsistemas principales y auxiliares.',
                'TRL': 'TRL6_1_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología se encuentra completamente integrada y ha sido calificada a través de pruebas y demostraciones en un entorno real.',
                'TRL': 'TRL8_1_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado evaluaciones periódicas de sostenibilidad y eficiencia de la tecnología/producto finalizado.',
                'TRL': 'TRL9_1_4',
                'chained':False}
            },
        ]
    },

    'campo_3':{
        'title': 'Entorno de desarrollo',
        'factor':factor_implementacion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha modelado y simulado condiciones marinas y/o cuerpos hídricos (para el caso de acuicultura) de baja fidelidad en un entorno de laboratorio o semejante para probar la tecnología planteada, obteniendo resultados positivos.',
                'TRL': 'TRL4_2_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha validado la operatividad del prototipo pesquero/acuícolas en entorno de laboratorio o semejante de alta fidelidad.',
                'TRL': 'TRL5_2_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha demostrado que la tecnología o producto mínimo viable presentada es eficiente y sostenible en un entorno operativo de alta fidelidad (fuera de un entorno controlado, pero no es un entorno operativo final).',
                'TRL': 'TRL6_2_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7_2_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con certificaciones por autoridades regulatorias (si la tecnología lo requiere).',
                'TRL': 'TRL8_2_4',
                'chained':False}
            }
        ]
    },

    'campo_4':{
        'title': 'Implementación comercial',
        'factor':factor_desarrollo_comercial,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis inicial de viabilidad técnica y/o económica.',
                'TRL': 'TRL2_3_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha recopilado retroalimentación de los usuarios finales para mejorar el diseño.',
                'TRL': 'TRL7_3_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha completado el desarrollo del sistema y está listo para la producción.',
                'TRL': 'TRL8_3_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de manera regular.',
                'TRL': 'TRL9_3_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han recopilado y analizado los datos de los usuarios/clientes para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas.',
                'TRL': 'TRL9_3_4',
                'chained':False}
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
                'TRL': 'TRL1_0_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con documentación técnica a nivel básico.',
                'TRL': 'TRL2_0_1',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Las limitaciones han sido identificadas y se ha hecho el planteamiento de las estrategias para abordarlas..',
                'TRL': 'TRL3_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han validado las componentes de la tecnología en condiciones controladas.',
                'TRL': 'TRL4_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han hecho las evaluaciones iniciales de la eficiencia y sostenibilidad de la tecnología.',
                'TRL': 'TRL5_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'Se cuenta con las primeras versiones de la tecnología desarrollada con las funciones iniciales.',
                'TRL': 'TRL3_1_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con una versión alpha del modelo/algoritmo y/o versión inicial de la tecnología.',
                'TRL': 'TRL4_1_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con una versión beta del modelo/algoritmo y/o versión mejorada de la tecnología.',
                'TRL': 'TRL6_1_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con una versión estable del modelo/algoritmo y/o versión optimizada de la tecnología.',
                'TRL': 'TRL8_1_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión estable u optimizada que se encuentra en condiciones de pleno funcionamiento y recibe actualizaciones constantes.',
                'TRL': 'TRL9_1_4',
                'chained':False}
            },
        ]
    },

    'campo_3':{
        'title': 'Implementación',
        'factor':factor_implementacion,
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología ha sido probada por terceros o personas ajenas al equipo de desarrollo en condiciones simuladas.',
                'TRL': 'TRL5_2_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología ha sido probada por usuarios seleccionados en condiciones cercanas a las reales.',
                'TRL': 'TRL6_2_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología se encuentra disponible para los usuarios finales siendo demostrada en condiciones operativas reales.',
                'TRL': 'TRL7_2_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en su versión estable en operaciones diarias.',
                'TRL': 'TRL7_2_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión final que se encuentra en condiciones de pleno funcionamiento.',
                'TRL': 'TRL8_2_4',
                'chained':False}
            },
        ]
    },

    'campo_4':{
        'title': 'Desarrollo Comercial',
        'factor':factor_desarrollo_comercial,
        'questions': [
        {'pregunta':{
            'enunciado':'Se han identificado posibles aplicaciones para la tecnología.',
            'TRL': 'TRL2_3_0',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'Se cuenta con un diseño adaptado de la tecnología según las necesidades y/o preferencias del mercado.',
            'TRL': 'TRL7_3_1',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
            'TRL': 'TRL8_3_2',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'La tecnología está completamente operativa, se realiza monitoreo y mantenimiento continuo.',
            'TRL': 'TRL9_3_2',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'Se ha hecho el lanzamiento de la tecnología y se está recopilando y analizando datos de los usuarios/clientes para realizar las mejoras pertinentes.',
            'TRL': 'TRL9_3_2',
                'chained':False}
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
                'enunciado':'Se ha identificado el problema y las necesidades que justifican una investigación.',
                'TRL': 'TRL1_0_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se cuenta la especificación de   requisitos   formales de la tecnología a nivel básico.',
                'TRL': 'TRL2_0_1',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Las limitaciones han sido identificadas y se ha hecho el planteamiento de las estrategias para abordarlas.',
                'TRL': 'TRL3_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han validado las componentes de la tecnología en condiciones controladas.',
                'TRL': 'TRL4_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han hecho las evaluaciones iniciales de la eficiencia y sostenibilidad de la tecnología.',
                'TRL': 'TRL5_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'Se cuenta con las primeras versiones de la tecnología desarrollada con las funciones iniciales.',
                'TRL': 'TRL3_1_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con una versión alpha del modelo/algoritmo y/o versión inicial de la tecnología.',
                'TRL': 'TRL4_1_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con una versión beta del modelo/algoritmo y/o versión mejorada de la tecnología.',
                'TRL': 'TRL6_1_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con una versión estable del modelo/algoritmo y/o versión optimizada de la tecnología.',
                'TRL': 'TRL8_1_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con una versión estable u optimizada que se encuentra en condiciones de pleno funcionamiento y recibe actualizaciones constantes.',
                'TRL': 'TRL9_1_4',
                'chained':False}
            },
        ]
    },

    'campo_3':{
        'title': 'Entorno de Desarrollo',
        'factor':factor_implementacion,
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología ha sido probada por terceros o personas ajenas al equipo de desarrollo en condiciones simuladas.',
                'TRL': 'TRL5_2_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología ha sido probada por usuarios seleccionados en condiciones cercanas a las reales.',
                'TRL': 'TRL6_2_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología se encuentra disponible para los usuarios finales siendo demostrada en condiciones operativas reales.',
                'TRL': 'TRL7_2_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en su versión estable en operaciones diarias.',
                'TRL': 'TRL7_2_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado capacitación y soporte a los usuarios del sistema y las nuevas funciones integradas.',
                'TRL': 'TRL8_2_4',
                'chained':False}
            },
        ]
    },

    'campo_4':{
        'title': 'Implementación y Comercialización',
        'factor':factor_desarrollo_comercial,
        'questions': [
        {'pregunta':{
            'enunciado':'Se han identificado posibles aplicaciones para la tecnología.',
            'TRL': 'TRL2_3_0',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'Se cuenta con un diseño adaptado de la tecnología según las necesidades y/o preferencias del mercado.',
            'TRL': 'TRL7_3_1',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'Se cuenta con los certificados emitidos por autoridades regulatorias relevantes.',
            'TRL': 'TRL8_3_2',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'La tecnología está completamente operativa, se realiza monitoreo y mantenimiento continuo.',
            'TRL': 'TRL9_3_2',
                'chained':False}
        },
        {'pregunta':{
            'enunciado':'Se ha hecho el lanzamiento de la tecnología, además, se está recopilando y analizando datos de los usuarios/clientes para realizar las mejoras pertinentes.',
            'TRL': 'TRL9_3_2',
                'chained':False}
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
                'enunciado':'Se ha establecido una base teórica inicial que justifica la necesidad de una investigación.',
                'TRL': 'TRL1_0_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado modelos conceptuales que describen el funcionamiento práctico de la tecnología.',
                'TRL': 'TRL2_0_1',
                'chained':False
            },
        },
            {'pregunta':{
                'enunciado':'Se han realizado estudios analíticos y experimentales para validar los principios básicos observados y aplicados.',
                'TRL': 'TRL3_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han validado las componentes y/o subsistemas de la tecnología en condiciones controladas.',
                'TRL': 'TRL4_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se tiene evidencia de resultados positivos del desempeño de la tecnología producto mínimo viable.',
                'TRL': 'TRL7_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta inicial, ha demostrado eficacia en condiciones de laboratorio (ideales) o semejantes.',
                'TRL': 'TRL3_1_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado la validación de un prototipo con una integración básica de sus componentes/subsistemas principales.',
                'TRL': 'TRL5_1_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con un prototipo con una integración de sus componentes/subsistemas principales y auxiliares, el cual ha sido sometido a pruebas rigurosas para validar su viabilidad y efectividad.',
                'TRL': 'TRL6_1_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología se encuentra completamente integrada y ha sido calificada a través de pruebas y demostraciones en un entorno real.',
                'TRL': 'TRL8_1_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado evaluaciones periódicas de sostenibilidad y eficiencia de la tecnología/producto finalizado.',
                'TRL': 'TRL9_1_4',
                'chained':False}
            }
        ]
    },

    'campo_3':{
        'title': 'Entorno de desarrollo',
        'factor':factor_implementacion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha validado el prototipo básico en un entorno de laboratorio (ideal) o semejante (baja fidelidad).',
                'TRL': 'TRL4_2_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha validado el prototipo con integración básica en un entorno simulado de alta fidelidad, asegurando que cada componente individual funciona correctamente antes de su integración final.',
                'TRL': 'TRL5_2_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El prototipo ha sido sometido a pruebas rigurosas para asegurar su viabilidad y efectividad en un entorno operacional simulado (cercano al real).',
                'TRL': 'TRL6_2_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El prototipo del sistema ha sido probado en un entorno operacional real, demostrando su funcionalidad y eficacia en condiciones reales de uso.',
                'TRL': 'TRL7_2_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con certificaciones por autoridades regulatorias (si la tecnología lo requiere).',
                'TRL': 'TRL8_2_4',
                'chained':False}
            }
        ]
    },

    'campo_4':{
        'title': 'Implementación Comercial',
        'factor':factor_desarrollo_comercial,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis inicial de viabilidad técnica y/o económica.',
                'TRL': 'TRL2_3_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha recopilado retroalimentación de los usuarios finales para mejorar el diseño.',
                'TRL': 'TRL7_3_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha completado el desarrollo del sistema y está listo para la producción.',
                'TRL': 'TRL8_3_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de manera regular.',
                'TRL': 'TRL9_3_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han recopilado y analizado los datos de los usuarios/clientes para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas.',
                'TRL': 'TRL9_3_4',
                'chained':False}
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
                'enunciado':'Se ha identificado una necesidad o problema específico en agricultura o silvicultura que la tecnología abordará.',
                'TRL': 'TRL1_0_0',
                'chained':False
                }
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado una idea o concepto inicial para abordar la necesidad identificada en agricultura/silvicultura.',
                'TRL': 'TRL2_0_1',
                'chained':False
            },
        },
            {'pregunta':{
                'enunciado':'Se ha validado el concepto a través de pruebas analíticas y de rendimiento.',
                'TRL': 'TRL3_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han validado los componentes o procesos en un entorno de laboratorio o semejante (baja fidelidad) específico para agricultura o silvicultura.',
                'TRL': 'TRL4_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se tiene evidencia de resultados positivos del desempeño de la tecnología.',
                'TRL': 'TRL7_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo tecnológico',
        'factor':factor_desarrollo_tecnologico,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha demostrado la eficacia de la tecnología propuesta para agricultura/silvicultura en condiciones de laboratorio o similares.',
                'TRL': 'TRL3_1_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado pruebas para validar la operatividad del prototipo con una integración básica orientado al sector agrícola/forestales.',
                'TRL': 'TRL5_1_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se cuenta con un producto mínimo viable o con un prototipo con una integración de sus componentes/subsistemas principales y auxiliares, el cual ha mostrado que es eficiente y sostenible.',
                'TRL': 'TRL6_1_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología se encuentra en un estado beta de desarrollo o se encuentra completamente integrada y ha sido calificada a través de pruebas y demostraciones en un entorno real.',
                'TRL': 'TRL8_1_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales agrícolas/silvícolas de manera regular.',
                'TRL': 'TRL9_1_4',
                'chained':False}
            },
        ]
    },

    'campo_3':{
        'title': 'Entorno de desarrollo',
        'factor':factor_implementacion,
        'questions': [
            {'pregunta':{
                'enunciado':'El prototipo básico o tecnología agrícola/silvícola se ha evaluado en un entorno de laboratorio o similar de baja fidelidad.',
                'TRL': 'TRL4_2_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El prototipo con una integración básica o tecnología agrícola/silvícola se ha validado en un entorno de laboratorio o similar de alta fidelidad, con la finalidad de asegurar que cada componente individual funciona correctamente antes de su integración final.',
                'TRL': 'TRL5_2_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El producto mínimo viable o tecnología ha sido sometido a pruebas operativas de alta fidelidad en colaboración con agricultores/silvicultores, en un entorno operacional simulado (cercano al real).',
                'TRL': 'TRL6_2_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El producto mínimo viable o tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso.',
                'TRL': 'TRL7_2_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'La tecnología cuenta con certificaciones por autoridades regulatorias (si la tecnología lo requiere).',
                'TRL': 'TRL8_2_4',
                'chained':False}
            },
        ]
    },

    'campo_4':{
        'title': 'Implementación comercial',
        'factor':factor_desarrollo_comercial,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis inicial de viabilidad técnica y/o económica.',
                'TRL': 'TRL2_3_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha recopilado retroalimentación de los usuarios finales para mejorar el diseño.',
                'TRL': 'TRL7_3_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha completado el desarrollo del sistema y está listo para la producción del primer lote.',
                'TRL': 'TRL8_3_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'La tecnología está completamente operativa y se utiliza en operaciones comerciales de manera regular.',
                'TRL': 'TRL9_3_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han recopilado y analizado los datos de los usuarios/clientes para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas.',
                'TRL': 'TRL9_3_4',
                'chained':False}
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
                'TRL': 'TRL1_0_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han llevado a cabo ensayos in vitro que proporcionan evidencia inicial de que el concepto es viable y de que los principios del fármaco son efectivos bajo condiciones biológicas controladas.',
                'TRL': 'TRL3_0_1',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha realizado una investigación científica que explora las posibles aplicaciones terapéuticas del fármaco.',
                'TRL': 'TRL2_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos experimentales y se ha validado la hipótesis científica en un entorno de laboratorio.',
                'TRL': 'TRL3_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado el conocimiento necesario para iniciar el desarrollo de un nuevo medicamento, con un propósito definido de aplicación.',
                'TRL': 'TRL2_0_4',
                'chained':False
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
                'TRL': 'TRL4_1_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han realizado estudios de evaluación de dosis, efectos tóxicos a corto y largo plazo, y posibles efectos secundarios.',
                'TRL': 'TRL5_1_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos preclínicos en un entorno de laboratorio, donde se ha evaluado la farmacodinámica y la farmacocinética del nuevo medicamento.',
                'TRL': 'TRL4_1_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 1.',
                'TRL': 'TRL5_1_3',
                'chained':False}
            },
        ]
    },
    'campo_3':{
        'title': 'Ensayos Clínicos',
        'factor':factor_ensayos_clinicos,
        'questions': [
            {'pregunta':{
                'enunciado':'Se han realizado ensayos clínicos de fase 1, donde el nuevo medicamento se ha administrado a un pequeño grupo de voluntarios sanos.',
                'TRL': 'TRL6_2_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 2.',
                'TRL': 'TRL6_2_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos clínicos de fase 2, donde se ha evaluado la eficacia del medicamento y su dosis óptima.',
                'TRL': 'TRL7_2_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Actualmente, tengo la autorización del Instituto Nacional de Salud (INS) para realizar ensayos clínicos de fase 3.',
                'TRL': 'TRL7_2_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos clínicos de fase 3, donde el medicamento se ha administrado a un gran número de pacientes con la enfermedad o condición que el medicamento se destina a tratar.',
                'TRL': 'TRL8_2_4',
                'chained':False}
            },
        ]
    },

    'campo_4':{
        'title': 'Aprobación y Comercialización',
        'factor':factor_aprobacion_comercializacion,
        'questions': [
            {'pregunta':{
                'enunciado':'Se ha confirmado la eficacia del medicamento mediante la realización de ensayos preclínicos y clínicos, donde se han monitoreado los efectos secundarios, y ha comparado los resultados con tratamientos estándar o placebos.',
                'TRL': 'TRL8_3_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'El medicamento cuenta con la aprobación de las autoridades regulatorias para ser lanzado oficialmente al mercado.',
                'TRL': 'TRL8_3_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'El medicamento ha sido lanzado oficialmente al mercado y está disponible para su uso médico.',
                'TRL': 'TRL9_3_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han implementado controles de calidad y sistemas de distribución para asegurar que el medicamento llegue a los usuarios finales de manera segura y oportuna.',
                'TRL': 'TRL9_3_2',
                'chained':False}
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
                'enunciado':'Se ha realizado una investigación científica inicial, que incluye la revisión de literatura relevante, definición de hipótesis y objetivos.',
                'TRL': 'TRL1_0_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha realizado un análisis preliminar de Propiedad Intelectual (PI) para asegurarse de que la idea no infringe patentes existentes y para identificar cualquier invención potencial que pueda ser patentada en el futuro.',
                'TRL': 'TRL2_0_1',
                'chained':False
            },
        },
            {'pregunta':{
                'enunciado':'Se ha desarrollado el conocimiento necesario para iniciar una nueva tecnología, explorando sus posibles aplicaciones.',
                'TRL': 'TRL2_0_2',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han realizado ensayos analíticos y/o experimentales para validar los principios básicos observados y reportados.',
                'TRL': 'TRL3_0_3',
                'chained':False
            },
            },
            {'pregunta':{
                'enunciado':'Se han realizado pruebas en condiciones de laboratorio (in vitro) y/o en modelos animales (in vivo) para demostrar el concepto tecnológico.',
                'TRL': 'TRL4_0_4',
                'chained':False
            }
            }
        ],
    },

    'campo_2':{
        'title': 'Desarrollo Tecnológico',
        'factor':factor_fase_preclinica_clinica,
        'questions': [
            {'pregunta':{
                'enunciado':'La tecnología propuesta ha demostrado viabilidad a través de ensayos experimentales en un entorno de laboratorio.',
                'TRL': 'TRL3_1_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado un prototipo inicial de la tecnología, basado en los resultados de pruebas de laboratorio.',
                'TRL': 'TRL4_1_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado un prototipo estandarizado, el cual ha sido validado mediante ensayos preclínicos.',
                'TRL': 'TRL5_1_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'Se ha desarrollado un prototipo final, el cual ha sido validado mediante ensayos clínicos.',
                'TRL': 'TRL7_1_3',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El dispositivo médico desarrollado se encuentra completamente finalizado, validado y listo para ser comercializado/implementado.',
                'TRL': 'TRL8_1_4',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'La tecnología desarrollada no requiere ser validada mediante ensayos clínicos.',
                'TRL': 'TRL7_1_5',
                'chained':True}
            },
        ]
    },

    'campo_3':{
        'title': 'Entorno de Desarrollo',
        'factor':factor_desarrollo_produccion,
        'questions': [
            {'pregunta':{
                'enunciado':'El prototipo desarrollado y sus componentes han sido validados en un entorno de laboratorio.',
                'TRL': 'TRL4_2_0',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El prototipo desarrollado y sus componentes han sido validados en un entorno simulado que imita las condiciones de uso clínico.',
                'TRL': 'TRL5_2_1',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El prototipo desarrollado y sus componentes han sido validados en un entorno clínico real controlado.',
                'TRL': 'TRL6_2_2',
                'chained':True}
            },
            {'pregunta':{
                'enunciado':'El prototipo desarrollado y sus componentes han sido validados en un entorno clínico real operativo.',
                'TRL': 'TRL7_2_3',
                'chained':True}
            },
        ]
    },

    'campo_4':{
        'title': 'Comercialización/Implementación',
        'factor':factor_desarrollo_comercial_dispositivos,
        'questions': [
            {'pregunta':{
                'enunciado':'Se tiene un registro e historial de los diseños de los prototipos realizados.',
                'TRL': 'TRL6_3_0',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Los prototipos desarrollados han sido optimizados y ya se cuenta con un diseño final del dispositivo médico.',
                'TRL': 'TRL7_3_1',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se ha iniciado el proceso de producción de la tecnología.',
                'TRL': 'TRL8_3_2',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'La tecnología se encuentra disponible para su uso médico y se encuentra en un proceso de comercialización/implementación.',
                'TRL': 'TRL9_3_3',
                'chained':False}
            },
            {'pregunta':{
                'enunciado':'Se han implementado controles de calidad y sistemas de distribución para asegurar que la tecnología llegue a los usuarios finales de manera segura y oportuna.',
                'TRL': 'TRL9_3_3',
                'chained':False}
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




