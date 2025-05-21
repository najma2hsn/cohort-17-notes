import pytest

from main import translate_sequence_to_letter, is_valid_woof


def test_translate_sequence_to_letter_valid_input_1():

    res = translate_sequence_to_letter(["woof"])

    assert res == "a"


def test_translate_sequence_to_letter_valid_input_2():

    res = translate_sequence_to_letter(["woof", "woof"])

    assert res == "b"


def test_translate_sequence_to_letter_valid_input_3():

    res = translate_sequence_to_letter(["woof", "woof", "woof", "woof", "woof", "woof"])

    assert res == "f"


def test_translate_sequence_to_letter_raises_error_on_empty():

    with pytest.raises(ValueError):
        translate_sequence_to_letter([])


def test_is_valid_woof_valid_input_1():

    assert is_valid_woof("woof")


def test_is_valid_woof_valid_input_2():

    assert is_valid_woof("WOOF")


def test_is_valid_woof_valid_input_3():

    assert is_valid_woof("wolof")


def test_is_valid_woof_valid_input_4():

    assert not is_valid_woof("foow")