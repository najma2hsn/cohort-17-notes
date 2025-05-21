from external_testing import external
from unittest.mock import patch

@patch("external_testing.choice")
def test_external(fake_choice):
    fake_choice.return_value = "A"
    assert isinstance(external(), str)
    assert external() == "A"


def test_fixtures(fixed_number):
    assert fixed_number == 1