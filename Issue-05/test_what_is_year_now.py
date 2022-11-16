from unittest.mock import patch
from what_is_year_now import what_is_year_now
import pytest
from io import StringIO


def test_dmy():
    """Тест для даты формата 'DD.MM.YYYY'."""
    expected_resp = '{"currentDateTime": "15.11.2019"}'
    with patch('urllib.request.urlopen', return_value=StringIO(expected_resp)):
        year = what_is_year_now()
    expected_year = 2019
    assert year == expected_year


def test_ymd():
    """Тест для даты формата 'YYYY-MM-DD'."""
    expected_resp = '{"currentDateTime": "2019-11-15"}'
    with patch('urllib.request.urlopen', return_value=StringIO(expected_resp)):
        year = what_is_year_now()
    expected_year = 2019
    assert year == expected_year


def test_wrong_date_format():
    """Тест для даты в неправильном формате."""
    expected_resp = '{"currentDateTime": "2019/11/15"}'
    with patch('urllib.request.urlopen', return_value=StringIO(expected_resp)):
        with pytest.raises(ValueError):
            what_is_year_now()
