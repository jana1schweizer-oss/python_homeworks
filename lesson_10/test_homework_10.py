import logging
from homework_10 import log_event

def test_log_success(caplog):
    with caplog.at_level(logging.INFO):
        log_event("jana", "success")
        assert "Login event - Username: jana, Status: success" in caplog.text

def test_log_expired(caplog):
    with caplog.at_level(logging.WARNING):
        log_event("jana", "expired")
        assert "Login event - Username: jana, Status: expired" in caplog.text

def test_log_failed(caplog):
    with caplog.at_level(logging.ERROR):
        log_event("jana", "failed")
        assert "Login event - Username: jana, Status: failed" in caplog.text
