# tests/test_lib.py
from gsproject.lib import try_me

def test_try_me():
    assert len(try_me('Gabi',737)) != 0