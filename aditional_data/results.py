from aditional_data.trl_crl import tree_content,fields

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
        results_new=[]
        indexes_spider=[]
        data=tree_content[self.name]['content']
        for result in results:
            try:
                #index_0=int(re.findall(f'[{self.type}0-9]+',result)[1])
                index_0=int(result.split('_')[1])
                #index_1=int(re.findall(f'[{self.type}0-9]+',result)[2])
                index_1=int(result.split('_')[2])
                #option=data[fields[index_0]]['questions'][index_1]['pregunta']['enunciado']
                #options_marked.append(option)
                indexes_spider.append((index_0,index_1))
                #results_new.append(re.findall(f'[{self.type}0-9]+',result)[0])
                results_new.append(result.split('_')[0])
            except:
                continue

        spider_dict=dict()

        for index in range(4):
            amount=0
            questions=[]
            field=index
            print(data[fields[field]])
            for element in indexes_spider:
                print(element)
                if element[0] == index:
                    amount+=1
                    question=element[1]
                    #field=element[0]
                    print(field,fields[field])
                    print(question,data[fields[field]]['questions'][question])
                    option=data[fields[field]]['questions'][question]['pregunta']['enunciado']
                    print('option marcada',option)
                    
                    questions.append(option)
                question=None

            if len(questions) == 0:
                questions=["No ha seleccionado ninguna opción"]
            factor=data[fields[index]]['factor']
            spider_dict[f'campo_{index}']={
                'title':data[fields[field]]['title'],
                'questions':questions,
                'value_spider': float(amount*factor)
            }

        # for index in stored:
        #     amount=0
        #     for element in indexes_spider:
        #         if index == element[0]:
        #             amount+=1
        #     group_name=data[fields[index]]['title']
        #     factor=data[fields[index]]['factor']
        #     spider_dict[group_name]=amount*factor #correccion de los valores
        
        #print(spider_dict)
        return results_new,spider_dict
    
    def get_level(self,results_new):
        count=0
        conditions=tree_content[self.name]['conditions']
        print(results_new)
        for level in conditions.keys():
            if results_new.count(level) == conditions[level]:
                count+=1
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
    campo_2='Entorno de Desarrollo',
    campo_3='Desarrollo Tecnológico/Producción',
    campo_4='Implementación/Comercialización',
    type='TRL',
    name='Agricultura y Silvicultura'
)

software_hardware=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Implementación',
    campo_4='Desarrollo Comercial',
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
    campo_2='Fase preclínica-clínica',
    campo_3='Implementación',
    campo_4='Desarrollo Comercial',
    type='TRL',
    name='Ciencias Médicas y de la Salud-dispositivos'
)

general=category(
    campo_1='Investigación',
    campo_2='Desarrollo Tecnológico',
    campo_3='Implementación',
    campo_4='Desarrollo Comercial',
    type='TRL',
    name='General'
)

pesca=category(
    campo_1='Investigación',
    campo_2='Entorno de Desarrollo',
    campo_3='Desarrollo tecnológico/Producción',
    campo_4='Implementación/Comercialización',
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