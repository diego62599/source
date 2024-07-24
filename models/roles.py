from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Roles(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(45), nullable=True)
    estado = db.Column(db.Boolean, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'estado': self.estado
        }
