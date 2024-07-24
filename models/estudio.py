from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Estudio(db.Model):
    __tablename__ = 'estudios'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    institucion = db.Column(db.String(45), nullable=True)
    graduado = db.Column(db.Boolean, nullable=True)
    ano_de_grado = db.Column(db.String(45), nullable=True)
    titulo = db.Column(db.String(45), nullable=True)
    documento = db.Column(db.String(45), nullable=True)
    empleados_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), primary_key=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'institucion': self.institucion,
            'graduado': self.graduado,
            'ano_de_grado': self.ano_de_grado,
            'titulo': self.titulo,
            'documento': self.documento,
            'empleados_id': self.empleados_id
        }
