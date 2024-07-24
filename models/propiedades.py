from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Propiedades(db.Model):
    __tablename__ = 'propiedades'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombre_propiedad = db.Column(db.String(45), nullable=True)
    tipo = db.Column(db.String(45), nullable=True)
    formato = db.Column(db.String(45), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre_propiedad': self.nombre_propiedad,
            'tipo': self.tipo,
            'formato': self.formato
        }
