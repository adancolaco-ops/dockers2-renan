
import math

from app.exceptions import ApiError
from app.models.calculo import Calculo
from app.repositories.calculo_repository import CalculoRepository


# Operações matemáticas

def _soma(a, b):
    return a + b


def _subtracao(a, b):
    return a - b


def _multiplicacao(a, b):
    return a * b


def _divisao(a, b):
    if b == 0:
        raise ApiError("Divisão por zero não é permitida.")

    return a / b


def _potencia(a, b):
    return a ** b


# Dicionário de operações disponíveis

OPERACOES = {
    "soma": _soma,
    "subtracao": _subtracao,
    "multiplicacao": _multiplicacao,
    "divisao": _divisao,
    "potencia": _potencia
}


class CalculoService:

    @staticmethod
    def calcular(dados):

        if not isinstance(dados, dict):
            raise ApiError("Os dados devem ser enviados em JSON.")

        operacao = dados.get("operacao")
        a = dados.get("a")
        b = dados.get("b")

        if operacao not in OPERACOES:
            raise ApiError(
                "Operação inválida. Utilize: soma, subtracao, multiplicacao, divisao ou potencia."
            )

        if isinstance(a, bool) or isinstance(b, bool):
            raise ApiError("Os valores precisam ser números.")

        try:
            a = float(a)
            b = float(b)
        except (TypeError, ValueError):
            raise ApiError("Os valores precisam ser números válidos.")

        if not math.isfinite(a) or not math.isfinite(b):
            raise ApiError("Os números precisam ser finitos.")

        try:
            resultado = OPERACOES[operacao](a, b)

            if not math.isfinite(resultado):
                raise ApiError("O resultado não é um número finito.")

            resultado = round(resultado, 10)

        except OverflowError:
            raise ApiError("O resultado ultrapassou o limite permitido.")

        calculo = Calculo(
            operacao,
            a,
            b,
            resultado
        )

        return CalculoRepository.salvar(calculo)
