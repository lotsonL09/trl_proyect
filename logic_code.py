from PyQt5 import QtWidgets, QtCore

#Para PESCA

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interfaz con checklist")
        
        # Crear el título en la parte superior
        titulo = QtWidgets.QLabel("Technological Readiness Level (TRL)")
        titulo.setStyleSheet("background-color: #457d97; color: white; font-size: 20px;")
        titulo.setAlignment(QtCore.Qt.AlignCenter)
        titulo.setFixedHeight(50)
        
        # Crear la línea de color naranja que va por toda la pantalla
        linea_naranja = QtWidgets.QFrame()
        linea_naranja.setFrameShape(QtWidgets.QFrame.HLine)
        linea_naranja.setFrameShadow(QtWidgets.QFrame.Sunken)
        linea_naranja.setStyleSheet("background-color: orange; color: orange;")
        linea_naranja.setFixedHeight(3)
        
        # Crear un canvas con scroll para contener los bloques
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        
        # Crear los bloques de secciones
        self.variables_seccion1 = self.crear_seccion("Investigación", [
            ("checkbox1_1", "Se ha establecido una base teórica inicial que justifica la necesidad de una investigación (TRL1)"),
            ("checkbox1_2", "Se ha realizado pruebas experimentales iniciales en condiciones controladas (TRL3)"),
            ("checkbox1_3", "Se ha desarrollado modelos conceptuales que describen el funcionamiento práctico de la tecnología (TRL2)"),
            ("checkbox1_4", "La tecnología ha demostrado eficacia en condiciones de laboratorio (TRL3)"),
            ("checkbox1_5", "Se ha formulado una hipótesis clara y específica (TRL2)"),
            ("checkbox1_6", "No cumplo con ninguna de las alternativas")
        ], incluir_enunciado=True)

        self.variables_seccion2 = self.crear_seccion("Desarrollo tecnológico", [
            ("checkbox2_1", "Ha modelado y simulado condiciones marinas en el laboratorio para probar la tecnología planteada, obteniendo resultados positivos (TRL4)"),
            ("checkbox2_2", "Se ha simulado situaciones operativas reales controladas (no necesariamente en el campo o entorno de uso final) para validar la tecnología propuesta (TRL5)"),
            ("checkbox2_3", "Se ha colaborado con pescadores/usuarios para realizar pruebas operativas de la tecnología (TRL6)"),
            ("checkbox2_4", "Se tiene alguna documentación o reportes de las pruebas en el laboratorio que muestren la funcionalidad de tu prototipo (TRL4)"),
            ("checkbox2_5", "Se ha demostrado que la tecnología presentada es eficiente y sostenible en un entorno operativo relevante (fuera de un entorno controlado, pero no es un entorno operativo final) (TRL6)"),
            ("checkbox2_6", "Ha realizado evaluaciones iniciales de eficiencia y sostenibilidad de la tecnología (TRL5)"),
            ("checkbox2_7", "No cumplo con ninguna de las alternativas")
        ], incluir_enunciado=False)

        self.variables_seccion3 = self.crear_seccion("Implementación", [
            ("checkbox3_1", "La tecnología propuesta ya ha sido probada y demostrada en condiciones operativas finales, es decir, en el entorno real de uso (TRL7)"),
            ("checkbox3_2", "Se tiene informes detallados donde se evidencie resultados positivos del desempeño de la tecnología en operaciones diarias (TRL7)"),
            ("checkbox3_3", "La tecnología ha sido completamente desarrollada e implementada (TRL8)"),
            ("checkbox3_4", "Se cuenta con los certificados emitidos por autoridades regulatorias relevantes (TRL8)"),
            ("checkbox3_5", "Tu tecnología está en proceso de implementación comercial o ya se encuentra en el mercado (TRL9)"),
            ("checkbox3_6", "La tecnología está completamente operativa y se utiliza en operaciones comerciales de pesca de manera regular (TRL9)"),
            ("checkbox3_7", "No cumplo con ninguna de las alternativas")
        ], incluir_enunciado=False)

        self.variables_seccion4 = self.crear_seccion("Desarrollo comercial", [
            ("checkbox4_1", "Se está recopilando y analizando datos de los usuarios/clientes pesqueros para realizar las mejoras pertinentes y llevar a cabo campañas de marketing y ventas para aumentar la adopción y expandirse al mercado (TRL 9)"),
            ("checkbox4_2", "Se ha desarrollado material de soporte técnico y formación para los usuarios y clientes potenciales (TRL 8)"),
            ("checkbox4_3", "Se ha presentado la tecnología a potenciales clientes y/o empresas pesqueras y ha recibido interés para futuras implementaciones comerciales (TRL 7)"),
            ("checkbox4_4", "No cumplo con ninguna de las alternativas")
        ], incluir_enunciado=False)

        # Crear el botón para mostrar los checkboxes marcados
        boton_mostrar_marcados = QtWidgets.QPushButton("Mostrar checkboxes marcados")
        boton_mostrar_marcados.clicked.connect(self.mostrar_checkboxes_marcados)

        # Crear el layout principal
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(titulo)
        main_layout.addWidget(linea_naranja)
        main_layout.addWidget(self.scroll_area)
        main_layout.addWidget(boton_mostrar_marcados)

    def crear_seccion(self, titulo_texto, opciones_seccion, incluir_enunciado):
        seccion = QtWidgets.QFrame(self.scroll_content)
        seccion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        seccion.setStyleSheet("background-color: white; border: 2px solid #457d97; border-radius: 5px;")

        vbox = QtWidgets.QVBoxLayout(seccion)

        titulo_seccion = QtWidgets.QLabel(titulo_texto)
        titulo_seccion.setStyleSheet("background-color: #457d97; color: white; font-size: 30px; padding: 5px;")
        titulo_seccion.setAlignment(QtCore.Qt.AlignCenter)
        vbox.addWidget(titulo_seccion)

        if incluir_enunciado:
            enunciado_seccion = QtWidgets.QLabel("Por favor, lea atentamente las siguientes opciones y marque aquellas que su proyecto ya haya llevado a cabo.")
            enunciado_seccion.setStyleSheet("background-color: white; font-size: 26px;")
            enunciado_seccion.setWordWrap(True)
            vbox.addWidget(enunciado_seccion)

        variables_seccion = []
        for var_name, opcion in opciones_seccion:
            checkbox = QtWidgets.QCheckBox(opcion)
            checkbox.setStyleSheet("background-color: white; font-size: 18px; border: none;")
            vbox.addWidget(checkbox)
            setattr(self, var_name, checkbox)
            variables_seccion.append(checkbox)

        # Añadir un QSpacerItem al final del layout del bloque
        vbox.addItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        self.scroll_layout.addWidget(seccion)
        return variables_seccion

    def mostrar_checkboxes_marcados(self):
        # Función para determinar el TRL y mostrar la ventana con los resultados
        def analizar_TRL():
            # Análisis de TRL
            if not self.checkbox1_1.isChecked():
                return "Usted no se encuentra en ningún TRL pues no ha marcado ninguna alternativa"
            if not (self.checkbox1_3.isChecked() and self.checkbox1_5.isChecked()):
                return "Usted se encuentra en un TRL 1, por el cual se encuentra en una investigación básica"
            if not (self.checkbox1_2.isChecked() and self.checkbox1_4.isChecked()):
                return "Usted se encuentra en un TRL 2, por el cual se encuentra en una investigación aplicada"
            if not (self.checkbox2_1.isChecked() and self.checkbox2_4.isChecked()):
                return "Usted se encuentra en un TRL 3, por el cual se encuentra en una investigación aplicada"
            if not (self.checkbox2_2.isChecked() and self.checkbox2_6.isChecked()):
                return "Usted se encuentra en un TRL 4, por el cual se encuentra en una investigación aplicada"
            if not (self.checkbox2_3.isChecked() and self.checkbox2_5.isChecked()):
                return "Usted se encuentra en un TRL 5, por el cual se encuentra en una fase de desarrollo tecnológico"
            if not (self.checkbox3_1.isChecked() and self.checkbox3_2.isChecked() and self.checkbox4_1.isChecked()):
                return "Usted se encuentra en un TRL 6, por el cual se encuentra en una fase de desarrollo tecnológico"
            if not (self.checkbox3_3.isChecked() and self.checkbox3_4.isChecked() and self.checkbox4_2.isChecked()):
                return "Usted se encuentra en un TRL 7, por el cual se encuentra en una fase de Innovación"
            if not (self.checkbox3_5.isChecked() and self.checkbox3_6.isChecked() and self.checkbox4_3.isChecked()):
                return "Usted se encuentra en un TRL 8, por el cual se encuentra en una fase de Innovación"
            return "Usted se encuentra en un TRL 9, por el cual se encuentra en una fase de Desarrollo comercial"

        # Obtener los checkboxes marcados
        checkboxes_marcados = []
        for seccion in [self.variables_seccion1, self.variables_seccion2, self.variables_seccion3, self.variables_seccion4]:
            for checkbox in seccion:
                if checkbox.isChecked():
                    checkboxes_marcados.append(checkbox.text())

        # Crear la nueva ventana para mostrar los checkboxes marcados y el TRL
        ventana_marcados = QtWidgets.QWidget()
        ventana_marcados.setWindowTitle("Checkboxes Marcados")

        layout_marcados = QtWidgets.QVBoxLayout(ventana_marcados)
        
        label_trl = QtWidgets.QLabel(analizar_TRL())
        label_trl.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout_marcados.addWidget(label_trl)

        for texto in checkboxes_marcados:
            label = QtWidgets.QLabel(texto)
            label.setStyleSheet("background-color: white; font-size: 18px; border: none;")
            layout_marcados.addWidget(label)

        ventana_marcados.setLayout(layout_marcados)
        ventana_marcados.show()

        # Mantener una referencia a la nueva ventana para evitar que se cierre
        self.ventana_marcados = ventana_marcados

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
