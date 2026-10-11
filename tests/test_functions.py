import pytest

from src.functions import filter_by_state, sort_by_date


def test_filter_by_state_default() -> None:
    """Проверяет, что по умолчанию фильтруются только EXECUTED."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-03"},
        {"id": 2, "state": "CANCELED", "date": "2024-01-02"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-01"},
    ]
    result = filter_by_state(data)
    assert len(result) == 2
    assert all(op["state"] == "EXECUTED" for op in result)


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 1),
])
def test_filter_by_state_states(sample_operations: list[dict], state: str, expected_count: int) -> None:
    """Параметризованная проверка фильтрации по разным статусам."""
    result = filter_by_state(sample_operations, state)
    assert len(result) == expected_count
    assert all(op["state"] == state for op in result)


def test_filter_by_state_empty(empty_operations: list[dict]) -> None:
    """Пустой список — результат тоже пустой."""
    assert filter_by_state(empty_operations, "EXECUTED") == []


def test_filter_by_state_no_match(sample_operations: list[dict]) -> None:
    """Статуса нет ни у одной операции — пустой результат."""
    assert filter_by_state(sample_operations, "ABSENT") == []


def test_sort_by_date_default() -> None:
    """Проверяет, что по умолчанию сортировка идет от новых к старым."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-03"},
        {"id": 2, "state": "EXECUTED", "date": "2024-01-01"},
        {"id": 3, "state": "EXECUTED", "date": "2024-01-02"},
    ]
    result = sort_by_date(data)
    dates = [op["date"] for op in result]
    assert dates == ["2024-01-03", "2024-01-02", "2024-01-01"]


def test_sort_by_date_same_dates(same_date_operations: list[dict]) -> None:
    """Одинаковые даты не ломают сортировку."""
    result = sort_by_date(same_date_operations)
    assert len(result) == 3


def test_sort_by_date_empty(empty_operations: list[dict]) -> None:
    """Пустой список сортируется без ошибок."""
    assert sort_by_date(empty_operations) == []

