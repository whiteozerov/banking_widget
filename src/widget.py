from datetime import datetime


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: XXXX XX** **** XXXX"""
    if len(card_number) != 16 or not card_number.isdigit():
        return card_number
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account_number(account_number: str) -> str:
    """Маскирует номер счета: **XXXX"""
    if len(account_number) < 4:
        return account_number
    return f"**{account_number[-4:]}"


def mask_account_card(data: str) -> str:
    """
    Обрабатывает строку вида 'Тип Номер'.
    Возвращает замаскированный номер.
    """
    if not data or not isinstance(data, str):
        return data

    parts = data.strip().split()

    if len(parts) != 2:
        return data

    acc_type, number = parts

    if not number.isdigit():
        return data

    if acc_type.lower() == 'счет':
        return f"{acc_type} {get_mask_account_number(number)}"
    else:
        return f"{acc_type} {get_mask_card_number(number)}"


def get_date(iso_string: str) -> str:
    """
    Принимает строку в формате ISO и возвращает строку в формате ДД.ММ.ГГГГ.
    """
    try:
        dt_obj = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S.%f")
        return dt_obj.strftime("%d.%m.%Y")
    except ValueError:
        return iso_string
