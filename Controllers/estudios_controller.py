from flask import Blueprint, request, jsonify
from models import db
from models.estudio import Estudio

estudios_bp = Blueprint('estudios_bp', __name__)


@estudios_bp.route('/estudios', methods=['GET'])
def get_estudios():
    estudios = Estudio.query.all()
    return jsonify([estudio.to_dict() for estudio in estudios]), 200


@estudios_bp.route('/estudios/<int:id>/<int:empleados_id>', methods=['GET'])
def get_estudio(id, empleados_id):
    estudio = Estudio.query.get_or_404((id, empleados_id))
    return jsonify(estudio.to_dict()), 200


@estudios_bp.route('/estudios', methods=['POST'])
def create_estudio():
    data = request.get_json()
    new_estudio = Estudio(
        id=data.get('id'),
        institucion=data.get('institucion'),
        graduado=data.get('graduado'),
        ano_de_grado=data.get('ano_de_grado'),
        titulo=data.get('titulo'),
        documento=data.get('documento'),
        empleados_id=data.get('empleados_id')
    )
    db.session.add(new_estudio)
    db.session.commit()
    return jsonify(new_estudio.to_dict()), 201


@estudios_bp.route('/estudios/<int:id>/<int:empleados_id>', methods=['PUT'])
def update_estudio(id, empleados_id):
    estudio = Estudio.query.get_or_404((id, empleados_id))
    data = request.get_json()
    estudio.institucion = data.get('institucion', estudio.institucion)
    estudio.graduado = data.get('graduado', estudio.graduado)
    estudio.ano_de_grado = data.get('ano_de_grado', estudio.ano_de_grado)
    estudio.titulo = data.get('titulo', estudio.titulo)
    estudio.documento = data.get('documento', estudio.documento)
    db.session.commit()
    return jsonify(estudio.to_dict()), 200




@estudios_bp.route('/estudios/<int:id>/<int:empleados_id>', methods=['DELETE'])
def delete_estudio(id, empleados_id):
    estudio = Estudio.query.get_or_404((id, empleados_id))
    db.session.delete(estudio)
    db.session.commit()
    return jsonify({'message': 'Estudio eliminado'}), 200
