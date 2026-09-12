"""
Unit tests for netguard.scanner (pure parsing logic only, no live sockets).
"""

import pytest
from netguard.scanner import parse_port_range


def test_parse_single_port():
    assert parse_port_range("80") == [80]


def test_parse_comma_separated():
    assert parse_port_range("80,443,8080") == [80, 443, 8080]


def test_parse_range():
    assert parse_port_range("1-5") == [1, 2, 3, 4, 5]


def test_parse_mixed():
    result = parse_port_range("22,80-82,443")
    assert result == [22, 80, 81, 82, 443]


def test_parse_deduplicates():
    result = parse_port_range("80,80,443")
    assert result == [80, 443]


def test_parse_invalid_range_raises():
    with pytest.raises(ValueError):
        parse_port_range("100-1")


def test_parse_out_of_bounds_raises():
    with pytest.raises(ValueError):
        parse_port_range("70000")
