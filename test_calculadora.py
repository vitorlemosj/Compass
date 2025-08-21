"""
Arquivo: test_calculadora.py
Descrição: Testes unitários para a classe Calculadora utilizando pytest.
Autor: João Vitor
Referências: Implementado com apoio de inteligência artificial (ChatGPT - OpenAI).
"""

import pytesgit t
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

def test_somar(calc):
    assert calc.somar(2, 3) == 5

def test_subtrair(calc):
    assert calc.subtrair(10, 4) == 6

def test_multiplicar(calc):
    assert calc.multiplicar(3, 7) == 21

def test_dividir(calc):
    assert calc.dividir(20, 5) == 4

def test_dividir_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.dividir(10, 0)

def test_potencia(calc):
    assert calc.potencia(2, 3) == 8

def test_modulo(calc):
    assert calc.modulo(10, 3) == 1

def test_modulo_por_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.modulo(10, 0)

def test_historico(calc):
    calc.somar(2, 2)
    calc.subtrair(5, 3)
    historico = calc.mostrar_historico()
    assert historico == ["2 + 2 = 4", "5 - 3 = 2"]
