# src/widget.py
from typing import Any, Dict, List

from src.processing.functions import filter_by_state, sort_by_date


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
