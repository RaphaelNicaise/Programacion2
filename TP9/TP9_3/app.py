from flask import Flask 

from Routes.routes_socio import socios_bp
from Routes.routes_libro import libros_bp
from Routes.routes_prestamo import prestamos_bp

app = Flask(__name__)

app.register_blueprint(libros_bp)
app.register_blueprint(socios_bp)
app.register_blueprint(prestamos_bp)

if __name__ == '__main__':
    app.run(debug=True, port=4000)