# tests/test_filters.py

import pytest
from filters import line_matches

def test_level_filter():
    line = "2024-06-12 ERROR Servicio caído"
    assert line_matches(line, level="ERROR") is True
    assert line_matches(line, level="INFO") is False

def test_date_filter():
    line = "2024-05-01 INFO Todo en orden"
    assert line_matches(line, from_date="2024-04-01", to_date="2024-06-01") is True
    assert line_matches(line, from_date="2024-06-02") is False

def test_regex_pattern():
    line = "2024-07-01 INFO Usuario Juan accedió al sistema"
    assert line_matches(line, pattern=r"Juan") is True
    assert line_matches(line, pattern=r"Pedro") is False

def test_combined_filters():
    line = "2023-01-15 WARNING Módulo inestable"
    assert line_matches(
        line,
        level="WARNING",
        from_date="2023-01-01",
        to_date="2023-12-31",
        pattern="inestable"
    ) is True
