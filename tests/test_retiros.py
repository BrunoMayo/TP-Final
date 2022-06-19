from src.retiros import retiros

"""
Este test se encarga de recorrer los caminos de retiros
"""

def test_retiros_0():
    """
    Esta funcion recorre el primer camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 1, 3, 1500, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_1():
    """
    Esta funcion recorre el segundo camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 1, 1, 5000, 1)
    assert resultado == (80000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_2():
    """
    Esta funcion recorre el tercer camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 1, 1, 500000, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_3():
    """
    Esta funcion recorre el cuarto camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 3, 1, 500000, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_4():
    """
    Esta funcion recorre el quinto camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 2, 1, 500000, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_5():
    """
    Esta funcion recorre el sexto camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 2, 1, 564, 0)
    assert resultado == (85000, 3000)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_6():
    """
    Esta funcion recorre el septimo camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 2, 1, 3000, 1)
    assert resultado == (85000, 564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_7():
    """
    Esta funcion recorre el octavo camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 1, 2, 30000, 0)
    assert resultado == (55000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

def test_retiros_8():
    """
    Esta funcion recorre el noveno camino de retiros
    Tambien chequea que el tipo de retorno se corresponda con la poscondicion
    """
    resultado = retiros(85000, 3564, 1, 2, 300000, 1)
    assert resultado == (85000, 3564)
    assert isinstance(resultado[0], int)
    assert isinstance(resultado[1], int)

