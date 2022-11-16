from unittest.mock import patch
from what_is_year_now import what_is_year_now
import pytest


def test_dmy():
    """Тест для даты формата 'DD.MM.YYYY'."""
    with patch('urllib.request.urlopen'), patch('json.load', return_value={"currentDateTime": "15.11.2019"}):
        year = what_is_year_now()
    expected_year = 2019
    assert year == expected_year


def test_ymd():
    """Тест для даты формата 'YYYY-MM-DD'."""
    with patch('urllib.request.urlopen'), patch('json.load', return_value={"currentDateTime": "2019-11-15"}):
        year = what_is_year_now()
    expected_year = 2019
    assert year == expected_year


def test_wrong_date_format():
    """Тест для даты в неправильном формате."""
    with patch('urllib.request.urlopen'), patch('json.load', return_value={"currentDateTime": "2019/11/15"}):
        with pytest.raises(ValueError):
            what_is_year_now()
