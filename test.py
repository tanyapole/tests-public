import torch

def add(a, b):
    return a + b # comment

def test_add():
    assert add(2, 5) == 7, 'failed int'
    assert add('a', 'b') == 'ab', 'failed str'

def test_torch():
    t = torch.tensor([1, 3, 5])
    assert t.sum() == 9, 'failed torch'
