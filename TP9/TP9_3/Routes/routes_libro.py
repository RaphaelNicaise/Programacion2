from flask import Blueprint, jsonify, request
from Models.Entities.libro import Libro
from Models.Repos.repositorios import getRepoLibro

repo_libro = getRepoLibro()

libros_bp = Blueprint('libros_bp', __name__)

# Ruta para obtener todos las libros
@libros_bp.route('/libros', methods=['GET'])
def getLibros():
    return jsonify([libro.toDict() for libro in repo_libro.getLibros()])

# Ruta para obtener un libro por su ISBN
@libros_bp.route('/libros/<isbn>', methods=['GET'])
def getLibro(isbn):
    libro = repo_libro.getLibro(isbn)
    if libro:
        return jsonify(libro.toDict())
    return jsonify({'error': 'Libro no encontrado'}), 404

@libros_bp.route('/libros', methods=['POST'])
def addLibro():
    if request.is_json:
        data = request.get_json()
        if 'ISBN' not in data or 'titulo' not in data or 'autor' not in data or 'anio' not in data or 'genero' not in data:
            return jsonify({'error': 'Faltan datos'}), 400
        if repo_libro.existeISBN(data['ISBN']):
            return jsonify({'error': 'El ISBN ya existe'}), 400
        
        try:
            libro = Libro.fromDict(data)
            repo_libro.agregarLibro(libro)
            return jsonify(libro.toDict()), 201
        
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'El formato no es JSON'}), 400
    
@libros_bp.route('/libros/<isbn>', methods=['DELETE'])
def deleteLibro(isbn):
    libro = repo_libro.getLibro(isbn)
    if libro:
        repo_libro.eliminarPorISBN(isbn)
        return jsonify({'message': 'Libro eliminado'})
    return jsonify({'error': 'Libro no encontrado'}), 404

@libros_bp.route('/libros/<isbn>', methods=['PUT'])
def updateLibro(isbn):
    libro = repo_libro.getLibro(isbn)
    if libro:
        data = request.get_json()
        if 'titulo' not in data or 'autor' not in data or 'genero' not in data or 'anio' not in data:
            return jsonify({'error': 'Faltan datos'}), 400
        if repo_libro.modificarPorISBN(isbn, data['titulo'], data['autor'], data['anio'], data['genero']):
            return jsonify({'message': 'Libro actualizado'})
    return jsonify({'error': 'Libro no encontrado'}), 404