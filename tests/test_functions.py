import pytest
from src.processing.functions import filter_by_state, sort_by_date

def test_filter_by_state_default():
    """Проверяет, что по умолчанию фильтруются только EXECUTED."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-03"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01"},
    ]
    result = filter_by_state(data)  # не передаем state, берем default
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)

def test_sort_by_date_default():
    """Проверяет, что по умолчанию сортировка идет от новых к старым (reverse=True)."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-03"},
        {"id": 2, "state": "EXECUTED", "date": "2024-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-02"},
    ]
    result = sort_by_date(data)  # не передаем reverse, берем default True
    dates = [op["date"] for op in result]
    assert dates == ["2024-01-03", "2024-01-02", "2024-01-01"]
