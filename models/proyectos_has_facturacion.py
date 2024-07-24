from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class ProyectosHasFacturacion(db.Model):
    __tablename__ = 'proyectos_has_Facturacion'
    proyectos_id = db.Column(db.Integer, db.ForeignKey('proyectos.id'), primary_key=True)
    Facturacion_id = db.Column(db.Integer, db.ForeignKey('Facturacion.id'), primary_key=True)


    proyecto = db.relationship('Proyectos', backref='proyecto_rel')
    
    facturacion = db.relationship('Facturacion', backref='facturacion_rel')
