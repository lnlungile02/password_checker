from password_checker.logger_password_is_valid import log
from _pytest.logging import LogCaptureFixture


def test_log_function(caplog: LogCaptureFixture):
    log
    for record in caplog.records:
        assert record.levelname != "CRITICAL"
    assert "User Password is ok" not in caplog.text
