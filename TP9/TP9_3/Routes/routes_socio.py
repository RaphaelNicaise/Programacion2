from flask import Blueprint, request, jsonify
from Models.Entities.socio import Socio
from Models.Repos.repositorios import getRepoSocio

repo_socio = getRepoSocio()

socios_bp = Blueprint('socios_bp', __name__)

@socios_bp.route('/socios', methods=['GET'])
def get_socios():
    return jsonify([socio.toDict() for socio in repo_socio.getSocios()])

@socios_bp.route('/socios/<int:dni>', methods=['GET'])
def get_socio(dni):
    socio = repo_socio.getSocio(dni)
    if socio:
        return jsonify(socio.toDict())
    return jsonify({'error': 'Socio no encontrado'}), 404

@socios_bp.route('/socios', methods=['POST'])
def add_socio():
    if request.is_json:
        data = request.get_json()
        if 'dni' not in data or 'nombre' not in data or 'apellido' not in data or 'mail' not in data or 'fecha_nacimiento' not in data:
            return jsonify({'error': 'Faltan datos'}), 400
        if repo_socio.existeDNI(data['dni']):
            return jsonify({'error': 'El DNI ya existe'}), 400
        
        try:
            socio = Socio.fromDict(data)
            repo_socio.agregarSocio(socio)
            return jsonify(socio.toDict()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'El formato no es JSON'}), 400
    
@socios_bp.route('/socios/<int:dni>', methods=['PUT'])
def update_socio(dni):
    socio = repo_socio.getSocio(dni)
    if socio:
        data = request.get_json()
        if 'nombre' not in data or 'apellido' not in data or 'mail' not in data or 'fecha_nacimiento' not in data:
            return jsonify({'error': 'Faltan datos'}), 400
        if repo_socio.modificarSocio(dni, data['nombre'], data['apellido'], data['mail'], data['fecha_nacimiento']):
            return jsonify({'message': 'Socio actualizado'})
    return jsonify({'error': 'Socio no encontrado'}), 404

@socios_bp.route('/socios/<int:dni>', methods=['DELETE'])
def delete_socio(dni):
    socio = repo_socio.getSocio(dni)
    if socio:
        repo_socio.eliminarPorDNI(dni)
        return jsonify({'message': 'Socio eliminado'})
    return jsonify({'error': 'Socio no encontrado'}), 404