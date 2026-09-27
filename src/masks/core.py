def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX."""
    clean_number = card_number.replace(" ", "").replace("-", "")

    if len(clean_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    return f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    clean_number = account_number.replace(" ", "").replace("-", "")

    if len(clean_number) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return f"**{clean_number[-4:]}"
