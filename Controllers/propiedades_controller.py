from flask import Blueprint, request, jsonify
from models import db
from models.propiedades import Propiedades

propiedades_bp = Blueprint('propiedades_bp', __name__)

@propiedades_bp.route('/propiedades', methods=['GET'])
def get_propiedades():
    propiedades = Propiedades.query.all()
    return jsonify([propiedad.to_dict() for propiedad in propiedades]), 200

@propiedades_bp.route('/propiedades/<int:id>', methods=['GET'])
def get_propiedad(id):
    propiedad = Propiedades.query.get_or_404(id)
    return jsonify(propiedad.to_dict()), 200

@propiedades_bp.route('/propiedades', methods=['POST'])
def create_propiedad():
    data = request.get_json()
    new_propiedad = Propiedades(
        id=data.get('id'),
        nombre_propiedad=data.get('nombre_propiedad'),
        tipo=data.get('tipo'),
        formato=data.get('formato')
    )
    db.session.add(new_propiedad)
    db.session.commit()
    return jsonify(new_propiedad.to_dict()), 201

@propiedades_bp.route('/propiedades/<int:id>', methods=['PUT'])
def update_propiedad(id):
    propiedad = Propiedades.query.get_or_404(id)
    data = request.get_json()
    propiedad.nombre_propiedad = data.get('nombre_propiedad', propiedad.nombre_propiedad)
    propiedad.tipo = data.get('tipo', propiedad.tipo)
    propiedad.formato = data.get('formato', propiedad.formato)
    db.session.commit()
    return jsonify(propiedad.to_dict()), 200

@propiedades_bp.route('/propiedades/<int:id>', methods=['DELETE'])
def delete_propiedad(id):
    propiedad = Propiedades.query.get_or_404(id)
    db.session.delete(propiedad)
    db.session.commit()
    return jsonify({'message': 'Propiedad eliminada'}), 200
