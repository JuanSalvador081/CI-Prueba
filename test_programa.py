import pytest
from main import es_primo  # Reemplaza 'tu_archivo' con el nombre de tu script

@pytest.mark.parametrize("numero, esperado", [
    (2, True),      # 2 es primo
    (3, True),      # 3 es primo
    (4, False),     # 4 no es primo
    (11, True),     # 11 es primo
    (15, False),    # 15 no es primo
    (29, True),     # 29 es primo
    (1, False),     # 1 no es primo
    (0, False),     # 0 no es primo
    (-5, False),    # Números negativos no son primos
    (97, True),     # 97 es primo
])
def test_es_primo(numero, esperado):
    assert es_primo(numero) == esperado

