from flask import Blueprint, jsonify, request

from Models.Entities.prestamo import Prestamo
from Models.Repos.repositorios import getRepoPrestamo, getRepoLibro, getRepoSocio

repo_prestamo = getRepoPrestamo()
repo_libro = getRepoLibro()
repo_socio = getRepoSocio()

prestamos_bp = Blueprint('prestamos_bp', __name__)

@prestamos_bp.route('/prestamos', methods=['GET'])
def get_prestamos():
    return jsonify([prestamo.toDict() for prestamo in repo_prestamo.getPrestamos()])

@prestamos_bp.route('/prestamos/<id>', methods=['GET'])
def get_prestamo(id):
    prestamo = repo_prestamo.getPrestamo(int(id))
    if prestamo:
        return jsonify(prestamo.toDict())
    return jsonify({'error': 'Prestamo no encontrado'})

@prestamos_bp.route('/prestamos/<id>', methods=['DELETE'])
def delete_prestamo(id):
    if repo_prestamo.eliminarPorID(int(id)):
        return jsonify({'success': True})
    return jsonify({'success': False})

@prestamos_bp.route('/prestamos', methods=['POST'])
def add_prestamo():
    data = request.get_json()
    try:
        
        if not repo_libro.existeISBN(data['libro_isbn']):
            raise ValueError('El libro no existe')
        if not repo_socio.existeDNI(data['socio_dni']):
            raise ValueError('El socio no existe')
        if repo_libro.getLibro(data['libro_isbn']).getEjemplares() < 0:
            raise ValueError('No hay ejemplares disponibles')
        if 'fecha_retiro' not in data:
            raise ValueError('Falta la fecha de retiro')
        if 'cant_dias' not in data:
            raise ValueError('Falta la cantidad de días')
        
        repo_libro.getLibro(data['libro_isbn']).restar_ejemplar()
        
        prestamo = Prestamo.fromDict(data)
        repo_prestamo.agregarPrestamo(prestamo)
        
        return jsonify({'success': True})
    
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)})





