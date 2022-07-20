from password_checker.password_checker import password_strength
import pytest


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("", "invalid"),
        ("          ", "weak"),
    ),
)
def test_password_length_output(input, expected):
    assert (
        password_strength(input) == expected
    ), "The function does not return invalid for empty string"


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("1234567", "invalid"),
        ("abcdefg", "invalid"),
    ),
)
def test_password_invalid_for_two_conditions_or_less(input, expected):
    assert (
        password_strength(input) == expected
    ), "The function output should be invalid for two or less conditions"


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("abcdefgh", "weak"),
        ("12345678", "weak"),
        ("", "invalid"),
    ),
)
def test_password_weak_for_three_conditions(input, expected):
    assert (
        password_strength(input) == expected
    ), "The function output should be weak for three conditions"


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("abcd1234H", "medium"),
        ("1234567@ ", "medium"),
        ("", "invalid"),
    ),
)
def test_password_medium_for_four_conditions(input, expected):
    assert (
        password_strength(input) == expected
    ), "The function output should be medium for four and five conditions"


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("zifiKD2@ ", "strong"),
        ("Loot@ 6b", "strong"),
        ("Loot", "invalid"),
    ),
)
def test_password_strong_for_six_conditions(input, expected):
    assert (
        password_strength(input) == expected
    ), "The function output should be strong for six conditions"
