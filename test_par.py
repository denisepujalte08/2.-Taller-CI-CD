from par_api import es_par_logico

def test_es_par():
    assert es_par_logico(2) == True
    assert es_par_logico(3) == False