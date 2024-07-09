from aditional_data.trl_crl import tree_content,fields
from copy import deepcopy


class category:
    def __init__(self,campo_1:str,campo_2:str,campo_3:str,campo_4:str,type:str,name:str=None):
        self.campo_1=campo_1
        self.campo_2=campo_2
        self.campo_3=campo_3
        self.campo_4=campo_4
        self.type=type
        self.name=name
        self.__valuesCache = ''
    
    @property
    def valuesCache(self):
        return self.__valuesCache

    @valuesCache.setter
    def valuesCache(self, values):
        self.__valuesCache = values


    def get_options_marked_and_new_format(self,results:list):
        results_new_format=[]
        spider_indexes=[]
        data=tree_content[self.name]['content']
        print('Opciones marcadas por el usuario',results)
        for result in results:
            index_0=int(result.split('_')[1])
            index_1=int(result.split('_')[2])
            spider_indexes.append((index_0,index_1))
            results_new_format.append(result.split('_')[0])

        ########################################################################
        
        #Para obtener el spider_value con el nuevo formato

        spider_indexes_to_get_level=deepcopy(spider_indexes)
        spider_indexes_to_get_level.reverse()

        indexes_by_group={}

        for index in spider_indexes_to_get_level:
            index_0, index_1=index
            if index_0 not in indexes_by_group:
                indexes_by_group[index_0]=[]
            indexes_by_group[index_0].append(index)
        
        list_spider_values=[0,0,0,0]


        questions_added=[]
        for key, indexes in indexes_by_group.items():
            count=0
            clock=True
            for index in indexes:
                index_0,index_1=index
                print(index_0,index_1)
                chained=data[fields[index_0]]['questions'][index_1]['pregunta']['chained']
                if clock:
                    if chained==True:
                        if index_1 == 5:
                            count+= 1+ 3
                            index_1=3
                        else:
                            count+=1+index_1 #suma su punto mas el de los encadenados a esta pregunta
                        clock=False
                        for i in range(index_1):
                            question_added=data[fields[index_0]]['questions'][i]['pregunta'][self.type]
                            if question_added not in results:
                                questions_added.append(question_added.split('_')[0])
                        continue
                    else:
                        count+=1
            factor=data[fields[key]]['factor']
            list_spider_values[key]=count*factor
        #print('preguntas agregadas',questions_added)
        results_new_format.extend(questions_added)
        #print('cantidad de preguntas en total',len(results_new_format))
        ########################################################################
        
        spider_dict=dict()

        for index in range(4):
            questions=[]
            field=index
            for element in spider_indexes:
                if element[0] == index:
                    #amount+=1
                    question=element[1]
                    option=data[fields[field]]['questions'][question]['pregunta']['enunciado']
                    questions.append(option)
                question=None

            if len(questions) == 0:
                questions=["No ha seleccionado ninguna opción"]
            # factor=data[fields[index]]['factor']
            spider_dict[f'campo_{index}']={
                'title':data[fields[field]]['title'],
                'questions':questions,
                'value_spider': list_spider_values[index]  #float(amount*factor)
            }
            
        return results_new_format,spider_dict
    
    def get_level(self,results_new):
        print(results_new)
        count=0
        conditions=tree_content[self.name]['conditions']
        for level in conditions.keys():
            if results_new.count(level) == conditions[level]:
                count+=1
                print(count)
            else:
                break
        if count == 0:
            return 'none'
        if count != 0 and self.type == 'TRL':
            return f'TRL {count}'
        if count != 0 and self.type == 'CRL':
            return f'CRL {count}'


ingenieria_tecno=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Implementación',
    campo_4='Desarrollo Comercial',
    type='TRL',
    name='Ingeniería y Tecnología'
)

agricultura_silvicultura=category(
    campo_1='Investigación',
    campo_2='Desarrollo tecnológico',
    campo_3='Entorno de desarrollo',
    campo_4='Implementación comercial',
    type='TRL',
    name='Agricultura y Silvicultura'
)

software_hardware=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Entorno de Desarrollo',
    campo_4='Implementación y Comercialización',
    type='TRL',
    name='Software y Hardware'
)

ciencias_salud_medicamentos=category(
    campo_1='Investigación',
    campo_2='Ensayos Preclínicos',
    campo_3='Ensayos Clínicos',
    campo_4='Aprobación y Comercialización',
    type='TRL',
    name='Ciencias Médicas y de la Salud-medicamentos'
)

ciencias_salud_dispositivos=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Entorno de Desarrollo',
    campo_4='Comercialización/Implementación',
    type='TRL',
    name='Ciencias Médicas y de la Salud-dispositivos'
)

general=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Entorno de desarrollo',
    campo_4='Implementación Comercial',
    type='TRL',
    name='General'
)

pesca=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Entorno de desarrollo',
    campo_4='Implementación comercial',
    type='TRL',
    name='Pesca'
)

crl=category(
    campo_1='Iniciación y Evaluación Preliminar',
    campo_2='Investigación y Análisis de mercado',
    campo_3='Desarrollo y Validación Técnica',
    campo_4='Lanzamiento y Evaluación Post-Lanzamiento',
    type='CRL',
    name='CRL'
)