from change import get_change

def test_get_change():
    assert get_change(28) == 6

def test_get_change_small():
    assert get_change(2) == 2
