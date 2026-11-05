
from flask import Flask, jsonify

from app.database import init_db
from app.controllers.calculo_controller import calculo_bp
from app.exceptions import register_error_handlers


def create_app():
    app = Flask(__name__)

    # Registra as rotas de cálculos
    app.register_blueprint(calculo_bp)

    # Configura o tratamento de erros
    register_error_handlers(app)

    # Verifica se a API está funcionando
    @app.get("/health")
    def health():
        return jsonify({
            "status": "online",
            "mensagem": "API de calculadora funcionando!"
        }), 200

    # Inicializa o banco de dados
    with app.app_context():
        init_db()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
