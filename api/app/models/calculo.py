
class Calculo:
    def __init__(self, operacao, a, b, resultado):
        self.operacao = operacao
        self.a = a
        self.b = b
        self.resultado = resultado

    def to_dict(self):
        return {
            "operacao": self.operacao,
            "a": self.a,
            "b": self.b,
            "resultado": self.resultado
        }
