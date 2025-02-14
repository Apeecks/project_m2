from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(unsorted_list_state: list, state_canceled: str, state_executed: list) -> Any:
    """Проверка функции filter_by_state"""
    assert filter_by_state(unsorted_list_state, "EXECUTED") == state_executed
    assert filter_by_state(unsorted_list_state, "CANCELED") == state_canceled
    assert filter_by_state(unsorted_list_state) == state_executed


# @pytest.mark.parametrize(
#     "state, result",
#     [
#         ("", "Аргумент state, не найден в списке"),
#         ("Hi!", "Аргумент state, не найден в списке"),
#         ("1234567890", "Аргумент state, не найден в списке"),
#     ]
# )
# def test_error_filter_by_state(unsorted_list: list, state: str, result: list) -> Any:
#     """Проверка функции filter_by_state на ошибки"""
#     with pytest.raises(ValueError) as file:
#         filter_by_state(unsorted_list, state)
#     assert str(file.value) == result


def test_sort_by_date(unsorted_list_date: list, sorted_list_date: list, reverse_sorted_list_date: list) -> Any:
    """Проверка функции sort_by_date"""
    assert sort_by_date(unsorted_list_date) == sorted_list_date
    assert sort_by_date(unsorted_list_date, False) == reverse_sorted_list_date


@pytest.mark.parametrize(
    "data_sort_list, result",
    [
        ([{"id": 939719570, "state": "EXECUTED", "date": "18-06-30T02:08:58.425572"}], "Неверный формат"),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2025-06T02:08:58.425572"}], "Неверный формат"),
        ([{"id": 939719570, "state": "EXECUTED", "date": "T02:08:58.425572"}], "Неверный формат"),
    ]
)
def test_error_sort_by_data(data_sort_list: list, result: str) -> Any:
    """Проверка функции sort_by_date на ошибки"""
    with pytest.raises(ValueError) as file:
        sort_by_date(data_sort_list)
    assert str(file.value) == result
