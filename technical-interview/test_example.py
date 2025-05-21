"""Tests example.py"""

from example import pad_with_zeroes
import pytest

def test_pad_with_zeroes_correct_input():
    """Tests that the function works correctly"""
    assert pad_with_zeroes([1, 23, 2, 17, 102]) == ["001", "023", "002", "017", "102"]

def test_pad_with_zeroes_incorrect_input_list_str():
    """Tests that a list of non-integers raises an erros"""
    with pytest.raises(ValueError):
        pad_with_zeroes(["A string"])

def test_pad_with_zeroes_correct_input_large_numbers():
    """Tests that large numbers wont break my code"""
    assert pad_with_zeroes([1111111111111, 1]) == ["1111111111111", "000000000001"]