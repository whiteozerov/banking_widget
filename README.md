# Banking Widget

## Цель проекта

Модуль для фильтрации и сортировки банковских транзакций. Реализованы функции `filter_by_state` (фильтрация по статусу) и `sort_by_date` (сортировка по дате).

## Установка и запуск

Проект использует Poetry.

```bash
git clone https://github.com/whiteozerov/banking_widget.git
cd banking_widget
poetry install
poetry run pytest
```

## Примеры использования

### Фильтрация по статусу (filter_by_state)

Отбирает транзакции по указанному статусу.

```python
from src.functions import filter_by_state

transactions = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
    {"id": 3, "state": "EXECUTED"},
]

result = filter_by_state(transactions, "EXECUTED")
# Возвращает транзакции с id 1 и 3
```

### Сортировка по дате (sort_by_date)

Сортирует транзакции по дате в порядке убывания.

```python
from src.functions import sort_by_date

transactions = [
    {"id": 1, "date": "2024-01-03"},
    {"id": 2, "date": "2024-01-01"},
    {"id": 3, "date": "2024-01-02"},
]

result = sort_by_date(transactions)
# Порядок: id 1, id 3, id 2
```

## Тестирование

Проект покрыт тестами pytest (фикстуры, параметризация), покрытие кода более 80%.

Запуск тестов:

```bash
poetry run pytest
```

Запуск с отчётом о покрытии (HTML-отчёт сохраняется в папке `htmlcov`):

```bash
poetry run pytest --cov=src --cov-report=html
```
