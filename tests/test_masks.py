import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_card_mask() -> None:
    result = get_mask_card_number("7000792289606361")
    assert result == "7000 79** **** 6361"


def test_account_mask() -> None:
    result = get_mask_account("73654108430135874305")
    assert result == "**4305"


def test_account_short() -> None:
    result = get_mask_account("123456")
    assert result == "**3456"

def test_card_mask_wrong_length() -> None:
    """Номер не из 16 цифр вызывает ValueError."""
    with pytest.raises(ValueError):
        get_mask_card_number("")

