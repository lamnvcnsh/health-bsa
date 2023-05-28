from health_bsa.bsa import BSA
from health_bsa import __version__

def test_version():
    assert __version__ == '0.1.1'

def test_bsa():
    assert BSA(60, 170, "DuBois") == 1.69
    assert BSA(60, 170, "Mosteller") == 1.68
    assert BSA(60, 170, "Haycock") == 1.68
    assert BSA(60, 170, "GehanGeorge") == 1.69
    assert BSA(60, 170, "Fujimoto") == 1.65