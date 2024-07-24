from flask_sqlalchemy import SQLAlchemy

from extensions import db  # Usa la instancia global


class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    Nombre = db.Column(db.String(45), nullable=True)
    Correo = db.Column(db.String(45), nullable=True)
    Contraseña = db.Column(db.String(45), nullable=True)
    Documento = db.Column(db.String(45), nullable=True)
    tipoDocumento = db.Column(db.String(45), nullable=True)
    Apellido = db.Column(db.String(45), nullable=True)
    Direccion = db.Column(db.String(45), nullable=True)
    Telefono = db.Column(db.String(45), nullable=True)
    Usuario = db.Column(db.String(45), nullable=True)
    Sexo = db.Column(db.String(45), nullable=True)
    Fotografia = db.Column(db.String(45), nullable=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'Nombre': self.Nombre,
            'Correo': self.Correo,
            'Contraseña': self.Contraseña,
            'Documento': self.Documento,
            'tipoDocumento': self.tipoDocumento,
            'Apellido': self.Apellido,
            'Direccion': self.Direccion,
            'Telefono': self.Telefono,
            'Usuario': self.Usuario,
            'Sexo': self.Sexo,
            'Fotografia': self.Fotografia
        }
