import pytest

from src.widget import get_date, get_ready_operations, mask_account_card


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
    """Одинаковые даты не ломает работу функции."""
    result = get_ready_operations(same_date_operations)
    assert len(result) == 3


@pytest.mark.parametrize(
    "card_info, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счёт 12345678901234567890", "Счёт **7890"),
    ],
)
def test_mask_account_card(card_info: str, expected: str) -> None:
    assert mask_account_card(card_info) == expected


@pytest.mark.parametrize(
    "card_info",
    ["", "   ", "Visa Platinum", "Visa 70007922896abc", "Счет 123"],
)
def test_mask_account_card_invalid(card_info: str) -> None:
    with pytest.raises(ValueError):
        mask_account_card(card_info)


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-01-01", "01.01.2024"),
        ("1999-12-31T23:59:59", "31.12.1999"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    assert get_date(date_string) == expected


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError):
        get_date("")
