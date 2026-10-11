from src.widget import get_ready_operations


def test_get_ready_operations_default(sample_operations: list[dict]) -> None:
    """По умолчанию оставляет только EXECUTED и сортирует от новых к старым."""
    result = get_ready_operations(sample_operations)
    states = [op["state"] for op in result]
    assert all(state == "EXECUTED" for state in states)
    dates = [op["date"] for op in result]
    assert dates == sorted(dates, reverse=True)


def test_get_ready_operations_empty(empty_operations: list[dict]) -> None:
    """Пустой список — пустой результат."""
    assert get_ready_operations([]) == []


def test_get_ready_operations_single(same_date_operations: list[dict]) -> None:
    """Одинаковые даты не ломают работу функции."""
    result = get_ready_operations(same_date_operations)
    assert len(result) == 3
