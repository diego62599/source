from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nombreProyecto = db.Column(db.String(45), nullable=True)
    tipoDeProyecto = db.Column(db.String(45), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombreProyecto': self.nombreProyecto,
            'tipoDeProyecto': self.tipoDeProyecto
        }
