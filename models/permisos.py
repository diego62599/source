from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Permisos(db.Model):
    __tablename__ = 'permisos'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_permiso = db.Column(db.String(45), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_permiso': self.nombre_permiso
        }
