from flask import Blueprint, request, jsonify, current_app
from models import db
from models.facturacion import Facturacion

facturacion_bp = Blueprint('facturacion_bp', __name__)

@facturacion_bp.route('/facturacion', methods=['POST'])
def create_facturacion():
    try:
        data = request.get_json()
        new_facturacion = Facturacion(
            id=data['id'],
            Fecha_factura=data.get('fecha_factura'),
            Precio=data.get('precio')
        )
        db.session.add(new_facturacion)
        db.session.commit()
        current_app.logger.info(f'Facturación creada exitosamente con ID: {new_facturacion.id}')
        return jsonify({'message': 'Facturación creada exitosamente'}), 201
    except Exception as e:
        current_app.logger.error(f'Error al crear facturación: {str(e)}')
        return jsonify({'error': 'Error al crear facturación'}), 500

@facturacion_bp.route('/facturacion/<int:facturacion_id>', methods=['PUT'])
def update_facturacion(facturacion_id):
    try:
        data = request.get_json()
        facturacion = Facturacion.query.get_or_404(facturacion_id)
        
        if 'fecha_factura' in data:
            facturacion.fecha_factura = data['fecha_factura']
        if 'precio' in data:
            facturacion.Precio = data['precio']
        
        db.session.commit()
        current_app.logger.info(f'Facturación actualizada exitosamente con ID: {facturacion.id}')
        return jsonify({'message': 'Facturación actualizada exitosamente'}), 200
    except Exception as e:
        current_app.logger.error(f'Error al actualizar facturación: {str(e)}')
        return jsonify({'error': 'Error al actualizar facturación'}), 500

@facturacion_bp.route('/facturacion/<int:facturacion_id>', methods=['DELETE'])
def delete_facturacion(facturacion_id):
    try:
        facturacion = Facturacion.query.get_or_404(facturacion_id)
        db.session.delete(facturacion)
        db.session.commit()
        current_app.logger.info(f'Facturación eliminada exitosamente con ID: {facturacion.id}')
        return jsonify({'message': 'Facturación eliminada exitosamente'}), 200
    except Exception as e:
        current_app.logger.error(f'Error al eliminar facturación: {str(e)}')
        return jsonify({'error': 'Error al eliminar facturación'}), 500

@facturacion_bp.route('/facturacion', methods=['GET'])
def get_facturaciones():
    try:
        facturaciones = Facturacion.query.all()
        return jsonify([{
            'id': fac.id,
            'fecha_factura': fac.Fecha_factura,
            'precio': fac.Precio
        } for fac in facturaciones]), 200
    except Exception as e:
        current_app.logger.error(f'Error al obtener facturaciones: {str(e)}')
        return jsonify({'error': 'Error al obtener facturaciones'}), 500




