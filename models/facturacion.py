from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from . import db

class Facturacion(db.Model):
    __tablename__ = 'facturacion'
    id = db.Column(db.Integer, primary_key=True)
    fecha_factura = db.Column(db.String(45), nullable=True)  # Asegúrate de que coincida con el nombre en la base de datos
    precio = db.Column(db.String(45), nullable=True)  # Asegúrate de que coincida con el nombre en la base de datos

    empleados = relationship("empleados", back_populates="facturacion")

    def __repr__(self):
        return f"<Facturacion(id={self.id}, fecha_factura={self.fecha_factura}, precio={self.precio})>"
