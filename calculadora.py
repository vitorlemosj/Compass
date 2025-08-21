"""
Arquivo: calculadora.py
Descrição: Implementação da classe Calculadora com operações matemáticas básicas.
Autor: João Vitor
Referências: Implementado com apoio de inteligência artificial (ChatGPT - OpenAI).
"""

class Calculadora:
    def __init__(self):
        # Lista para registrar o histórico das operações realizadas
        self.historico = []

    def somar(self, numero1, numero2):
        """Realiza a soma entre dois números"""
        resultado = numero1 + numero2
        self.historico.append(f"{numero1} + {numero2} = {resultado}")
        return resultado

    def subtrair(self, numero1, numero2):
        """Realiza a subtração entre dois números"""
        resultado = numero1 - numero2
        self.historico.append(f"{numero1} - {numero2} = {resultado}")
        return resultado

    def multiplicar(self, numero1, numero2):
        """Realiza a multiplicação entre dois números"""
        resultado = numero1 * numero2
        self.historico.append(f"{numero1} * {numero2} = {resultado}")
        return resultado

    def dividir(self, numero1, numero2):
        """Realiza a divisão entre dois números, com tratamento de divisão por zero"""
        if numero2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        resultado = numero1 / numero2
        self.historico.append(f"{numero1} / {numero2} = {resultado}")
        return resultado

    def potencia(self, base, expoente):
        """Calcula a potência sem uso da biblioteca math"""
        resultado = base ** expoente
        self.historico.append(f"{base} ** {expoente} = {resultado}")
        return resultado

    def modulo(self, numero1, numero2):
        """Calcula o resto da divisão (módulo), com tratamento para divisor zero"""
        if numero2 == 0:
            raise ZeroDivisionError("Não é possível calcular módulo com divisor zero.")
        resultado = numero1 % numero2
        self.historico.append(f"{numero1} % {numero2} = {resultado}")
        return resultado

    def mostrar_historico(self):
        """Retorna o histórico de operações realizadas"""
        if not self.historico:
            return ["Nenhuma operação realizada."]
        return self.historico
