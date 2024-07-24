from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class ListasChequeo(db.Model):
    __tablename__ = 'listas_chequeo'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre = db.Column(db.String(45), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }
