from par_api import es_par_logico


def test_es_par():
    assert es_par_logico(2)
    assert not es_par_logico(3)
    assert es_par_logico(0)
    assert es_par_logico(-2)         # Número negativo par
    assert not es_par_logico(-3)     # Número negativo impar
    assert es_par_logico(1000000)    # Número grande par
    assert not es_par_logico(1000001)  # Número grande impar
