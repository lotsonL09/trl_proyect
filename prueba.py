from flask import Blueprint,render_template,request
from aditional_data.trl import tree_content,fields

import re


class category:
    def __init__(self,campo_1:str,campo_2:str,campo_3:str,campo_4:str,type:str,name:str):
        self.campo_1=campo_1
        self.campo_2=campo_2
        self.campo_3=campo_3
        self.campo_4=campo_4
        self.type=type
        self.name=name
    
    def get_options_marked_and_new_format(self,results:list):
        options_marked=[]
        results_new=[]
        for result in results:
            try:
                data=tree_content[self.name]
                index_0=int(re.findall(f'[{self.type}0-9]+',result)[1])
                index_1=int(re.findall(f'[{self.type}0-9]+',result)[2])
                option=data[fields[index_0]]['questions'][index_1]['pregunta']['enunciado']
                options_marked.append(option)
                results_new.append(re.findall('[TRL0-9]+',result)[0])
            except:
                continue
        if len(options_marked)==0:
            return 'No ha seleccionado ninguna opción',[]
        return options_marked,results_new
    
    def get_level(self,results_new):
        conditions=tree_content[self.name]['conditions']
        for level in conditions.keys():
            if results_new.count(level) == conditions[level]:
                count+=1
            else:
                break
        if count == 0:
            return 'none'
        if count == 0 and self.type == 'TRL':
            return f'TRL{count}'
        if count == 0 and self.type == 'CRL':
            return f'CRL{count}'




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
    campo_2='Desarrollo Tecnológico',
    campo_3='Implementación',
    campo_4='Desarrollo Comercial',
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
    campo_2='Desarrollo Tecnológico',
    campo_3='Implementación',
    campo_4='Desarrollo Comercial',
    type='TRL',
    name='Pesca'
)



