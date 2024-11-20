from flask import Blueprint, request, jsonify
from Models.Repos.repositorios import getRepoPoliza
from Models.Entities.poliza_inmueble import PolizaInmueble
from Models.Entities.poliza_inmueble_escolar import PolizaInmuebleEscolar

repo_poliza = getRepoPoliza()

polizas_bp = Blueprint('polizas_bp', __name__)

@polizas_bp.route('/polizas', methods=['GET'])
def get_polizas():
    return jsonify([poliza.toDict() for poliza in repo_poliza.getPolizas()])

@polizas_bp.route('/polizas/<int:numero>', methods=['GET'])
def get_poliza(numero):
    poliza = repo_poliza.getPoliza(numero)
    if poliza:
        return jsonify(poliza.toDict())
    return jsonify({'error': 'Poliza no encontrada'}), 404

@polizas_bp.route('/polizas', methods=['POST'])
def add_poliza():
    if request.is_json:
        data = request.get_json()
        
        if 'numero' not in data or 'explosion' not in data or 'incendio' not in data or 'robo' not in data:
            return jsonify({'error': 'Faltan datos'}), 400
        
        if repo_poliza.existeNumero(data['numero']):
            return jsonify({'error': 'El numero de poliza ya existe'}), 400
        
        if 'cantPersonas' in data:
            if 'montoEquipamiento' not in data or 'montoInmobiliario' not in data or 'montoPersona' not in data:
                return jsonify({'error': 'Faltan datos'}), 400
            try:
                poliza = PolizaInmuebleEscolar.fromDict(data)
                repo_poliza.agregarPoliza(poliza)
                return jsonify(poliza.toDict()), 201
            except ValueError as e:
                return jsonify({'error': str(e)}), 400
        else:
            try:
                poliza = PolizaInmueble.fromDict(data)
                repo_poliza.agregarPoliza(poliza)
                return jsonify(poliza.toDict()), 201
            except ValueError as e:
                return jsonify({'error': str(e)}), 400
            
@polizas_bp.route('/polizas/<int:numero>', methods=['DELETE'])
def delete_poliza(numero):
    
    if repo_poliza.existeNumero(numero):
        if repo_poliza.eliminarPoliza(numero):
            return jsonify({'message': 'Poliza eliminada'})
        else:
            return jsonify({'error': 'No se pudo eliminar la poliza'}), 400
    return jsonify({'error': 'Poliza no encontrada'}), 404

            
@polizas_bp.route('/polizas/<int:numero>', methods=['PUT'])
def update_poliza(numero):
    if request.is_json:
        data = request.get_json()
        
        if 'explosion' not in data or 'incendio' not in data or 'robo' not in data:
            return jsonify({'error': 'Faltan datos'}), 400
        
        if not repo_poliza.existeNumero(numero):
            return jsonify({'error': 'Poliza no encontrada'}), 404
        
        if 'cantPersonas' in data and isinstance(repo_poliza.getPoliza(numero), PolizaInmuebleEscolar):
            if 'montoEquipamiento' not in data or 'montoInmobiliario' not in data or 'montoPersona' not in data:
                return jsonify({'error': 'Faltan datos'}), 400
            try:
                repo_poliza.modificarPorNumero(numero, data['incendio'], data['explosion'], data['robo'], data['cantPersonas'], data['montoEquipamiento'], data['montoInmobiliario'], data['montoPersona'])
                return jsonify(repo_poliza.getPoliza(numero).toDict())
            except ValueError as e:
                return jsonify({'error': str(e)}), 400
        else:
            try:
                repo_poliza.modificarPorNumero(numero, data['incendio'], data['explosion'], data['robo'])
                return jsonify(repo_poliza.getPoliza(numero).toDict())
            except ValueError as e:
                return jsonify({'error': str(e)}), 400
            
            
                

