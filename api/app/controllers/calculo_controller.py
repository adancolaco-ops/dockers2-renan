
from flask import Blueprint, jsonify, request

from app.services.calculo_service import CalculoService
from app.repositories.calculo_repository import CalculoRepository
from app.exceptions import ApiError


calculo_bp = Blueprint("calculos", __name__, url_prefix="/calculos")


# Criar um cálculo
@calculo_bp.post("")
def criar_calculo():
    dados = request.get_json(silent=True)

    resultado = CalculoService.calcular(dados)

    return jsonify(resultado), 201


# Listar cálculos com filtros
@calculo_bp.get("")
def listar_calculos():
    operacao = request.args.get("operacao")
    limite = request.args.get("limite", type=int)

    historico = CalculoRepository.listar(
        operacao=operacao,
        limite=limite
    )

    return jsonify(historico), 200


# Consultar o resumo dos cálculos
@calculo_bp.get("/resumo")
def resumo_calculos():
    resumo = CalculoRepository.resumo()

    return jsonify(resumo), 200


# Consultar um cálculo pelo ID
@calculo_bp.get("/<int:id>")
def buscar_calculo(id):
    calculo = CalculoRepository.buscar_por_id(id)

    if calculo is None:
        raise ApiError("Cálculo não encontrado.", 404)

    return jsonify(calculo), 200


# Excluir um cálculo pelo ID
@calculo_bp.delete("/<int:id>")
def excluir_calculo(id):
    excluido = CalculoRepository.excluir_por_id(id)

    if not excluido:
        raise ApiError("Cálculo não encontrado.", 404)

    return jsonify({
        "mensagem": "Cálculo excluído com sucesso."
    }), 200


# Excluir todo o histórico
@calculo_bp.delete("")
def excluir_todos_calculos():
    quantidade = CalculoRepository.excluir_todos()

    return jsonify({
        "mensagem": "Histórico excluído com sucesso.",
        "quantidade_excluida": quantidade
    }), 200
