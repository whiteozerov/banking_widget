from masks import get_mask_card_number, get_mask_account


def test_card_mask():
    result = get_mask_card_number("7000792289606361")
    assert result == "7000 79** **** 6361"


def test_account_mask():
    result = get_mask_account("73654108430135874305")
    assert result == "**4305"


def test_account_short():
    result = get_mask_account("123456")
    assert result == "**3456"

