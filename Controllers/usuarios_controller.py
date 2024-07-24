from flask import Blueprint, request, jsonify
from models import db
from models.usuarios import Usuario

usuarios_bp = Blueprint('usuarios_bp', __name__)


@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([usuario.to_dict() for usuario in usuarios]), 200


@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    return jsonify(usuario.to_dict()), 200


@usuarios_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    new_usuario = Usuario(
        id=data.get('id'),
        Nombre=data.get('Nombre'),
        Correo=data.get('Correo'),
        Contraseña=data.get('Contraseña'),
        Documento=data.get('Documento'),
        tipoDocumento=data.get('tipoDocumento'),
        Apellido=data.get('Apellido'),
        Direccion=data.get('Direccion'),
        Telefono=data.get('Telefono'),
        Usuario=data.get('Usuario'),
        Sexo=data.get('Sexo'),
        Fotografia=data.get('Fotografia')
    )
    db.session.add(new_usuario)
    db.session.commit()
    return jsonify(new_usuario.to_dict()), 201


@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.get_json()
    usuario.Nombre = data.get('Nombre', usuario.Nombre)
    usuario.Correo = data.get('Correo', usuario.Correo)
    usuario.Contraseña = data.get('Contraseña', usuario.Contraseña)
    usuario.Documento = data.get('Documento', usuario.Documento)
    usuario.tipoDocumento = data.get('tipoDocumento', usuario.tipoDocumento)
    usuario.Apellido = data.get('Apellido', usuario.Apellido)
    usuario.Direccion = data.get('Direccion', usuario.Direccion)
    usuario.Telefono = data.get('Telefono', usuario.Telefono)
    usuario.Usuario = data.get('Usuario', usuario.Usuario)
    usuario.Sexo = data.get('Sexo', usuario.Sexo)
    usuario.Fotografia = data.get('Fotografia', usuario.Fotografia)
    db.session.commit()
    return jsonify(usuario.to_dict()), 200


@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado'}), 200
