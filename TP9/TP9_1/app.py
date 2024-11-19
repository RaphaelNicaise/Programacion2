from flask import Flask 
from Routes.routes_libro import libros_bp

app = Flask(__name__)

app.register_blueprint(libros_bp) # Importa el blueprint que le asignemos

if __name__ == '__main__':
    app.run(debug=True, port=4000)
    
    