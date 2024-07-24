import logging
from flask import Flask, jsonify
from flask_mail import Mail, Message
from config import DevelopmentConfig
from extensions import db  # Asegúrate de que estás importando db desde extensions
import utils
from sqlalchemy import inspect  # Importa inspect

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logging.debug('Este es un mensaje de debug')
logging.info('Este es un mensaje informativo')
logging.warning('Este es un mensaje de advertencia')
logging.error('Este es un mensaje de error')
logging.critical('Este es un mensaje crítico')

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializar la base de datos
db.init_app(app)

# Configuración de correo electrónico (comentar si no se usa)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'diegobetancur62599@gmail.com'
# app.config['MAIL_PASSWORD'] = 'lpqk htdg wkhm lsqb'

# mail = Mail(app)

# Importar y registrar los Blueprints
from Controllers.empleados_controller import empleados_bp
from Controllers.facturacion_controller import facturacion_bp
from Controllers.usuarios_controller import usuarios_bp
from Controllers.proyectos_controller import proyectos_bp
from Controllers.estudios_controller import estudios_bp
from Controllers.experiencia_controller import experiencia_bp
from Controllers.administracion_controller import administracion_bp
from Controllers.roles_controller import roles_bp
from Controllers.permisos_controller import permisos_bp

app.register_blueprint(empleados_bp)
app.register_blueprint(facturacion_bp)
app.register_blueprint(proyectos_bp)
app.register_blueprint(estudios_bp)
app.register_blueprint(experiencia_bp)
app.register_blueprint(administracion_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(permisos_bp)
app.register_blueprint(usuarios_bp)

# Definir una función de manejo de errores
def handle_error(error):
    response = {
        "message": str(error),
        "status": 500
    }
    return jsonify(response), 500

@app.errorhandler(Exception)
def handle_all_exceptions(error):
    return handle_error(error)

if __name__ == '__main__':
    with app.app_context():
        inspector = inspect(db.engine)
        print(inspector.get_table_names())
    
    app.run(debug=True)
