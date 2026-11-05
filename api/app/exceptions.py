
from flask import jsonify


class ApiError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code


def register_error_handlers(app):

    @app.errorhandler(ApiError)
    def handle_api_error(error):
        return jsonify({
            "erro": error.message
        }), error.status_code

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "erro": "Rota não encontrada"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "erro": "Erro interno do servidor"
        }), 500
