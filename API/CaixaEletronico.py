from collections import OrderedDict


class CaixaEletronico:
    def __init__(self):
        self.cedulas = [100, 50, 20, 10, 5, 2]

    def calcular_cedulas(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("O valor deve ser um inteiro positivo.")

        resultado = OrderedDict()
        for cedula in sorted(self.cedulas, reverse=True):  # Ordenando as cédulas em ordem decrescente
            quantidade, valor = divmod(valor, cedula)
            resultado[cedula] = quantidade

        if valor != 0:
            raise ValueError("Não é possível atender o valor de saque com as cédulas disponíveis.")

        return resultado
