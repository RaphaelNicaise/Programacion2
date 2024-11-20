from flask import Flask 
from Routes.routes_socio import socios_bp

app = Flask(__name__)

app.register_blueprint(socios_bp)


if __name__ == '__main__':
    app.run(debug=True, port=4000)