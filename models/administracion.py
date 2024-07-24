from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class Administracion(db.Model):
    __tablename__ = 'administracion'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cargo = db.Column(db.String(45), nullable=True)
    dependencia = db.Column(db.String(45), nullable=True)
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cargo': self.cargo,
            'dependencia': self.dependencia,
            'usuarios_id': self.usuarios_id
        }
