from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global

class ListasChequeoHasPropiedades(db.Model):
    __tablename__ = 'listasChequeo_has_propiedades'
    listasChequeo_id = db.Column(db.Integer, db.ForeignKey('listasChequeo.id'), primary_key=True)
    propiedades_id = db.Column(db.Integer, db.ForeignKey('propiedades.id'), primary_key=True)

 
    lista_chequeo = db.relationship('ListasChequeo', backref='listas_chequeo_rel')
    
    propiedad = db.relationship('Propiedades', backref='propiedad_rel')
