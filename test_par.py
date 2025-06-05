from par_api import es_par_logico


def test_es_par():
    assert es_par_logico(2) is True
    assert es_par_logico(3) is False
    assert es_par_logico(0) == True
    assert es_par_logico(-2) == True         # Número negativo par
    assert es_par_logico(-3) == False        # Número negativo impar
    assert es_par_logico(1000000) == True    # Número grande par
    assert es_par_logico(1000001) == False   # Número grande impar