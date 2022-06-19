from src.consultas import movimientos

"""
Este archivo testea todos los caminos basicos de la funcion movimientos
"""


def test_movimiento_0():
    """
    Este test corresponde al camino basico uno
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(3, 1)
    assert resultado == (3, 1)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_1():
    """
    Este test corresponde al camino basico dos
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(1, 1)
    assert resultado == (1, 1)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_2():
    """
    Este test corresponde al camino basico tres
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(1, 1)
    assert resultado == (1, 1)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_3():
    """
    Este test corresponde al camino basico cuatro
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(1, 4)
    assert resultado == (1, 4)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_4():
    """
    Este test corresponde al camino basico cinco
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(1, 2)
    assert resultado == (1, 2)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_5():
    """
    Este test corresponde al camino basico seis
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(1, 2)
    assert resultado == (1, 2)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_6():
    """
    Este test corresponde al camino basico siete
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(2, 1)
    assert resultado == (2, 1)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_7():
    """
    Este test corresponde al camino basico ocho
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(2, 1)
    assert resultado == (2, 1)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_8():
    """
    Este test corresponde al camino basico nueve
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(2, 2)
    assert resultado == (2, 2)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_9():
    """
    Este test corresponde al camino basico diez
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(2, 2)
    assert resultado == (2, 2)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_10():
    """
    Este test corresponde al camino basico once
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(2,2)
    assert resultado == (2, 2)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_movimiento_11():
    """
    Este test corresponde al camino basico doce
    Chequea que el tipo de dato de ratorno se corresponda con la poscondicion
    """
    resultado = movimientos(2,2)
    assert resultado == (2, 2)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

