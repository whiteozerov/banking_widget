# src/widget.py
from datetime import datetime
from typing import Any, Dict, List

from .functions import filter_by_state, sort_by_date
from .masks import get_mask_account, get_mask_card_number


def get_ready_operations(operations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Готовит список операций для виджета: фильтрует и сортирует.

    Args:
        operations: Список словарей с данными об операциях.

    Returns:
        Отфильтрованный и отсортированный список операций.
    """
    # 1. Фильтруем по статусу (по умолчанию EXECUTED)
    filtered = filter_by_state(operations)

    # 2. Сортируем по дате (по умолчанию новые сначала)
    sorted_ops = sort_by_date(filtered)

    return sorted_ops


def get_date(date_string: str) -> str:
    """Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.
    :rtype: str
    """
    if not date_string:
        raise ValueError("Передана пустая строка")
    dt = datetime.fromisoformat(date_string)
    return dt.strftime("%d.%m.%Y")


def mask_account_card(card_info: str) -> str:
    """Маскирует номер карты или счёта в строке с названием."""
    if not card_info or not card_info.strip():
        raise ValueError("Передана пустая строка")

    name, _, number = card_info.strip().rpartition(" ")
    if not name or not number.isdigit():
        raise ValueError("Некорректный формат входных данных")

    if len(number) == 20:
        return f"{name} {get_mask_account(number)}"
    return f"{name} {get_mask_card_number(number)}"
