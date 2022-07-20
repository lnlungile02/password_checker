from password_checker.password_checker import (
    check_has_digit,
    check_has_special_char,
    check_has_uppercase,
    check_has_whitespace_char,
    check_password_length,
    check_password_exists,
    check_has_lowercase,
    password_is_valid,
)
from contextlib import nullcontext as does_not_raise
import pytest


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("lkj37KGD@ ", True),
        ("ZIFIkd99@ ", True),
    ),
)
def test_password_valid(input, expected):
    assert password_is_valid(input) == expected, "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        ("", pytest.raises(NameError), "Password should exist"),
        ("123456789", does_not_raise(), None),
    ],
)
def test_password_exists_exception(input, expected, message):
    with expected as e:
        check_password_exists(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("123", True),
        ("1@ ", True),
    ),
)
def test_check_password_exists(input, expected):
    assert (
        check_password_exists(input) == expected
    ), "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        (
            "1234",
            pytest.raises(ValueError),
            "password should be longer than 8 characters",
        ),
        ("123456789", does_not_raise(), None),
    ],
)
def test_password_length_greater_than_8(input, expected, message):
    with expected as e:
        check_password_length(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("abcdefghij", True),
        ("1@444444 ", True),
    ),
)
def test_check_password_length(input, expected):
    assert (
        check_password_length(input) == expected
    ), "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        (
            "123",
            pytest.raises(ValueError),
            "password should have at least one lowercase letter",
        ),
        ("bghu", does_not_raise(), None),
    ],
)
def test_password_has_atleast_one_lowercase(input, expected, message):
    with expected as e:
        check_has_lowercase(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("a", True),
        ("1n@ ", True),
    ),
)
def test_check_has_lowercase(input, expected):
    assert check_has_lowercase(input) == expected, "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        (
            "ghu",
            pytest.raises(ValueError),
            "password should have at least one uppercase letter",
        ),
        ("Gunit", does_not_raise(), None),
    ],
)
def test_password_has_atleast_one_uppercase(input, expected, message):
    with expected as e:
        check_has_uppercase(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("123H", True),
        ("1@GH ", True),
    ),
)
def test_check_has_uppercase(input, expected):
    assert check_has_uppercase(input) == expected, "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        (
            "ghu",
            pytest.raises(ValueError),
            "password should have at least have one digit",
        ),
        ("Gunit2", does_not_raise(), None),
    ],
)
def test_password_has_atleast_one_digit(input, expected, message):
    with expected as e:
        check_has_digit(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("123", True),
        ("1@ ", True),
    ),
)
def test_check_has_digit(input, expected):
    assert check_has_digit(input) == expected, "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        (
            "ghu",
            pytest.raises(ValueError),
            "password should have at least one special character",
        ),
        ("Gunit2@", does_not_raise(), None),
    ],
)
def test_password_has_atleast_one_special_char(input, expected, message):
    with expected as e:
        check_has_special_char(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("123%", True),
        ("1@ ", True),
    ),
)
def test_check_has_special_char(input, expected):
    assert (
        check_has_special_char(input) == expected
    ), "The function output should be true"


@pytest.mark.parametrize(
    ("input,expected,message"),
    [
        (
            "ghu",
            pytest.raises(ValueError),
            "password should have at least one whitespace character",
        ),
        ("Gunit2 ", does_not_raise(), None),
    ],
)
def test_password_has_atleast_one_whitespace_char(input, expected, message):
    with expected as e:
        check_has_whitespace_char(input)
    assert message is None or message in str(e)


@pytest.mark.parametrize(
    ("input, expected"),
    (
        ("123 ", True),
        ("1@ ", True),
    ),
)
def test_check_has_whitespace_char(input, expected):
    assert (
        check_has_whitespace_char(input) == expected
    ), "The function output should be true"


@pytest.mark.parametrize(
    ("input_id", "expected"),
    (
        ("zifiKD123@ ", True),
        ("123KKg@ ", True),
    ),
)
def test_password_is_valid(input_id, expected):
    assert (
        password_is_valid(input_id) == expected
    ), "password is not valid, one or more conditions are not met"
