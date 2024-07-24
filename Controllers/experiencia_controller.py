from flask import Blueprint, request, jsonify
from models import db
from models.experiencia import Experiencia

experiencia_bp = Blueprint('experiencia_bp', __name__)

# GET: Obtener todas las experiencias
@experiencia_bp.route('/experiencias', methods=['GET'])
def get_experiencias():
    experiencias = Experiencia.query.all()
    return jsonify([experiencia.to_dict() for experiencia in experiencias]), 200

# GET: Obtener una experiencia por ID
@experiencia_bp.route('/experiencias/<int:id>/<int:empleados_id>', methods=['GET'])
def get_experiencia(id, empleados_id):
    experiencia = Experiencia.query.get_or_404((id, empleados_id))
    return jsonify(experiencia.to_dict()), 200

# POST: Crear una nueva experiencia
@experiencia_bp.route('/experiencias', methods=['POST'])
def create_experiencia():
    data = request.get_json()
    new_experiencia = Experiencia(
        id=data.get('id'),
        empresa=data.get('empresa'),
        fecha_inicio=data.get('fecha_inicio'),
        fecha_final=data.get('fecha_final'),
        cargo=data.get('cargo'),
        jefe_inmediato=data.get('jefe_inmediato'),
        documento=data.get('documento'),
        empleados_id=data.get('empleados_id')
    )
    db.session.add(new_experiencia)
    db.session.commit()
    return jsonify(new_experiencia.to_dict()), 201

# PUT: Actualizar una experiencia existente
@experiencia_bp.route('/experiencias/<int:id>/<int:empleados_id>', methods=['PUT'])
def update_experiencia(id, empleados_id):
    experiencia = Experiencia.query.get_or_404((id, empleados_id))
    data = request.get_json()
    experiencia.empresa = data.get('empresa', experiencia.empresa)
    experiencia.fecha_inicio = data.get('fecha_inicio', experiencia.fecha_inicio)
    experiencia.fecha_final = data.get('fecha_final', experiencia.fecha_final)
    experiencia.cargo = data.get('cargo', experiencia.cargo)
    experiencia.jefe_inmediato = data.get('jefe_inmediato', experiencia.jefe_inmediato)
    experiencia.documento = data.get('documento', experiencia.documento)
    db.session.commit()
    return jsonify(experiencia.to_dict()), 200

# DELETE: Eliminar una experiencia
@experiencia_bp.route('/experiencias/<int:id>/<int:empleados_id>', methods=['DELETE'])
def delete_experiencia(id, empleados_id):
    experiencia = Experiencia.query.get_or_404((id, empleados_id))
    db.session.delete(experiencia)
    db.session.commit()
    return jsonify({'message': 'Experiencia eliminada'}), 200

