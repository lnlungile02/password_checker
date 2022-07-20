import re
from password_checker.logger_password_is_valid import log


@log
def password_is_valid(password):
    if (
        check_password_exists(password)
        and check_password_length(password)
        and check_has_lowercase(password)
        and check_has_uppercase(password)
        and check_has_digit(password)
        and check_has_special_char(password)
        and check_has_whitespace_char(password)
    ):
        return True


def check_password_exists(password):
    if not password:
        raise NameError("Password should exist")
    else:
        return True


def check_password_length(password):
    if len(password) < 8:
        raise ValueError("password should be longer than 8 characters")
    else:
        return True


def check_has_lowercase(password):
    if not re.search(".*[a-z].*", password):
        raise ValueError("password should have at least one lowercase letter")
    else:
        return True


def check_has_uppercase(password):
    if not re.search(".*[A-Z].*", password):
        raise ValueError("password should have at least one uppercase letter")
    else:
        return True


def check_has_digit(password):
    if not re.search(".*[0-9].*", password):
        raise ValueError("password should have at least have one digit")
    else:
        return True


def check_has_special_char(password):
    if not re.search(".*[@_!#$%^&*()<>?/\\|}{~:].*", password):
        raise ValueError("password should have at least one special character")
    else:
        return True


def check_has_whitespace_char(password):
    if not re.search("(.* )", password):
        raise ValueError("password should have at least one whitespace character")
    else:
        return True


def password_strength(password):
    conditions_met = 0
    regex_conditions = [
        "^.{8,}$",
        ".*[a-z].*",
        ".*[A-Z].*",
        ".*[0-9].*",
        ".*[@_!#$%^&*()<>?/\\|}{~:].*",
        "(.* )",
    ]

    for condition in regex_conditions:
        if re.match(condition, password):
            conditions_met += 1
    if password:
        conditions_met += 1

    if not password or password == None or len(password) < 8:
        return "invalid"

    if conditions_met >= 6:
        password_condition = "strong"
    elif conditions_met >= 4:
        password_condition = "medium"
    elif conditions_met == 3:
        password_condition = "weak"
    elif conditions_met <= 2:
        password_condition = "invalid"

    return password_condition


if __name__ == "__main__":
    password_is_valid("a")
