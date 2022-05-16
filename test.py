def add(a, b):
    return a + b

def test_add():
    assert add(2, 5) == 5, 'failed int'
    assert add('a', 'b') == 'ab', 'failed str'
