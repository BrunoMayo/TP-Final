from src.consultas import consultas

"""
Esta test recorre los caminos basicos de consultas
"""

def test_consultas_0():
    """
    Esta funcion testea el primer camino basico de consultas
    Tambien chequea que el tipo del valor retornado se corresponda con la poscondicion
    """
    resultado = consultas(85000, 3564, 1, 1, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_consultas_1():
    """
    Esta funcion testea el segundo camino basico de consultas
    Tambien chequea que el tipo del valor retornado se corresponda con la poscondicion
    """
    resultado = consultas(85000, 3564, 2, 1, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_consultas_2():
    """
    Esta funcion testea el tercer camino basico de consultas
    Tambien chequea que el tipo del valor retornado se corresponda con la poscondicion
    """
    resultado = consultas(85000, 3564, 3, 1, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)