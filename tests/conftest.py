import pytest


@pytest.fixture
def sample_operations() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T02:26:55.936673"},
        {"id": 2, "state": "CANCELED", "date": "2023-12-01T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-06-01T15:30:00.000000"},
        {"id": 4, "state": "PENDING", "date": "2024-01-15T08:45:00.000000"},
    ]


@pytest.fixture
def empty_operations() -> list[dict]:
    return []


@pytest.fixture
def same_date_operations() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-05-01T10:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2024-05-01T10:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-04-01T10:00:00.000000"},
    ]
