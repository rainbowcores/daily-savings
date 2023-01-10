import pytest
from app.save import get_day_number

def test_date_calculation_first_day():
    assert get_day_number('01-01-2023') == 1

def test_date_calculation_last_day():
    assert get_day_number('31-12-2023') == 365