import pytest

from shop.cart import price

def test_empty():
    assert 0 == price([])

def test_basics():
    assert 8     == price([1])
    assert 8     == price([2])
    assert 8     == price([3])
    assert 8     == price([4])
    assert 8 * 3 == price([1, 1, 1])

def test_simple_discounts():
    assert 8 * 2 * 0.95 == price([0, 1])
    assert 8 * 3 * 0.9  == price([0, 2, 4])
    assert 8 * 4 * 0.8  == price([0, 1, 2, 4])
    assert 8 * 5 * 0.75 == price([0, 1, 2, 3, 4])

def test_several_discounts():
    assert 8 + (8 * 2 * 0.95)             == price([0, 0, 1])
    assert 2 * (8 * 2 * 0.95)             == price([0, 0, 1, 1])
    assert (8 * 4 * 0.8) + (8 * 2 * 0.95) == price([0, 0, 1, 2, 2, 3])
    assert 8 + (8 * 5 * 0.75)             == price([0, 1, 1, 2, 3, 4])

def test_edge_cases():
    assert 2 * (8 * 4 * 0.8) == price([0, 0, 1, 1, 2, 2, 3, 4])
    assert 3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8) == price([0, 0, 0, 0, 0, 
                                                            1, 1, 1, 1, 1, 
                                                            2, 2, 2, 2, 
                                                            3, 3, 3, 3, 3, 
                                                            4, 4, 4, 4])

