from flask import Flask,Blueprint,render_template

#importando los bp
from routes.agricultura_silvicultura import bp_agricultura_silvicultura
from routes.ingenieria_tecnologia import bp_ingenieria_tecnologia
from routes.pesca import bp_pesca
from routes.software_hardware import bp_software_hardware
from routes.home import bp_home
from routes.general import bp_general
from routes.ciencias_medicas_salud_medicamentos import bp_ciencias_medicas_salud_medicamentos
from routes.ciencias_medicas_salud_dispositivos import bp_ciencias_medicas_salud_dispositivos
from routes.crl import bp_crl
from routes.resultados import bp_resultados


app=Flask(__name__)
app.register_blueprint(bp_home)
app.register_blueprint(bp_general)
app.register_blueprint(bp_crl)
app.register_blueprint(bp_resultados)
app.register_blueprint(bp_agricultura_silvicultura)
app.register_blueprint(bp_ingenieria_tecnologia)
app.register_blueprint(bp_pesca)
app.register_blueprint(bp_software_hardware)
app.register_blueprint(bp_ciencias_medicas_salud_medicamentos)
app.register_blueprint(bp_ciencias_medicas_salud_dispositivos)

# @app.route('/')
# def home():
#     return render_template('home.1.html')

if __name__ == '__main__':
    app.run(debug=True)

