from src.transferencias import transferir

"""
Este test recorre los caminos basicos de la funcion transferir
"""


def test_transferir_0():
    """
    Esta funcion recorre el primer camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 3, 1500, 98765)
    assert resultado == (85000, 3564, True, 0, 0)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)

def test_transferir_1():
    """
    Esta funcion recorre el segundo camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 3, 1500, 2765)
    assert resultado == (85000, 3564, False, 0, 0)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)


def test_transferir_2():
    """
    Esta funcion recorre el tercer camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 2, 101500, 98765)
    assert resultado == (85000, 3564, True, 0, 0)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)


def test_transferir_3():
    """
    Esta funcion recorre el cuarto camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 2, 1500, 2765)
    assert resultado == (85000, 2064, False, 0, 1500)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)


def test_transferir_4():
    """
    Esta funcion recorre el quinto camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 1, 101500, 98765)
    assert resultado == (85000, 3564, True, 0, 0)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)


def test_transferir_5():
    """
    Esta funcion recorre el sexto camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 1, 10000, 98765)
    assert resultado == (75000, 3564, True, 10000, 0)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)


def test_transferir_6():
    """
    Esta funcion recorre el septimo camino de transferir
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = transferir(98765, 85000, 3564, 1, 10000, 765)
    assert resultado == (75000, 3564, False, 10000, 0)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)
    assert isinstance(resultado[2], bool)
    assert isinstance(resultado[3], int)
    assert isinstance(resultado[4], int)

