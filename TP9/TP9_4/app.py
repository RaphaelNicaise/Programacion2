from flask import Flask 
from Routes.route_polizas import polizas_bp

app = Flask(__name__)

app.register_blueprint(polizas_bp)

if __name__ == '__main__':
    app.run(debug=True, port=4000)