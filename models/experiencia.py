from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Experiencia(db.Model):
    __tablename__ = 'experiencia'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    empresa = db.Column(db.String(45), nullable=True)
    fecha_inicio = db.Column(db.String(45), nullable=True)
    fecha_final = db.Column(db.String(45), nullable=True)
    cargo = db.Column(db.String(45), nullable=True)
    jefe_inmediato = db.Column(db.String(45), nullable=True)
    documento = db.Column(db.String(45), nullable=True)
    empleados_id = db.Column(db.Integer, db.ForeignKey('empleados.id'), primary_key=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'empresa': self.empresa,
            'fecha_inicio': self.fecha_inicio,
            'fecha_final': self.fecha_final,
            'cargo': self.cargo,
            'jefe_inmediato': self.jefe_inmediato,
            'documento': self.documento,
            'empleados_id': self.empleados_id
        }
