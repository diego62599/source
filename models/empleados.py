from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


from extensions import db  # Usa la instancia global

class Empleado(db.Model):
    __tablename__ = 'empleados'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    valor = db.Column(db.String(45), nullable=True)
    listado = db.Column(db.String(45), nullable=True)
    facturacion_id = db.Column(db.Integer, db.ForeignKey('facturacion.id'), nullable=False)
    profesion = db.Column('Profesíon', db.String(45), nullable=True)  # Nombre de columna con tilde
    usuarios_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    facturacion = relationship("Facturacion", back_populates="empleados")

    def __repr__(self):
        return f"<Empleado(id={self.id}, valor={self.valor}, listado={self.listado}, facturacion_id={self.facturacion_id}, profesion={self.profesion}, usuarios_id={self.usuarios_id})>"
