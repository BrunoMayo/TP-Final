
from src.consultas import saldo

"""
En este archivo se realian los tests que recorren todos los caminos 
basicos de la funcion saldo
"""

def test_saldo_0():
    """
    Este caso prueba el recorrido del primer camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 3, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_saldo_1():
    """
    Este caso prueba el recorrido del segundo camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 1, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_saldo_2():
    """
    Este caso prueba el recorrido del tercer camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 1, 3)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_saldo_3():
    """
    Este caso prueba el recorrido del cuarto camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 1, 2)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_saldo_4():
    """
    Este caso prueba el recorrido del quinto camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 2, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_saldo_5():
    """
    Este caso prueba el recorrido del sexto camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 2, 3)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_saldo_6():
    """
    Este caso prueba el recorrido del septimo camino basico
    Chequea que se cumpla el tipo de la poscondicion
    """

    resultado = saldo(85000, 3564, 2, 2)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

