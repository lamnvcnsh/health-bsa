from health_bsa.bsa import compute_bsa
from health_bsa import __version__

def test_version():
    assert __version__ == '0.1.0'

def test_bsa():
    compute_bsa(50, 170) == 1.57